# Mass Functions, Excursion Sets, and Merger Trees

###### status: `reference` · last reviewed: 2026-05-05

###### tags: `dark matter` `mass functions` `merger trees` `excursion sets`

# The Excursion Set Problem

## Motivation 

The "excursion set problem" arises in the context of determining the fraction of mass in the universe that has collapsed into objects ("halos") of given mass.

From simple [spherical collapse models](https://ui.adsabs.harvard.edu/abs/2005A%2526A...443..819P) and [linear perturbation theory](https://archive.org/details/cosmologicalphys0000peac), we know that a spherical patch of the universe enclosing a mass, $M$, will collapse to form a halo when the linear theory overdensity, $\delta(t)$, of that region reaches some critical threshold, $\delta_\mathrm{c}(t)$. A nice review is given by [Zentner (2007)](https://ui.adsabs.harvard.edu/abs/2007IJMPD..16..763Z).

Typically, we describe the linear theory overdensity of the universe as a Gaussian random field, which is then fully characterized by its power spectrum, $P(k)$.

Let $S(M)$ be the variance in the linear theory overdensity when the density field is smoothed on a scale corresponding to mass $M$. Specifically,
$$
S(M) = \int_0^\infty \frac{\mathrm{d}k}{k} \frac{k^3 P(k)}{2 \pi^2} W^2(k|M),
$$
where $W(k|M)$ is a window function that depends on the halo mass.

On large scales $S(M) \rightarrow 0$ while (for a CDM power spectrum), on small scales $S(M) \rightarrow \infty$ - so perturbations become arbitrarily large and must exceed $\delta_\mathrm{c}(t)$ on some sufficiently small scale. Therefore, any patch in the universe will be collapsed into a halo on some finite mass scale.

To determine that scale we can consider gradually reducing the smoothing scale, $M$, starting from $M=\infty$ (for which $S=0$ so we can be sure that the patch is not collapsed on this scale). As we decrease $M$, $S(M)$ increases, following a random walk. If we find the largest value of $M$ (corresponding to the smallest value of $S(M)$) for which $\delta(M) > \delta_\mathrm{c}$ (I've dropped the explicit time dependence in $\delta_\mathrm{c}$) then this must be the mass of the halo into which the patch has collapsed.

This random walk traced out by $\delta(M)$ as a function of $M$ (or, equivalently, as a function of $S$) is called an "excursion". The collection of all possible such excursions is called the "excursion set".

Determining the distribution of halo masses therefore reduces to finding the distribution, $f(S)$ of values of $S$ at which excursions first cross the collapse threshold, $\delta_\mathrm{c}$. In the mathematics of excursion sets this is known as a barrier first crossing problem.

## Simplifying Assumptions

We have not yet specified precisely how the density field is smoothed when computing $S(M)$. If we use a window function that is sharp in $k$-space, then the change in $\delta(M)$ as we decrease $M$ is uncorrelated with $\delta(M)$ on all larger mass scales. Then, each "excursion" is a draw from a [Wiener process](https://en.wikipedia.org/wiki/Wiener_process) (i.e. the steps are uncorrelated), often referred to as a Brownian random walk, which greatly simplifies the math.

## Solving the Excursion Set Problem in Galacticus

Galacticus contains a class, [`excursionSetFirstCrossing`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetFirstCrossing), which solves the excursion set problem. As with any class in Galacticus there can be (and are in this case) multiple different implementations. These will be described below.

Every instance of the [`excursionSetFirstCrossing`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetFirstCrossing) class will need to know what collapse threshold, $\delta_\mathrm{c}$, to use. This is specified via the [`excursionSetBarrier`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetBarrier) physics. We'll come back to that class later.

### Analytic Solutions

In the case of CDM, the collapse threshold, $\delta_\mathrm{c}$, is independent of mass, $M$. In this case there is an analytic solution for the barrier first crossing problem ([Chandrasekhar 1943](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.15.1); [Lacey & Cole 1993](https://ui.adsabs.harvard.edu/abs/1993MNRAS.262..627L)):
$$
f(S) = \frac{1}{\sqrt{2\pi}} \frac{\delta_\mathrm{c}}{S^{3/2}} \exp\left( - \frac{\delta_\mathrm{c}}{2 S} \right).
$$
This solution actually holds even for a collapse threshold that is linearly-dependent on $S$.

This solution is implemented by the [`linearBarrier`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetBarrierLinearBarrier) instance of the [`excursionSetFirstCrossing`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetFirstCrossing) class in Galacticus.

### Numerical Solutions

For arbitrary variance-dependence (corresponding to arbitrary mass-dependence) in the collapse threshold, analytic solutions are not available. Instead, we have to solve the excursion set problem numerically. 

Galacticus has several numerical excursion set problem solvers: 
* [`zhangHui`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetFirstCrossingZhangHui): [Zhang & Hui (2006)](http://adsabs.harvard.edu/abs/2006ApJ...641..641Z);
* [`zhangHuiHighOrder`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetFirstCrossingZhangHuiHighOrder]): [Zhang & Hui (2006)](http://adsabs.harvard.edu/abs/2006ApJ...641..641Z) - a higher-order implementation of the original [Zhang & Hui (2006)](http://adsabs.harvard.edu/abs/2006ApJ...641..641Z) algorithm;
* [`farahi`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetFirstCrossingFarahi): [Benson et al. (2013)](http://adsabs.harvard.edu/abs/2013MNRAS.428.1774B) - an improved algorithm that achieves better precision that the [Zhang & Hui (2006)](http://adsabs.harvard.edu/abs/2006ApJ...641..641Z) algorithm;
* [`farahiMidpoint`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetFirstCrossingFarahiMidpoint): [Du et al. (2017)](https://ui.adsabs.harvard.edu/abs/2017MNRAS.465..941D/abstract) - an improved version of the [Benson et al. (2013)](http://adsabs.harvard.edu/abs/2013MNRAS.428.1774B) algorithm that uses midpoint integration to achieve more robust results.

In general, the [`farahiMidpoint`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetFirstCrossingFarahiMidpoint) instance is the most robust and reliable of these solvers. 

Note that numerically solving the excursion set problem is usually slow. Galacticus can store the solutions to file for re-use in future runs where possible.

### Collapse Thresholds

Every instance of the [`excursionSetFirstCrossing`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetFirstCrossing) class  needs to know what collapse barrier to use. Collapse barriers are implemented by the [`excursionSetBarrier`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetBarrier) class.

Typically, the barrier to use will be $\delta_\mathrm{c}$, which is provided by the [`criticalOverdensity`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetBarrierCriticalOverdensity) instance of this class. 

There are also instances for linear and quadratic barriers, but those are intended mainly for testing, so are typically not used.

Finally, there are some [`excursionSetBarrier`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetBarrier) instances which impose some remapping on another barrier - these will be discussed below.

# Halo Mass Functions

Within Galacticus, halo mass functions are implemented by the [`haloMassFunction`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.haloMassFunction) physics.

The halo mass function is directly related to the solution to the excursion set problem. Specifically, $f(S) \mathrm{d}S$ is the fraction of mass in the universe in halos corresponding to variance $S$ to $S + \mathrm{d}S$. Therefore, the number of halos in the mass range $M$ to $M + \mathrm{d}M$ is just:
$$
n(M) = \frac{\bar{\rho}}{M} f(S) \left| \frac{\mathrm{d}S}{\mathrm{d}M} \right|,
$$
where $\bar{\rho}$ is the mean matter density of the universe.

## Press-Schechter (+Excursion Sets)

The [Press-Schechter](http://adsabs.harvard.edu/abs/1974ApJ...187..425P) mass function simply utilizes the above expression to estimate the halo mass function. It is often written as:
$$
n(M) = 2 \frac{\bar{\rho}}{M^2} |\alpha| S(M) f(S),
$$
where $\alpha = \mathrm{d}S/\mathrm{d}M$.

The [Press-Schechter](http://adsabs.harvard.edu/abs/1974ApJ...187..425P) mass function is implemented by the [`pressSchechter`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.haloMassFunctionPressSchechter) instance of the [`haloMassFunction`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.haloMassFunction) physics. As the [`pressSchechter`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.haloMassFunctionPressSchechter) instance directly uses the excursion set solution it can be applied to any instance of the [`excursionSetFirstCrossing`](ttps://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetFirstCrossing) physics.

## Fitting Functions

While the [Press-Schechter](http://adsabs.harvard.edu/abs/1974ApJ...187..425P) mass function is well-motivated from excursion set theory, it doesn't actually match the results of N-body simulations all that well. There are multiple reasons for this, including the fact that using a sharp-$k$ filter isn't really justified, real halos are not spherical, so using the constant collapse density predicted by spherical collapse theory is not realistic (and maybe an ellipsoidal collapse model should be used instead), etc.

Consequently, many fitting functions have been proposed which better match the results of N-body simulations. These are often (but not always) parameterized in the form:
$$
n(M) = 2 \frac{\bar{\rho}}{M^2} |\alpha| f(\nu),
$$
where $\nu = \delta_\mathrm{c}/\sqrt{S}$, and $f(\nu)$ is some function of $\nu$. This form is motivated by the fact that in the excursion set problem the solution depends on $S$ only through this parameter, $\nu$, known as the "peak height".

It is important to know that these empirical fitting functions are calibrated to CDM. Or, to put it another way, they definitely should not be applied in cases where the collapse barrier differs from CDM, and may not be as accurate even for models that have a different power spectrum than CDM.

These fitting functions *do not* utilize the solution to the excursion set problem and so do not require (nor will they use even if given) an instance of the [`excursionSetFirstCrossing`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetFirstCrossing) physics. As such, models which change the nature of the solution to the excursion set problem should not use one of these fitting functions.

One of the most commonly-used fitting functions is that of [Sheth & Tormen (2001)](http://adsabs.harvard.edu/abs/2002MNRAS.329...61S), which was motivated by ellipsoidal collapse models. It is implemented by the [`shethTormen`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.haloMassFunctionShethTormen) instance of the [`haloMassFunction`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.haloMassFunction) physics.

# Merger Tree Building

Halos grow hierarchically, that is, smaller halos merge to form larger halos. The excursion set problem can inform about this also. Since the random walks that make up the excursions in the excursion set are invariant with respect to their starting point, we can simply offset the solution to determine the distribution of masses of progenitor halos of a halo of variance $S(M_0)$ which collapse at a critical overdensity threshold of $\delta_\mathrm{c}$, at some earlier time, corresponding to a critical overdensity threshold of $\delta^\prime_\mathrm{c}$:
$$
f(S^\prime,\delta^\prime_\mathrm{c}|S,\delta_\mathrm{c}) = \frac{1}{\sqrt{2\pi}} \frac{\delta_\mathrm{c}-\delta^\prime_\mathrm{c}}{(S-S^\prime)^{3/2}} \exp\left( - \frac{\delta_\mathrm{c}-\delta^\prime_\mathrm{c}}{2 (S-S^\prime)} \right).
$$
Over a small "time" interval, $\Delta w = \delta_\mathrm{c}-\delta^\prime_\mathrm{c}$, this then gives us the distribution of mass in progenitor halos of mass $M_1 < M_0$. Multiplying this function by $M_0/M_1$ and dividing by $\Delta w$ then gives the merger rate of halos into a parent halo. This rate (known as the "branching rate") can be used to construct merger histories, known as merger trees, of halos.

In Galacticus, merger tree building is implemented by the `mergerTreeBuilder` physics.

## Cole et al. (2000) Algorithm

The [Cole et al. (2000)](http://adsabs.harvard.edu/abs/2000MNRAS.319..168C) tree-building algorithm, implemented by the [`cole2000`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.mergerTreeBuilderCole2000) instance of the [`mergerTreeBuilder`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.mergerTreeBuilder) class, begins with a halo characterized by variance $S(M)$ and time $w=\delta_\mathrm{c}(t)$. It then proceeds to take a step *backward* in time. It first determines the net probability of the halo undergoing a branching event during the timestep by integrating the branching rate over all possible progenitor halo masses (down to some mass resolution), and randomly determining if a branching event occurs. If it does, it samples a mass from the branching rate distribution function, otherwise it simply reduces the mass by a small amount to account for sub-resolution accretion.

Exactly how to sample from the branching rate distribution is a complicated question. [Cole et al. (2000)](http://adsabs.harvard.edu/abs/2000MNRAS.319..168C) draws masses from the lower half ($M_1 < M_0/2$) of the distribution, and assumes a binary split, such that a second progenitor of mass $M_2 = M_0 - M_1$ is also created. This does not precisely match the expectations from the excursion set solution however, since that distribution function is not symmetric around $M_0/2$ - see [Zhang, Fakhouri & Ma (2008)](https://ui.adsabs.harvard.edu/abs/2008MNRAS.389.1521Z) and [Jiang & van den Bosch (2014)](http://adsabs.harvard.edu/abs/2014MNRAS.440..193J) for discussion of this point.

## Branching Rates

In Galacticus, branching rates are provided by the [`mergerTreeBranchingProbability`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.mergerTreeBranchingProbability) physics. The [`cole2000`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.mergerTreeBranchingProbabilityCole2000) merger tree builder makes use of the [`mergerTreeBranchingProbability`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.mergerTreeBranchingProbability) class to compute rates of halo branching and mass accretion.

Currently, two [`mergerTreeBranchingProbability`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.mergerTreeBranchingProbability) implementations are available:
* [`parkinsonColeHelly`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.mergerTreeBranchingProbabilityParkinsonColeHelly) - Implements the model of [Parkinson, Cole & Helly (2008)](http://adsabs.harvard.edu/abs/2008MNRAS.383..557P) which applies a modifier function $G(\sigma_1,\sigma_2,\delta_2) = G_0 (\sigma_1/\sigma_2)^{\gamma_1} (\delta_2/\sigma_2)^{\gamma_2}$ (which was calibrated to produce trees in good agreement with the statistical properties of trees from N-body simulations) to the branching rate distribution predicted by extended Press-Schechter theory for a constant collapse threshold. As such, it **does not** make use of solutions from the [`excursionSetFirstCrossing`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetFirstCrossing) physics.
* [`gnrlzdPrssSchchtr`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.mergerTreeBranchingProbabilityGnrlzdPrssSchchtr) - Constructs branching rates using a solution to the excursion set first crossing problem provided by an [`excursionSetFirstCrossing`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetFirstCrossing) class, multiplied by a modifier function, provided by the [`mergerTreeBranchingProbabilityModifier`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.mergerTreeBranchingProbabilityModifier) physics. As such, this implementation is appropriate for cases where the collapse threshold, $\delta_\mathrm{c}$, is non-constant.

### Branching Probability Modifier Functions

Since extended Press-Schechter solutions do not perfectly match results from N-body simulations it is useful to be able to apply multiplicative modifiers to these solutions to bring branching rates into better agreement with those from N-body measurements.

In Galacticus, modifiers to the branching rate are implemented by the [`mergerTreeBranchingProbabilityModifier`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.mergerTreeBranchingProbabilityModifier)class, which has the following implementations:
* [`identity`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.mergerTreeBranchingProbabilityModifierIdentity) - here the modifier function is always 1, so the branching rates from the excursion set solution are used unchanged;
* [`parkinson2008`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.mergerTreeBranchingProbabilityModifierParkinson2008) - implements the modifier function from [Parkinson, Cole & Helly (2008)](http://adsabs.harvard.edu/abs/2008MNRAS.383..557P) which was calibrated to match N-body results.

## Differences between Halo Mass Function and Merger Rate Approaches

As noted above, solutions to the excursion set problem for a constant barrier do not exactly match the results of N-body simulations. As a result, empirical approaches have been adopted to give better agreement. The approach taken has historically differed for halo mass functions and branching rates.

For branching rates, the approach used is to take the solution to the excursion set first crossing problem and multiply by some empirical modifier to achieve a better match to N-body simulations.

If we now consider a model with a non-constant collapse threshold, then in the case of branching rates we can take the new solution to the excursion set first crossing problem, assume that the modifier function is unchanged (not necessarily a justified assumption) and compute new branching rates.

For halo mass functions the approach taken to achieve a good match to N-body results has typically been different. Instead of taking the excursion set solution and multiplying by a modifier function, instead new functional forms have been fit to the N-body data. (Although in at least some cases these could be cleanly written as the excursion set solution multiplied by a modifier function.)

As a result of this, only the [`pressSchechter`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.haloMassFunctionPressSchechter) halo mass function class utilizes the results of the excursion set first crossing problem via the [`excursionSetFirstCrossing`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetFirstCrossing) physics. If a non-constant collapse barrier is to be used then [`pressSchechter`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.haloMassFunctionPressSchechter) is the *only* halo mass function class that will respond to the change in the collapse threshold. But, the Press-Schechter mass function using the excursion set first crossing solution for a constant barrier does not match N-body results well. Therefore, the recommendation is, even for the standard CDM case which nominally has a constant collpase threshold, to used a modified collapse threshold which makes the Press-Schechter mass function more closely match N-body results. This is detailed in the following section.

# Which Options to Use

If you are running a model which has a collapse threshold $\delta_\mathrm{c}$ that is constant (i.e. independent of halo mass), then there is no need to use any of the excursion set solving machinery. This is true even if the power spectrum you are considering is not a CDM power spectrum (e.g. if it has a small-scale cut off). Recommended parameters (see this [parameter file](https://github.com/galacticusorg/darkMatterModels/blob/main/darkMatterOnly_CDM.xml)) are then:

```
  <!-- Dark matter halo mass function -->
  <haloMassFunction      value="shethTormen">
    <!-- Use the Sheth-Tormen mass function, with parameters calibrated to non-splashback halos from the MDPL simulation suite. -->
    <!-- See Benson (2017; MNRAS; 467; 3454; https://ui.adsabs.harvard.edu/abs/2017MNRAS.467.3454B),                            -->
    <!-- and https://github.com/galacticusorg/galacticus/wiki/Constraints:-Dark-matter-halo-mass-function                       -->
    <a             value="0.758359488694975"/>
    <normalization value="0.289897200615808"/>
    <p             value="0.331118219117848"/>
  </haloMassFunction>

  <mergerTreeBranchingProbability value="PCHPlus">
    <!-- Merger tree branching rates are computed using the PCH+ algorithm, with parameters constrained to match progenitor -->
    <!-- mass functions in the MDPL simulation suite.                                                                       -->
    <!-- See: https://github.com/galacticusorg/galacticus/wiki/Constraints:-Dark-matter-progenitor-halo-mass-functions      -->
    <!-- CDM assumptions are used here to speed up tree construction.                                                       -->
    <G0                 value="+1.1425468378985500"/>
    <gamma1             value="-0.3273597030267590"/>
    <gamma2             value="+0.0587448775510245"/>
    <gamma3             value="+0.6456170934757410"/>
    <accuracyFirstOrder value="+0.1000000000000000"/>
    <cdmAssumptions     value="true"               />
  </mergerTreeBranchingProbability>

```

If the model you are running has a non-constant collapse threshold then you may want to use the full excursion set machinery to more accurately compute halo mass functions and branching rates for your model. Recommended parameters (see this [parameter file](https://github.com/galacticusorg/darkMatterModels/blob/main/darkMatterOnly_WDM.xml)) are then:

```
    <haloMassFunction value="pressSchechter">
      <!-- Use the Press-Schechter mass function as this directly utilizes the first crossing rate distribution. -->
    </haloMassFunction>
    <excursionSetBarrier value="remapScale">
      <!-- Remapping of the barrier is applied for two reasons: -->
      <!-- 1: The use of a sharp-k window function changes sigma(M) for large M, so we rescale the barrier here to compensate for
           that which ensures that we get back to the original mass function in this limit (Benson et al.; 2013; MNRAS; 427; 1774;
           section 2.2; https://ui.adsabs.harvard.edu/abs/2013MNRAS.428.1774B). -->
      <factor  value="1.1965"  />
      <applyTo value="nonRates"/>
      <excursionSetBarrier value="remapShethMoTormen">
	<!-- We apply the Sheth-Mo-Tormen remapping to the barrier such that the first crossing distribution for an otherwise
	     constant barrier should approximate the actual mass function measured in simulations (see Sheth, Mo, & Tormen; 2001;
	     MNRAS; 323; 1; http://adsabs.harvard.edu/abs/2001MNRAS.323....1S; and Benson et al.; 2013; MNRAS; 427; 1774; equation
	     11; https://ui.adsabs.harvard.edu/abs/2013MNRAS.428.1774B). -->
	<a value="0.707"/>
	<b value="0.500"/>
	<c value="0.600"/>
	<applyTo             value="nonRates"           />
	<excursionSetBarrier value="criticalOverdensity" >
	  <!-- The unscaled barrier is just the usual critical overdensity for collapse. -->
	</excursionSetBarrier>
      </excursionSetBarrier>
    </excursionSetBarrier>
    <excursionSetFirstCrossing value="farahiMidpoint">
      <!-- Utilize the more stable midpoint variant of the Farahi excursion set solver described by Du et al. (2017; MNRAS; 465;
           941; http://adsabs.harvard.edu/abs/2017MNRAS.465..941D). -->
      <timeStepFractional value="0.01"/>
      <fileName           value="auto"/>
    </excursionSetFirstCrossing>
    <mergerTreeBranchingProbability value="gnrlzdPrssSchchtr">
      <!-- Use the generalized Press-Schechter branching algorithm which makes no assumptions about the form of the first crossing
           distribution, instead using the result computed by the excursion set solver. A minimum mass is set - this is the mass
           to which subresolution accretion fractions will be integrated. -->
      <massMinimum value="1.0e5"/>
    </mergerTreeBranchingProbability>
    <mergerTreeBranchingProbabilityModifier value="PCHPlus">
      <!-- Merger tree branching rates are computed using the PCH+ algorithm, with parameters constrained to match progenitor -->
      <!-- mass functions in the MDPL simulation suite.                                                                       -->
      <!-- See: https://github.com/galacticusorg/galacticus/wiki/Constraints:-Dark-matter-progenitor-halo-mass-functions      -->
      <G0     value="+1.1425468378985500"/>
      <gamma1 value="-0.3273597030267590"/>
      <gamma2 value="+0.0587448775510245"/>
      <gamma3 value="+0.6456170934757410"/>
    </mergerTreeBranchingProbabilityModifier>
```

In these options note that we use the [`pressSchechter`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.haloMassFunctionPressSchechter) mass function and [`gnrlzdPrssSchchtr`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.gnrlzdPrssSchchtr) branching probabilities so that the solution to the excursion set problem for the non-constant collapse barrier, $\delta_\mathrm{c}$, will be used.

In the [`excursionSetBarrier`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetBarrier) section we specify the functional form of the collapse barrier. As noted in the parameter snippet, we apply to modifiers to the barrier function, one to account for the use of a sharp-$k$ window function (which is often used for models in which the power spectrum has a small-scale cut off), and one to modify the constant barrier into the form suggested by [Sheth, Mo, & Tormen (2001)](http://adsabs.harvard.edu/abs/2001MNRAS.323....1S) to account for ellipsoidal collapse (and therefore produce a better match to the N-body halo mass function).

Note that the `<applyTo value="nonRates"/>` entries here mean that these remappings of the barrier are applied only to calculations of the first crossing probability (used in the halo mass function), and not to first crossing rates (used in branching rates). This is because of the different approaches in which empirical modifications of the excursion set results have been developed as described above.

Instead of remapping the barrier, for branching rates the excursion set solutions are multiplied by an extended version of the [Parkinson, Cole, & Helly (2008)](http://adsabs.harvard.edu/abs/2008MNRAS.383..557P) modifier function, implemented by the [`PCHPlus`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.mergerTreeBranchingProbabilityModiferPCHPlus) instance of the [`mergerTreeBranchingProbabilityModifer`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.mergerTreeBranchingProbabilityModifer) class.

Lastly, in this example the collapse threshold is implemented by the [`criticalOverdensity`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetBarrierCriticalOverdensity) instance of the [`excursionSetBarrier`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Physics.pdf#physics.excursionSetBarrier) class. Therefore the barrier will be equal to whatever $\delta_\mathrm{c}(M,t)$ is being used for this model.