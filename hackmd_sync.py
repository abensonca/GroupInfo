#!/usr/bin/env python3
"""Sync HackMD team notes with this Git repo.

Subcommands:
  init <team-path>   Initialize sync config in this repo.
  pull               Fetch remote changes into local files.
  push               Send local changes to HackMD.
  sync               Pull then push.
  status             Show what would change without touching anything.

State is tracked in .hackmd-sync-state.json (committed) so that conflict
detection works across machines. The HackMD API token is read from the
HACKMD_API_TOKEN environment variable, or from a local .env file.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Optional

import requests

API_BASE = "https://api.hackmd.io/v1"
CONFIG_FILE = ".hackmd-sync.json"
STATE_FILE = ".hackmd-sync-state.json"
DEFAULT_NOTES_DIR = "notes"
CONFLICT_SUFFIX = ".remote.md"


# --------------------------------------------------------------------------- #
# HackMD client
# --------------------------------------------------------------------------- #

class HackMDError(RuntimeError):
    pass


class HackMDClient:
    def __init__(self, token: str, team_path: str):
        self.team_path = team_path
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        })

    def _request(self, method: str, path: str, **kwargs):
        url = f"{API_BASE}{path}"
        last_exc: Optional[Exception] = None
        for attempt in range(5):
            try:
                resp = self.session.request(method, url, timeout=30, **kwargs)
            except requests.RequestException as e:
                last_exc = e
                time.sleep(2 ** attempt)
                continue
            if resp.status_code == 429:
                wait = int(resp.headers.get("Retry-After", 2 ** attempt))
                time.sleep(wait)
                continue
            if resp.status_code >= 500:
                time.sleep(2 ** attempt)
                continue
            if not resp.ok:
                raise HackMDError(
                    f"{method} {path} -> {resp.status_code}: {resp.text}"
                )
            if not resp.content:
                return None
            return resp.json()
        raise HackMDError(f"{method} {path} failed after retries: {last_exc}")

    def list_team_notes(self):
        return self._request("GET", f"/teams/{self.team_path}/notes")

    def get_team_note(self, note_id: str):
        return self._request("GET", f"/teams/{self.team_path}/notes/{note_id}")

    def create_team_note(self, title: str, content: str):
        return self._request(
            "POST",
            f"/teams/{self.team_path}/notes",
            json={"title": title, "content": content},
        )

    def update_team_note(self, note_id: str, content: str, title: Optional[str] = None):
        payload = {"content": content}
        if title is not None:
            payload["title"] = title
        return self._request(
            "PATCH",
            f"/teams/{self.team_path}/notes/{note_id}",
            json=payload,
        )


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #

def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        value = value.strip().strip("'").strip('"')
        os.environ.setdefault(key.strip(), value)


def get_token() -> str:
    load_env_file(Path.cwd() / ".env")
    token = os.environ.get("HACKMD_API_TOKEN")
    if not token:
        sys.exit("HACKMD_API_TOKEN is not set (env var or .env file).")
    return token


def slugify(title: str, max_len: int = 60) -> str:
    s = (title or "").strip().lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    s = re.sub(r"[\s_]+", "-", s)
    s = s.strip("-")
    return (s[:max_len] or "untitled").rstrip("-")


def filename_for(note_id: str, title: str) -> str:
    short = re.sub(r"[^A-Za-z0-9]", "", note_id)[:8] or "noteid"
    return f"{slugify(title)}-{short}.md"


def hash_content(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def extract_title(content: str) -> Optional[str]:
    """Best-effort title detection: first H1 line, ignoring YAML front matter."""
    lines = content.splitlines()
    i = 0
    if lines and lines[0].strip() == "---":
        for j in range(1, len(lines)):
            if lines[j].strip() == "---":
                i = j + 1
                break
    for line in lines[i:]:
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
        if stripped:
            break
    return None


def to_millis(value) -> int:
    """HackMD typically returns ms-since-epoch numbers; be defensive."""
    if value is None:
        return 0
    if isinstance(value, (int, float)):
        return int(value)
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def load_json(path: Path, default):
    if path.exists():
        return json.loads(path.read_text() or "null") or default
    return default


def save_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")


def repo_root() -> Path:
    return Path.cwd()


def load_config(repo: Path) -> dict:
    config = load_json(repo / CONFIG_FILE, None)
    if config is None:
        sys.exit(
            f"Missing {CONFIG_FILE}. Run `python hackmd_sync.py init <team-path>` first."
        )
    return config


# --------------------------------------------------------------------------- #
# Commands
# --------------------------------------------------------------------------- #

def cmd_init(args) -> None:
    repo = repo_root()
    config_path = repo / CONFIG_FILE
    if config_path.exists():
        sys.exit(f"{CONFIG_FILE} already exists.")
    save_json(config_path, {
        "team_path": args.team_path,
        "notes_dir": args.notes_dir,
    })
    state_path = repo / STATE_FILE
    if not state_path.exists():
        save_json(state_path, {"notes": {}})
    (repo / args.notes_dir).mkdir(parents=True, exist_ok=True)
    print(f"Initialized HackMD sync for team '{args.team_path}'.")
    print(f"  notes dir: {args.notes_dir}/")
    print(f"  config:    {CONFIG_FILE}")
    print(f"  state:     {STATE_FILE}")


def _resolve_unique_path(notes_dir: Path, base_name: str) -> Path:
    candidate = notes_dir / base_name
    if not candidate.exists():
        return candidate
    stem = candidate.stem
    counter = 2
    while True:
        candidate = notes_dir / f"{stem}-{counter}.md"
        if not candidate.exists():
            return candidate
        counter += 1


def _do_sync(pull: bool, push: bool, dry_run: bool) -> int:
    repo = repo_root()
    config = load_config(repo)
    notes_dir = repo / config.get("notes_dir", DEFAULT_NOTES_DIR)
    notes_dir.mkdir(parents=True, exist_ok=True)
    state = load_json(repo / STATE_FILE, {"notes": {}})
    state_notes: dict = dict(state.get("notes", {}))

    client = HackMDClient(get_token(), config["team_path"])
    print(f"Listing team notes for '{config['team_path']}'...")
    remote_list = client.list_team_notes() or []
    remote_by_id = {n["id"]: n for n in remote_list}

    new_state: dict = {}
    now_ms = int(time.time() * 1000)
    actions = 0

    # ---------------- Pull phase ---------------- #
    if pull:
        for nid, meta in remote_by_id.items():
            tracked = state_notes.get(nid)
            remote_changed = to_millis(meta.get("lastChangedAt") or meta.get("createdAt"))

            if tracked is None:
                detail = client.get_team_note(nid)
                content = detail.get("content") or ""
                title = detail.get("title") or extract_title(content) or "untitled"
                fpath = _resolve_unique_path(notes_dir, filename_for(nid, title))
                rel = fpath.relative_to(repo)
                print(f"  pull (new):  {rel}")
                actions += 1
                if not dry_run:
                    fpath.write_text(content)
                new_state[nid] = {
                    "filename": fpath.name,
                    "title": title,
                    "last_changed_at": remote_changed,
                    "content_hash": hash_content(content),
                    "last_synced_at": now_ms,
                }
                continue

            fpath = notes_dir / tracked["filename"]
            local_content = fpath.read_text() if fpath.exists() else ""
            local_hash = hash_content(local_content)
            local_modified = fpath.exists() and local_hash != tracked.get("content_hash")
            remote_modified = remote_changed > to_millis(tracked.get("last_changed_at"))

            if remote_modified:
                detail = client.get_team_note(nid)
                rcontent = detail.get("content") or ""
                rtitle = detail.get("title") or tracked.get("title") or "untitled"
                if local_modified and hash_content(rcontent) != local_hash:
                    conflict_path = fpath.with_name(fpath.stem + CONFLICT_SUFFIX)
                    print(
                        f"  CONFLICT:    {fpath.relative_to(repo)}"
                        f"  (remote written to {conflict_path.name})"
                    )
                    actions += 1
                    if not dry_run:
                        conflict_path.write_text(rcontent)
                    new_state[nid] = tracked  # keep state until user resolves
                    continue
                print(f"  pull:        {fpath.relative_to(repo)}")
                actions += 1
                if not dry_run:
                    fpath.write_text(rcontent)
                new_state[nid] = {
                    "filename": fpath.name,
                    "title": rtitle,
                    "last_changed_at": remote_changed,
                    "content_hash": hash_content(rcontent),
                    "last_synced_at": now_ms,
                }
            else:
                new_state[nid] = tracked
    else:
        for nid in set(state_notes) & set(remote_by_id):
            new_state[nid] = state_notes[nid]

    # ---------------- Push phase ---------------- #
    if push:
        # Update tracked notes whose local content has changed.
        for nid, tracked in list(new_state.items()):
            if nid not in remote_by_id:
                continue
            fpath = notes_dir / tracked["filename"]
            if not fpath.exists():
                continue
            local_content = fpath.read_text()
            local_hash = hash_content(local_content)
            if local_hash == tracked.get("content_hash"):
                continue
            remote_changed = to_millis(remote_by_id[nid].get("lastChangedAt"))
            if remote_changed > to_millis(tracked.get("last_changed_at")):
                print(
                    f"  WARN:        remote changed since last sync for "
                    f"{fpath.relative_to(repo)}; run `pull` first. Skipping push."
                )
                continue
            new_title = extract_title(local_content) or tracked.get("title")
            print(f"  push:        {fpath.relative_to(repo)}")
            actions += 1
            if not dry_run:
                client.update_team_note(nid, local_content, title=new_title)
                refreshed = client.get_team_note(nid)
                new_state[nid] = {
                    "filename": fpath.name,
                    "title": refreshed.get("title") or new_title or tracked.get("title"),
                    "last_changed_at": to_millis(refreshed.get("lastChangedAt")) or now_ms,
                    "content_hash": hash_content(local_content),
                    "last_synced_at": now_ms,
                }

        # Create new notes from untracked local .md files.
        tracked_filenames = {info["filename"] for info in new_state.values()}
        for fpath in sorted(notes_dir.glob("*.md")):
            if fpath.name in tracked_filenames:
                continue
            if fpath.name.endswith(CONFLICT_SUFFIX):
                continue
            local_content = fpath.read_text()
            title = extract_title(local_content) or fpath.stem
            print(f"  create:      {fpath.relative_to(repo)} -> HackMD")
            actions += 1
            if dry_run:
                continue
            created = client.create_team_note(title, local_content)
            nid = created["id"]
            new_name = filename_for(nid, title)
            new_path = fpath
            if fpath.name != new_name:
                target = notes_dir / new_name
                if not target.exists():
                    fpath.rename(target)
                    new_path = target
            refreshed = client.get_team_note(nid)
            new_state[nid] = {
                "filename": new_path.name,
                "title": refreshed.get("title") or title,
                "last_changed_at": to_millis(refreshed.get("lastChangedAt")) or now_ms,
                "content_hash": hash_content(local_content),
                "last_synced_at": now_ms,
            }

    # ---------------- Deletion warnings ---------------- #
    deleted_remote = set(state_notes) - set(remote_by_id)
    for nid in deleted_remote:
        info = state_notes[nid]
        print(
            f"  WARN:        '{info.get('title')}' ({info['filename']}) is in "
            f"{STATE_FILE} but no longer on HackMD. Local file kept; remove the "
            f"entry from {STATE_FILE} (and delete the file) to forget it."
        )
        new_state.setdefault(nid, info)

    for nid, info in state_notes.items():
        if nid not in remote_by_id:
            continue
        fpath = notes_dir / info["filename"]
        if not fpath.exists():
            print(
                f"  WARN:        local file '{info['filename']}' is missing but "
                f"the note still exists on HackMD. Not deleting remotely."
            )
            new_state.setdefault(nid, info)

    if not dry_run:
        save_json(repo / STATE_FILE, {"notes": new_state})

    suffix = " (dry run)" if dry_run else ""
    if actions == 0:
        print(f"Up to date.{suffix}")
    else:
        print(f"Done: {actions} action(s).{suffix}")
    return actions


def cmd_pull(args) -> None:
    _do_sync(pull=True, push=False, dry_run=args.dry_run)


def cmd_push(args) -> None:
    _do_sync(pull=False, push=True, dry_run=args.dry_run)


def cmd_sync(args) -> None:
    _do_sync(pull=True, push=True, dry_run=args.dry_run)


def cmd_status(args) -> None:
    _do_sync(pull=True, push=True, dry_run=True)


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init", help="Initialize sync config in this repo.")
    p_init.add_argument("team_path", help="HackMD team path (URL slug, e.g. 'my-team').")
    p_init.add_argument("--notes-dir", default=DEFAULT_NOTES_DIR,
                        help=f"Directory for note files (default: {DEFAULT_NOTES_DIR}).")
    p_init.set_defaults(func=cmd_init)

    for name, fn, desc in [
        ("pull", cmd_pull, "Fetch remote changes into local files."),
        ("push", cmd_push, "Send local changes to HackMD."),
        ("sync", cmd_sync, "Pull then push."),
        ("status", cmd_status, "Preview what pull/push would do (dry run)."),
    ]:
        sp = sub.add_parser(name, help=desc)
        if name != "status":
            sp.add_argument("--dry-run", action="store_true",
                            help="Show what would happen without making changes.")
        sp.set_defaults(func=fn)

    args = parser.parse_args()
    try:
        args.func(args)
    except HackMDError as e:
        sys.exit(f"HackMD API error: {e}")


if __name__ == "__main__":
    main()
