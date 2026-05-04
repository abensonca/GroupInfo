# Dark Matter Subhalo Finder Efficiency

###### tags: `dark matter`

# Background

The primary scientific goal of our group right now is to understand the nature of dark matter. Specifically, we're working to derive constraints on the particle nature of dark matter (e.g. the mass of the dark matter particle) using observations of quadruply-imaged gravitational lenses, and of the Milky Way satellite galaxy population.

Our work is theoretical - we're building models of the physical processes which govern the growth and destruction of dark matter subhalos. These are needed to connect the micro-scale properties of the dark matter particle to the macro-scale astronomical observations.

## Relevant papers

* A nice [review](https://ui.adsabs.harvard.edu/abs/2018PhR...761....1B/abstract) by Buckley & Peter on gravitational probes of dark matter physics - this is a good overview of what we're trying to do.
* Two papers that our group contributed to on constraining the mass of a warm dark matter particle:
    * [Gilman et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020MNRAS.491.6077G/abstract) - using quadruply-imaged gravitational lenses
    * [Nadler et al. (2021)](https://ui.adsabs.harvard.edu/abs/2021arXiv210107810N/abstract) - combining the lensing analysis with constraints from the Milky Way satellite galaxy population
* Successful [JWST proposal](https://ui.adsabs.harvard.edu/abs/2021jwst.prop.2046N/abstract) lead by Anna Nierenberg which will hopefully give us extensive new data from gravitational lenses to improve the constraints on the particle nature of dark matter.

# Goals

## Limitations of N-Body Simulations

We build (semi-)analytical models for the evolution of dark matter subhalos. (There's a nice "astrobites" article [here](https://astrobites.org/2020/07/15/dm-profile-hold-the-subhaloes/) which describes what we mean by halos and subhalos - an useful image from this is shown below.) These inevitably contain some parameters which we need to tune. (The reason for this is that the physics involved is highly non-linear so we can't expect to get all of the factors of order unity correct.)

![](https://i.imgur.com/D5oR9cp.png)

To perform this tuning we calibrate against results from N-body simulations (in which dark matter is represented in a computer as a large number of "particles" and the gravitational forces between them are computed to determine how the particles move around - there's a good, but detailed, [review](https://ui.adsabs.harvard.edu/abs/2011EPJP..126...55D/abstract) by Dehnen & Read), we we take as our "truth" target. But, N-body simulations are not perfect truth. Since they use a (large, but) finite number of particles their results are error prone. 

The output of an N-body simulation is a collection of position and velocity data for all of the particles used in the simulation (the image below shows an example of the results - this is from the [Caterpillar](https://www.caterpillarproject.org/) project). We use a "halo finder" tool to take that data and identify halos and subhalos (collections of particles which are gravitationally bound to each other above some density threshold). There's good evidence that these halo finders sometimes miss subhalos - particularly in the dense inner regions of their host halo.

![](https://i.imgur.com/OUFHUpc.jpg)

This would lead to incorrect measurement of population statistics (such as a the number of subhalos, and their radial distribution). If we calibrate to this incorrect "truth" then our model will give the wrong answers.

## This Project

If we can quantify how often the halo finder misses a subhalo, we can take that into account during our calibration process and avoid mis-calibrating our models.

To make this quantification we can run some numerical experiments. The approach is as follows:

1. Create a realization of a host halo with an embedded subhalo for which we know the true properties of the subhalo.
2. Run the halo finding algorithm on this realization.
3. Record if the subhalo was detected, and, if so, were its properties (mass, position, etc.) correctly recovered?
4. Repeat this process a large number of times (making a different random realization each time) to quantify how often the subhalo is missed, and the distribution of the recovered properties (mass, position, etc.)

The end result of this would be a function (initially a tabulated function, but we could look for some simple analytic fitting function that describes the tabulated data) the quantifies the efficiency of the halo finding algoritm.

There would be at least two phases to this:

1. Use an idealized host halo-subhalo system, in which both host and subhalo are smooth, spherical realizations, and in which the host halo has no other subhalos besides the one we put in there. We'll use our [Galacticus](https://github.com/galacticusorg/galacticus) toolkit to generate these realizations.
2. Use a "real" N-body host (which will have its own internal structure, be non-spherical, have a large number of subhalos already), and inject an idealized subhalo into it. For this we have data from the [Caterpillar](https://www.caterpillarproject.org/) that we can use.

# Tools

* Galacticus
    * This is our halo/subhalo/galaxy simulation code
    * Original [paper](https://ui.adsabs.harvard.edu/abs/2012NewA...17..175B/abstract) describing the model (although this is kind of out of date now)
    * Recent [paper](https://ui.adsabs.harvard.edu/abs/2020MNRAS.498.3902Y/abstract) by Shengqi Yang describing how we calibrate the model to match N-body simulations
    * Source code [repository](https://github.com/galacticusorg/galacticus)
* Rockstar
    * This is the halo finder algorithm that we will use. It's extensively used by other groups, and has been shown to be one of the most effective in various tests.
    * [Paper](https://ui.adsabs.harvard.edu/abs/2013ApJ...762..109B/abstract) describing the algorithm
    * Source code [repository](https://bitbucket.org/gfcstanford/rockstar/src/main/)
* Working with XML files in Python
    * [`eTree`](https://docs.python.org/3/library/xml.etree.elementtree.html) is a good module for this - allows reading/modifying/writing of XML files

# Density profiles

* The original paper on the [NFW density profile](https://arxiv.org/abs/astro-ph/9611107) that we use to describe the host dark matter halo. It has a form that looks like this:
$$
\rho(r) = {\rho_\star \over (r/r_\mathrm{s})(1+(r/r_\mathrm{s})^2}
$$
where $r_\mathrm{s}$ is the "scale radius" that we set when creating particle realizations of halos.
* For the subhalo we use a different density profile from [Penarrubia et al. (2010)](https://ui.adsabs.harvard.edu/abs/2010MNRAS.406.1290P/abstract) - their equation (2) which is more general and can account for the fact that the subhalo density profile is affected by tidal mass loss.

# Running RockStar

RockStar reads the partcile data file created by Galacticus, finds halos in it, and writes out the results. It needs a config file, `rockstar.cfg`, which we already have created.

The general way to run RockStar would be like this:
```
/path/to/rockstar/rockstar -c /path/to/rockstar.cfg /path/to/particleData.hdf5
```
It should only take around 15 seconds with our current number of particles.

It will output two files:
```
halos_0.0.ascii
halos_0.0.bin
```
For now, we're only interesting in the first of those. It's a simple text file that lists the halos that RockStar found, one halo per line.

For example:
```
#id num_p mvir mbound_vir rvir vmax rvmax vrms x y z vx vy vz Jx Jy Jz E Spin PosUncertainty VelUncertainty bulk_vx bulk_vy bulk_vz BulkVelUnc n_core m200b m200c m500c m2500c Xoff Voff spin_bullock b_to_a c_to_a A[x] A[y] A[z] b_to_a(500c) c_to_a(500c) A[x](500c) A[y](500c) A[z](500c) Rs Rs_Klypin T/|U| M_pe_Behroozi M_pe_Diemer Halfmass_Radius idx i_so i_ph num_cp mmetric
#a = 1.000000
#Om = 0.320000; Ol = 0.680000; h = 0.670000
#FOF linking length: 0.280000
#Unbound Threshold: 0.500000; FOF Refinement Threshold: 0.700000
#Particle mass: 6.70000e+06 Msun/h
#Box size: 0.000000 Mpc/h
#Total particles processed: 370300
#Force resolution assumed: 6.7e-06 Mpc/h
#Units: Masses in Msun / h
#Units: Positions in Mpc / h (comoving)
#Units: Velocities in km / s (physical, peculiar)
#Units: Halo Distances, Lengths, and Radii in kpc / h (comoving)
#Units: Angular Momenta in (Msun/h) * (Mpc/h) * km/s (physical)
#Units: Spins are dimensionless
#Units: Total energy in (Msun/h)*(km/s)^2 (physical)
#Note: idx, i_so, and i_ph are internal debugging quantities
#Np is an internal debugging quantity.
#Rockstar Version: 0.99.9-RC3+
0 297 1.990e+09 1.930e+09 25.189131 52.658337 0.363744 37.252544 0.033484 -0.000012 -0.000013 -0.812051 55.502029 1.685311 2.46241e+06 -5.23227e+06 2.35094e+06 -1.19705e+12 0.00970843 0.000053 4.354727 -0.864482 53.424088 0.018814 2.225106 121 1.929600e+09 1.855900e+09 1.701800e+09 1.407000e+09 0.335927 2.509029 0.005003 0.954201 0.846716 -0.136093 0.183193 -0.075335 0.967638 0.884026 -0.118220 0.173391 -0.066827 0.172746 0.158606 0.528491 8.744914e+09 1.145700e+09 3.268005 624 634 -1 297 1.477375
1 333708 2.480e+12 2.480e+12 273.861542 228.673431 71.104103 201.018875 -0.000034 -0.000055 -0.000106 2.128958 -0.291181 -0.581108 -1.53315e+10 -4.44266e+10 -1.72738e+09 -6.38699e+16 0.00028535 0.000098 1.240098 0.272008 0.269493 -0.087962 0.330421 40956 2.479824e+12 2.096303e+12 1.572892e+12 7.818767e+11 0.411512 2.001452 0.000248 0.998676 0.997050 8.952525 4.166212 2.771374 0.996838 0.996525 7.267395 2.351192 2.948471 33.328995 32.940193 0.440744 2.661059e+12 1.519654e+12 104.330429 634 -1 -1 370123 10000000000.000000
```
The lines starting with `#` are header lines that describe the content of the file. What we'll care about most is the `mvir_bound` column (column number 4) which gives the total mass of the halo as found by RockStar. 

Note that the masses are in units of $\mathrm{M}_\odot /h$ where $h=H_0$/100 km/s/Mpc and $H_0$ is the Hubble constant. In our case $h=0.67$. To convert the `mvir_bound` from RockStar to units of $\mathrm{M}_\odot$ (which is what we want) we need to divide by $h$. So, for example, for the first halo RockStar reports a mass of $1.930\times 10^9\mathrm{M}_\odot/h = 2.88 \times 10^9 \mathrm{M}_\odot$.
