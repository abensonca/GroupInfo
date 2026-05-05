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

## Galacticus development

- [Removing "Method" Suffix from Parameter Files](notes/removing-method-suffix-from-parameter-files-zQidUF95.md)
  — convention/migration note for parameter naming.

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

### Halo properties (stochastic-process models)

- [Concentration Stochastic Process Model](notes/concentration-stochastic-process-model-FQrO6Txr.md)
- [Spin Stochastic Process Model](notes/spin-stochastic-process-model-hIEK1DxT.md)
- [Halo Triaxiality Random Walk Model](notes/halo-triaxiality-random-walk-model-XLf5QYjR.md)

### Subhalos & substructure

- [Subhalo Tidal Tracks Model](notes/subhalo-tidal-tracks-model-GAVyCqaK.md)
- [Subhalo Orbits Model Papers](notes/subhalo-orbits-model-papers-jrQmIsfZ.md)
- [Subhalo Population Emulator](notes/subhalo-population-emulator-M1hUcBkA.md)
- [Subhalo Population Emulation](notes/subhalo-population-emulation-iqKXPdsC.md)
  — overlaps with the entry above; worth merging or cross-linking.
- [Dark Matter Subhalo Finder Efficiency](notes/dark-matter-subhalo-finder-efficiency-C0nHtSOl.md)
- [(S)HMF Slope/Shape Constraints](notes/shmf-slopeshape-constraints-Xbya5Pkw.md)

### Stellar streams

- [Overview of Streams-Probe Research Program](notes/overview-of-streams-probe-research-program-O2oX4Lp7.md)
  — full internal overview.
- [Overview of Streams-Probe Research Program (public)](notes/overview-of-streams-probe-research-program-public-wkWzseZZ.md)
  — public-facing version of the above.
- [Stellar Streams as Substructure Probe](notes/stellar-streams-as-substructure-probe-rW6oVexC.md)

### Alternative dark matter physics

- [Fuzzy Dark Matter](notes/fuzzy-dark-matter-i9H5jJyl.md)
- [Fuzzy Dark Matter Granule Structure](notes/fuzzy-dark-matter-granule-structure-q0yqg0TI.md)
- [SIDM Evolution Notes](notes/sidm-evolution-notes-FTfdM94s.md)
- [SIDM Halo Core Collapse](notes/sidm-halo-core-collapse-tltE2gjR.md)
- [Heating of DM Profile by SNe Feedback](notes/heating-of-dm-profile-by-sne-feedback-61zhqlkm.md)

### Baryonic physics & emission lines

- [Baryonic Physics Constraints Plan](notes/baryonic-physics-constraints-plan-eygJtc1Q.md)
- [Emission Line Modeling](notes/emission-line-modeling-mfh3hN9T.md)
- [Emission Lines Model Plan](notes/emission-lines-model-plan-LCcl8Yok.md)
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
