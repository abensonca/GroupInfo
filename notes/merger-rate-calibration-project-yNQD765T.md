# Merger Rate Calibration Project

###### tags: `merger trees`

# Steps

1. Measure new/updated progenitor mass functions from N-body simulations
    1. Available simulations:
        1. MDPL suite (data is on `mies` will need to be unpacked and re-processed; all CDM; multiple simulation resolutions/volumes);
        2. Caterpillar zoom-in suite (data is on `mies`);
        3. Ethan's zoom-ins (data is at Caltech; CDM + non-CDM models; Milky Way and LMC-mass primary halos).
    2. Decisions to be made:
        1. Progenitor halo mass ranges;
        2. Redshifts at which to compute the progenitor mass function;
        3. Do we want to include the Caterpillar suite? (Ethan found some discrepancies between it and his zoom-ins - we should discuss with Ethan).
    3. Process:
        1. Galacticus has tools for computing progenitor mass functions;
        2. This is already set up for MDPL simulations - we'll just need to change to the newer algorithm for rejecting backsplash halos;
        3. For the Zoom-Ins we'll need to create new parameter files to do the analysis, these will need to select the appropriate primary halo (discarding non-primary halos that may not be as well resolved).
2. Set up an MCMC simulation to generate extended Press-Schechter merger trees for each instance:
    1. Match the cosmological parameters, power spectra, resolution, etc. of each simulation;
    2. For Zoom-ins match the primary halo mass;
    3. Use sufficient number of trees such that the resulting uncertainties are smaller than those of the simulations;
    4. Use the `hyperbolicTangent` window function class;
    5. Use the newly-calibrated `bhattacharya2011` halo mass function class;
    6. Use the `PCHPlus` merger tree branching probability class.

## Re-analyzing MDPL simulations

The MDPL simulations are stored on `mies` in `/data001/abenson/Galacticus/Merger_Trees/CosmoSim` in subdirectories (in order of increasing volume/decreasing resolution):
* `VSMDPL`
* `SMDPL`
* `MDPL2`
* `BigMDPL`
* `HugeMDPL`

I've unpacked the data in the `MDPL2` directory - the others can be unpacked as needed. 

Use the `haloMergerRates` branch of Galacticus (as this has some new functionality that's not yet merged into the main branch that we'll want to use). To switch to this branch (and update):
```
git checkout haloMergerRates
git pull
```

Build Galacticus with MPI parallelism (which we'll need for the MCMC simulations):
```
make -j16 GALACTICUS_BUILD_OPTION=MPI Galacticus.exe
```

There is an existing workflow for analyzing the MDPL simulations. The relevant files are:
```
constraints/pipelines/darkMatter/progenitorMassFunctionPreProcess.pl
constraints/pipelines/darkMatter/progenitorMassFunctionIdentifyAlwaysIsolated.xml
```
The first of these manages constructing the analysis for each subvolume of the MDPL simulation (each simulation is broken into `10*10*10` subvolumes), and submitting these jobs to the queue. The second is the template for the analysis.

Currently this uses the `alwaysIsolated` method for rejecting backsplash halos - any halo that was ever a subhalo is considered to be always a subhalo even if it passes outside of its host halo at some later time.

We want to uses the newer `nonFlyby` method instead. To do this:
1. Change instances of `alwaysIsolated` in `progenitorMassFunctionPreProcess.pl` to `nonFlyby` (there are also places where the first letter is capitalized, so change `AlwaysIsolated` to `NonFlyby`);
2. We should run this first only for the MDPL2 simulation, so comment out the other simulations, e.g. `{ label => "VSMDPL"......... }` so that it doesn't try to run those.
3. Copy the file `constraints/pipelines/darkMatter/progenitorMassFunctionIdentifyAlwaysIsolated.xml` to `constraints/pipelines/darkMatter/progenitorMassFunctionIdentifyNonFlyby.xml`, and then edit it:
    1. Use the new `nonFlyby` algorithm; change the
    `<nbodyOperator value="flagAlwaysIsolated"/>`
parameter to:
    `<nbodyOperator value="identifyFlybysMansfieldKravtsov2020" >
     <missingHostsAreFatal value="false"/>
    </nbodyOperator>`
    2. We need some new properties to be read in for use by the `nonFlyby` method. So, in the `readColumns` parameter add `Rvir X Y Z`; and in the `propertyNames` parameter under `deleteProperties` add `radiusVirial position` (to remove these properties after we've used them);
    3. Change how halos are selected, by switching:
    `<nbodyOperator value="selectProperties"   >
      <propertyName   value="alwaysIsolated"/>
      <selectedValues value="1"             />
    </nbodyOperator>`
    to
    `<nbodyOperator value="selectProperties"   >
      <propertyName   value="isFlyby"/>
      <selectedValues value="0"             />
    </nbodyOperator>`
    4. In the `deleteProperties` operator, change `alwaysIsolated` to `isFlyby` (so we delete the new `isFlyby` property after we've used it)
    5. Change any remaining instances of `alwaysIsolated` in the file to `nonFlyby`.

You can also copy this file:
```
/home/abenson/Galacticus/galacticus/galacticusConfig.xml
```
to your own path (same location as `Galacticus.exe`) - it contains configuration information for the queue manager on `mies` that allows the following script to know how to communicate with it.

Once this is all done we can run the analysis using:
```
./constraints/pipelines/darkMatter/progenitorMassFunctionPreProcess.pl --simulationDataPath /data001/abenson/Galacticus/Merger_Trees --pbsJobMaximum 16 --submitSleepDuration 1
```
Before doing so we should check that permissions are set correctly on that path (so that you can write to it) and we may want to start by trying a single subvolume to be sure it's all working correctly. With the above options it will submit at most 16 jobs simultaneously (and then submit more after those are finished). If the queue on `mies` isn't too busy we could increase this - there are a total of 90 nodes on `mies` so increasing to 32 or even 48 would be ok.
