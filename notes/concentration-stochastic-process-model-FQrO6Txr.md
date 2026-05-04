# Concentration Stochastic Process Model

###### tags: `dark matter` `concentration`

## Goal

The goal here is to create a model for the scatter in halo concentration which is similar in approach to the [stochastic process model for spin](https://hackmd.io/@galacticus/HkI3EtHK_), and which captures the mean evolution of the $c(M,z)$ relation and also produces the correct scatter in concentration at fixed halo mass. It should be applicable even to halos for which the formation history is not well resolved.

## Model

### General Idea

Since [Johnson, Benson, & Grin (2021)](http://adsabs.harvard.edu/abs/2021ApJ...908...33J) show that concentration evolution can be modeled as a random walk process driven by merging of dark matter halos, I want to consider a similar approach.

Given that we have no knowledge of the mergers for halos of sufficiently low mass (because of the resolution limit in a merger tree) we can use a fully stochastic model instead - i.e. something similar to a Wiener process (but, as we will see below, with time-dependent variance).

### Model Description

The energy of each halo is assumed to evolve according to its mass evolution (as determined from the merger tree), plus some calibrated model for the mean $c(M,z)$ relation. This ensures that the mean $c(M,z)$ is always correctly reproduced. We then model a perturbation to this energy as a Wiener processes with time-dependent variance. Specifically, the energy perturbation obeys:

$$
\Delta E_\mathrm{i}(t_2) = \Delta E_\mathrm{i}(t_1) + \left[ \sigma^2 \left\{ E_\mathrm{v}^2(t_2) - E_\mathrm{v}^2(t_1) \right\} \right]^{1/2} N(0,1)
$$

where $E_\mathrm{v}(t) = \mathrm{G} M^2_\mathrm{v}(t) / R_\mathrm{v}(t)$ is the characteristic virial energy, $M_\mathrm{v}(t)$, and $R_\mathrm{v}(t)$ are the virial mass, and radius respectively, $\sigma^2$ represents the variance in energy per unit increase in $E_\mathrm{v}^2$, and $N(0,1)$ is a random variable distributed as a standard normal.

The energy of the halo is then computed as the energy assuming the mean $c(M,z)$ relation, plus the perturbation. Given this perturbed energy, a new concentration is computed consistent with this perturbed energy. The result is a random walk in energy and concentration along each branch of the merger tree.

This model captures the idea that the increase in energy from a merging event should be of order $\mathrm{G} \Delta M M_\mathrm{v} / R_\mathrm{v}(t)$ (since merging halos will have potential and kinetic energies both determined by the potential of the primary halo at the virial radius). Additionally, because this is a Wiener process the resulting distribution of $E_\mathrm{i}(t)$ at any given time is independent of the number of steps used to get from $t=0$ to that time. (That is, the results are independent of how finely we sample the mass accretion history of each halo.)

## Results

I find that a value of $\sigma^2 = 0.006$ works reasonably well to produce the correct scatter in concentration at fixed halo mass. The following plots show results from this model compared to measurements from the various MultiDark cosmological simulations on mass scales corresponding to dwarf galaxies, Milky Ways, groups, and clusters respectively. (The Galacticus results include models for N-body uncertainties in halo mass and concentration measurements.)

![](https://i.imgur.com/TtbVM4f.png)

![](https://i.imgur.com/wQsazW2.png)


![](https://i.imgur.com/7RnwNOC.png)


![](https://i.imgur.com/uuonxBv.png)

The agreement in the scatter is quite good, except for at the lowest mass scales where this model overestimates the scatter.

## Future Improvements

It might be possible to improve this model further by utilizing a better estimate for the variance. The scaling with $E_\mathrm{v}^2$ neglects the fact that the internal energy of merging secondary halos will depend on their concentrations. Alternatively, some empirical mass- and/or redshift-dependence, $\sigma^2(M,z)$ could be included to give a better match to simulations.