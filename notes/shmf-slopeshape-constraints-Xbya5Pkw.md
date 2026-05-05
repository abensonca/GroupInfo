# (S)HMF Slope/Shape Constraints

###### status: `active` · last reviewed: TBD

###### tags: `dark matter` `subhalos` `mass functions`

## Goals

Derive constraints on dark matter physics utilizing measurements of the slope of the (S)HMF from quad-lens flux ratio discrepancy measurements.

- [x] Compute (S)HMF slopes for ETHOS models as a function of $k_\mathrm{peak}$ and $h_1$;
    - [x] Incorporate the model of [Ondaro-Mallea et al. (2021)](https://arxiv.org/abs/2102.08958) for more accurate mass functions
        - [x] Implement their model for the HMF
        - [x] For the SHMF:
            - [x] Test if our merger trees lead to consistent evolution with the [Ondaro-Mallea et al. (2021)](https://arxiv.org/abs/2102.08958) HMF;
            - [ ] If not, can we tune up the parameters of the merger tree algorithm to make them consistent?
- [ ] Derive constraints on these parameters using the lensing data from Daniel Gilman.
    - [ ] Marginalize priors for $\Sigma_{sub}$, $\delta_{los}$, $\beta$ and $c0 = c_8$
        - [x] Approximating beta with slope between 10^7 and 10^9 solar masses accurate enough?
    - [x] Find sub-slope as a function of $k_\mathrm{peak}$ using interpolation.
    - [x] Find slope of concentration-mas relation to find $\beta$ and $c_8$
    - [ ] Experiment with trikde software to make triangle plots
    - [x] Compare results with / without Ondaro Mallea halo mass function. Can we constrain both ETHOS and OM? 

- [x] Check values of hmf/shmf slopes and c-m relation at higher redshifts (ETHOS papers often look at z = 5) 
- [x] See how varying kpeak affects the concetration-mass relation (recommended by Ethan)
- [ ] Prepare presentation on research completed so far.
- [ ] Write appendix to paper on Ondaro-Mallea + evolution of halo mass function and subhalo mass function over time.
- [ ] (Long term goal) Implement more exotic models of dark matter into Galacticus, as well as finding a way to incorporate modified gravity. 
## ETHOS Models

The [ETHOS](http://adsabs.harvard.edu/abs/2016PhRvD..93l3527C) models provide a parameterization of the transfer function, $T(k)$, for certain classes of dark matter particle model.

The transfer function contains dark acoustic oscillations (DAOs) which propagate into the (S)HMF - although they're much less pronounced in the (S)HMF than in $T(k)$. 

Goal is to predict (S)HMF slopes and figure out what constraints can be placed on the $k_\mathrm{peak}$ and $h_1$ parameters of the ETHOS transfer function from measurements of the (S)HMF slope using lensing.

### Deriving Constraints

[Daniel Gilman](mailto:gilman@astro.utoronto.ca) put together some [Python code](https://github.com/dangilman/lenslikelihood) which should be useful to derive constraints on the ETHOS model parameters. The [README](https://github.com/dangilman/lenslikelihood/blob/main/README.rst) has instructions on how to use it.

## Extended dependence of HMF on power-spectrum

The paper by [Ondaro-Mallea et al. (2021)](https://arxiv.org/abs/2102.08958) quantifies how the HMF depends on the effective slope of the power spectrum, $n_\mathrm{eff}$ and effective growth rate of structure, $\alpha_\mathrm{eff}$.

Since $n_\mathrm{eff}$ is wavenumber-dependent this could lead to some change in the slope of the HMF.

Goal is to understand how much effect this has on our predicted slopes of the HMF.

- [x] Implement the $f_1()f_2()f_3()$ mass function from [Ondaro-Mallea et al. (2021)](https://arxiv.org/abs/2102.08958)
    - [x] $f_1()$ can be any halo mass function

### Consequences for SHMF

There's currently no published analysis of how the SHMF might depend on $n_\mathrm{eff}$ or $\alpha_\mathrm{eff}$. We could try one of the following two things to try to understand the effect that it might have:
1. Assume that the effect on the SHMF is the same as on the HMF. In which case we can take the merger rate function (which is used in building the merger trees which lead to the SHMF), and multiply it by the same modifiers as used in the HMF. So, $R(M_2|M_1,t_1) \rightarrow R(M_2|M_1,t_1)f_1()f_2()$.
2. Require that the merger rate function produces consistent evolution of the HMF. Specifically:
    a. We know the evolution of the HMF with redshift under the [Ondaro-Mallea et al. (2021)](https://arxiv.org/abs/2102.08958) model;
    b. Take an ensemble of halos, drawn from the $z=0$ HMF, and build merger trees from them back to $z=1$. Build the HMF of all of the progenitor halos at $z=1$, and compare to the HMF prediction at $z=1$ from [Ondaro-Mallea et al. (2021)](https://arxiv.org/abs/2102.08958);
    c. Adjust the parameters of the merger rate model until the resulting HMF of progenitor halos is consistent with the expectation from [Ondaro-Mallea et al. (2021)](https://arxiv.org/abs/2102.08958).
    
Approach 1 is simple, but there's no real justification that it's the *correct* thing to do.

Approach 2 in principle gives a self-consistent result, but has two problems:
1. It's going to be slow to compute and optimize the merger rate model parameters.
2. There's no guarantee that there's a unique solution here.

A compromise solution might be to use approach 1, but use approach 2 as a test of whether it produces viable answers. This seems like a useful approach. Specifically:

1. Using the Sheth-Tormen mass function check that our merger rate model produces a consistent HMF at $z=1$ starting from a halo ensemble at $z=0$. It should give something close at least, and we can use this as a guide to how close we expect to get.
2. Now use the [Ondaro-Mallea et al. (2021)](https://arxiv.org/abs/2102.08958) HMF at $z=0$ and $z=1$ and apply the modifier functions $f_1()f_2()$ to the merger rates used in building merger trees. Check that the predicted $z=1$ HMF is in good agreement with [Ondaro-Mallea et al. (2021)](https://arxiv.org/abs/2102.08958).

In step 1 above, we know that it should work reasonably well as this was previously demonstrated by [Parkinson, Cole & Helly (2008](https://ui.adsabs.harvard.edu/abs/2008MNRAS.383..557P/abstract); their Figure 4 also shown below).

![](https://i.imgur.com/VZhtzUq.png)

## Schematic of Comparing HMF Ensemble Evolution

![](https://i.imgur.com/esV5aJi.png)


## Notes on parameter settings

### HMF vs. SHMF

For HMF calculations Galacticus can output the HMF directly. To request this use the [`haloMassFunction`](https://github.com/galacticusorg/galacticus/releases/download/masterRelease/Galacticus_Physics.pdf#physics.taskHaloMassFunction) task using parameter settings like this:

```
<taskMethod value="haloMassFunction"/>
```

For SHMF calculations we need to generate complete merger trees, and evolve them to the relevant output time. This is done using the [`evolveForests`](https://github.com/galacticusorg/galacticus/releases/download/masterRelease/Galacticus_Physics.pdf#physics.taskEvolveForests) task:

```
<taskMethod value="evolveForests"/>
```

### Multiple tasks

To combine multiple tasks (e.g. HMF and SHMF calculations) in a single model, wrap the parameters inside a `multi` task:
```
<taskMethod value="multi">
 <taskMethod value="haloMassFunction"/>
 <taskMethod value="evolveForests"/>
</taskMethod>
```

### Controlling output redshifts

Using the `list` `outputTimesMethod` you can add as many output redshifts as you want as a space separated list. For example:
```
<outputTimesMethod value="list">
 <redshifts value="0.0 1.0 2.0"/>
</outputTimesMethod>
```
The order of the redshifts in this list doesn't matter. You'll get an `OutputN` group for each requested redshift, with `N` running from 1 (for the earliest output) to $N$ where $N$ is the number of outputs in your list. 

The `OutputN` groups in the HDF5 file have attributes `outputTime` giving the time of the output (in Gyr) and `outputExpansionFactor` which gives the expansion factor, $a$, at the output. You can get the redshift from this using $1+z=a^{-1}$.

### Distributions of halo masses

When building merger trees we can control how the root masses of the trees are sampled from the halo mass function.

Using
```
<mergerTreeBuildMassDistributionMethod value="haloMassFunction"/>
```
will sample root masses at a rate proportional to the HMF (so you'll get mostly low mass halos, and many fewer high mass halos).

An alternative is to use:
```
<mergerTreeBuildMassDistributionMethod value="powerLaw">
 <exponent value="1.0"/>
</mergerTreeBuildMassDistributionMethod>
```
which will sample root masses from a power-law in halo mass. A choice of `exponent`$=1$ in the above leads to a more uniform sampling of root masses (so, you'll get more comparable numbers of low and high mass halos).