# GroupInfo

Group notes maintained on [HackMD](https://hackmd.io) and mirrored to this
repository for version history and collaborative editing.

## Setup

1. Install the script's one dependency:

   ```bash
   pip install -r requirements.txt
   ```

2. Get a HackMD API token from <https://hackmd.io/settings#api> and put it in a
   local `.env` file (already gitignored):

   ```
   HACKMD_API_TOKEN=your-token-here
   ```

   Alternatively, export it as an environment variable.

3. Initialize sync against your HackMD team. The team path is the slug from
   the team's URL (`https://hackmd.io/team/<team-path>`):

   ```bash
   python hackmd_sync.py init <team-path>
   ```

   This creates `.hackmd-sync.json` (config), `.hackmd-sync-state.json`
   (tracking state), and a `notes/` directory.

## Usage

```bash
python hackmd_sync.py pull      # remote -> local
python hackmd_sync.py push      # local  -> remote
python hackmd_sync.py sync      # pull, then push
python hackmd_sync.py status    # preview without changes (same as `sync --dry-run`)
```

All commands accept `--dry-run` (except `status`, which is always dry).

### How it works

- Each remote note is stored as `notes/<slug>-<shortId>.md`. The slug comes
  from the title (for human readability); the short ID anchors identity, so
  renaming the local file is fine — sync uses the manifest, not the path.
- `.hackmd-sync-state.json` records, per note, the filename, title,
  remote `lastChangedAt`, and a SHA-256 of the content at last sync. Commit
  it so conflict detection is consistent across machines.
- A new local `.md` file in `notes/` (without a matching state entry) is
  treated as a new note on `push` and gets renamed to include its new note ID.

### Conflicts

If both sides have changed since the last sync, `pull` writes the remote
version to `<name>.remote.md` and leaves your local file alone. Resolve the
diff manually, delete the `.remote.md` sidecar, and rerun `sync`.

If you run `push` and the remote has advanced since the last sync, the script
warns and skips that note — run `pull` first.

### Deletions

Deletions are never propagated. If a note disappears on one side, the script
warns; you decide whether to mirror the deletion by hand.

## Files

| Path                         | Purpose                                  | Tracked?     |
| ---------------------------- | ---------------------------------------- | ------------ |
| `hackmd_sync.py`             | The sync script                          | yes          |
| `.hackmd-sync.json`          | Team path + notes dir                    | yes          |
| `.hackmd-sync-state.json`    | Per-note manifest used by sync           | yes          |
| `notes/*.md`                 | The notes themselves                     | yes          |
| `notes/*.remote.md`          | Conflict sidecars (transient)            | no (gitignored) |
| `.env`                       | Local API token                          | no (gitignored) |
