# Notes Index

A curated guide to the contents of [`notes/`](notes/). Notes are the canonical
copies of HackMD pages used by the group — they cover onboarding, computing
how-tos, group policies, and ongoing research projects.

If you're new to the group, start with **Onboarding & policies** and
**Computing**.

> Descriptions below are short summaries derived from each note's title and
> opening section. If something is wrong or out of date, edit the note and
> update this index.

## Onboarding & policies

- [Group Policies](notes/group-policies-H8cEyZ8C.md) — Galacticus contribution
  expectations, credit, and the Carnegie group co-authorship policy.
- [Galacticus Project Organization](notes/galacticus-project-organization-a81PXyXm.md)
  — recommended `git`/GitHub workflow for projects that use Galacticus.
- [Useful Resources](notes/useful-resources-Xbd2iEcK.md) — external links worth
  bookmarking (currently a stub — please add to it).

## Computing

### Environment & tooling

- [Computing Resources](notes/computing-resources-ukWn23Ja.md) — Python/Anaconda
  setup, GitHub SSH keys, VSCode, `tmux`, `git diff` helpers, software
  engineering links.

### Building Galacticus

- [Compiling Galacticus on Caltech HPC](notes/compiling-galacticus-on-caltech-hpc-jol6HnNq.md)
- [Compiling Galacticus on OBS HPC](notes/compiling-galacticus-on-obs-hpc-OOMa0kUW.md)
- [Compiling Galacticus on NERSC](notes/compiling-galacticus-on-nersc-KMvLs5JT.md)

### Running jobs

- [Submitting Jobs on Caltech HPC](notes/submitting-jobs-on-caltech-hpc-o4QFFb8Q.md)
- [Submitting Jobs on OBS HPC](notes/submitting-jobs-on-obs-hpc-aCJxUqdn.md)
- [Submitting Jobs on NERSC](notes/submitting-jobs-on-nersc.md)

## Research projects

### Merger trees, mass functions, excursion sets

- [Mass Functions, Excursion Sets, and Merger Trees](notes/mass-functions-excursion-sets-and-merger-trees-cWwQQlHo.md)
  — long-form reference write-up.
- [Universal Halo Mass Function](notes/universal-halo-mass-function-oo0r3bsY.md)
- [Sampling from the Halo Progenitor Mass Function](notes/sampling-from-the-halo-progenitor-mass-function-Ep4bdN6Q.md)
- [Constrained Excursion Sets](notes/constrained-excursion-sets-cfeDeLqT.md)
- [Constrained Merger Trees](notes/constrained-merger-trees-8uulMqhp.md)
- [Conditioning Merger Trees](notes/conditioning-merger-trees-xGXlmmdu.md)
- [Improving Monte Carlo Merger Trees to Better Match N-body Statistics](notes/improving-monte-carlo-mergers-trees-to-better-match-n-body-s-ng5AtFbe.md)
- [Merger Rate Calibration Project](notes/merger-rate-calibration-project-yNQD765T.md)

### Stellar streams

- [Overview of Streams-Probe Research Program](notes/overview-of-streams-probe-research-program-O2oX4Lp7.md)
  — full internal overview.

### Alternative dark matter physics

- [Fuzzy Dark Matter](notes/fuzzy-dark-matter-i9H5jJyl.md)
- [Fuzzy Dark Matter Granule Structure](notes/fuzzy-dark-matter-granule-structure-q0yqg0TI.md)

### Emission lines

- [Emission Line Modeling](notes/emission-line-modeling-mfh3hN9T.md)
- [Emission Lines for OpenUniverse Work](notes/emission-lines-for-cosmosims-work-vSosPAND.md)

## For editors

### Status header

Each note carries a header just below its title of the form:

    ###### status: `active` · last reviewed: YYYY-MM-DD

Status values:

- `active` — currently being worked on
- `reference` — long-form / how-to / policy / overview; expected to stay accurate
- `dormant` — paused but not abandoned
- `archived` — historical, kept for context only

When you next read or edit a note, please also update its `last reviewed`
date so others can see at a glance how stale the content is. Initial values
were set in bulk and many are placeholders (`TBD`).

### Tag vocabulary

Tags use HackMD's `###### tags:` convention. To keep search useful, please
draw from the controlled vocabulary below (add new tags sparingly):

- **Categories:** `policies`, `computing`, `build`, `galacticus development`
- **Topics:** `dark matter`, `merger trees`, `mass functions`, `excursion sets`,
  `subhalos`, `concentration`, `spin`, `triaxiality`, `stellar streams`,
  `fuzzy dark matter`, `SIDM`, `baryonic physics`, `emission lines`,
  `parameters`, `constraints`
- **Sites:** `Caltech HPC`, `OBS HPC`, `NERSC`
- **Tools:** `git`, `GitHub`
