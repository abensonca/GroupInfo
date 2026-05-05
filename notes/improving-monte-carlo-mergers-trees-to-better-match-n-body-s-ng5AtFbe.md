# Improving Monte Carlo Mergers Trees to Better Match N-body Statistics

###### status: `active` · last reviewed: TBD

###### tags: `dark matter` `merger trees`

Consider a halo at "time" $\omega$ (the usual time variable for merger tree building), and let $S(\omega)$ be the variance along the branch of the halo as a function of time, i.e. $S(\omega) = \sigma^2(M[t])$.

This is a realization of a random walk trajectory. We want to take another step in the random walk. To do so we need to know the change in variance between our halo at time $\omega$ and the progenitor at time $\omega+\Delta \omega$.

In the usual excursion set model we assume a Brownian (i.e. uncorrelated) random walk such that the change in variance is simply
$$
\Delta S = S(\omega + \Delta \omega) - S(\omega),
$$
where $S(\omega + \Delta \omega)$ is the variance corresponding to the mass of the progenitor at time $\omega + \Delta \omega$. This corresponds to the usual $\sigma_1^2 - \sigma_2^2$ term that appears in the merger rate function.

Suppose, instead, that we want to model a correlated random walk using fractional Brownian motion. The change in variance then [becomes](https://en.wikipedia.org/wiki/Fractional_Brownian_motion#Background_and_definition)
$$
\Delta S = {\frac {1}{\Gamma (H+1/2)}}\left\{\int _{-\infty }^\omega\left[(\omega+\Delta \omega -\omega^\prime)^{H-1/2}-(\omega-\omega^\prime)^{H-1/2}\right]\,\mathrm{d}S(\omega^\prime)+\int _\omega^{\omega+\Delta\omega}(\omega+\Delta \omega-\omega^\prime)^{H-1/2}\,\mathrm{d}S(\omega^\prime)\right\},
$$
where $H$ is the Hurst exponent, and $S(\omega^\prime)$ takes the role of the white noise measure here.

In the uncorrelated case, $H=1/2$, and we have
$$
\Delta S = \int _\omega^{\omega+\Delta\omega}\,\mathrm{d}S(\omega^\prime) = S(\omega + \Delta \omega) - S(\omega),
$$
just as in the standard case.

For $H \ne 1/2$ we would need to evaulate the integral above on the branch. The problem here is that we do not know $\omega(S)$ along the branch. Instead, all we know is $\hat{\omega}(S)$, the maximum value attained by $\omega(S^\prime)$ for all $S^\prime < S$ (i.e. the [running maximum](https://en.wikipedia.org/wiki/Wiener_process#Running_maximum)), because our branch corresponds to the first-crossing events of the random walk.

So, it's not immediately obvious how to evaluate the integral for $H \ne 1/2$...

Could we actually build trees by generating random walks?

1. Start with a root halo of mass $M_0$, at time $\omega_0$;
2. Generate a random walk (Brownian or fractional Brownian), $\delta(S)$, on a grid of variance with spacing $\delta S \approx 2 S(M_0) (M_\mathrm{res}/M_0) |\alpha|$ and extending back to $S_\mathrm{res}$ such that it is fine enough to resolve mergers down to the required resolution limit;
3. Step through the grid looking for events where a new maximum $\delta$ is reached - these correspond to merger events. (For a non-constant barrier I guess this is more complicated, but I think we can still identify first-crossing events.)
4. At each first crossing event we know the mass before and after, so can assign the secondary halo that must have merged to make this event.
5. Repeat the process recursively for each secondary halo.

Then we can apply some [method](https://en.wikipedia.org/wiki/Fractional_Brownian_motion#Method_2_of_simulation) to generate fractional Brownian motion sample paths with any value of $H$.

## Generating Merger Trees Using Random Walks

The basic idea is to simply simulate excursions from the excursion set. This is trivial to do, starting from $(S_0,\delta_0)=(0,0)$ ($S_0$ is the variance [corresponding to halo mass, $M_0$], $\delta_0$ is overdensity) we can take steps in variance $\Delta S$, and select a change $\Delta \delta$ by drawing from a normal distribution with $\hat{\sigma} = \sqrt{\Delta S}$. Then we just look for the variance, $S_1$, at which the excursion first crosses the collapse barrier. Using the $S(M)$ relation, this gives us the mass of the progenitor, $M_1$.

After selecting this first progenitor mass, $M_1$, we have an amount of mass $M^\prime_1 = M_0 - M_1$ remaining which must be partitioned into progenitor halos. To do this we can simulate a new excursion starting from $(S^\prime_1,\delta_1)$ where $S^\prime_1 = S(M^\prime_1)$ and $\delta_1$ is some initial overdensity for this remaining mass which we must determined in some way. This new excursion gives us a new mass at first crossing of $M_2 < M^\prime_1$. We can continue this process of simulating excursions starting from the remaining mass until all mass is partitioned into progenitors (or, in practice, until the mass remaining to be partitioned is less then the mass resolution, at which point we stop).

### Choosing $\delta_i$ for $i\ge 1$

We have as yet not specified how we choose the starting overdensity for excursions after the primary excursion. A physically-motivated way to do this is to envision our initial patch of the universe which has collapsed into a halo of mass $M_0$ at a time corresponding to (linear theory, extrapolated) overdensity, $\delta_0$. By definition, the Lagrnagian volume of this region in linear theory is:
$$
V_0 = M_0 (1+\delta_0)^{-1}
$$
After the first excursion we have a halo of mass $M_1$ at time corresponding to overdensity $\delta^\prime$ (which we can choose to give whatever time resolution to our merger tree that we require). The Lagrangian volume of this halo must therefore be:
$$
V_1 = M_1 (1+\delta^\prime)^{-1}
$$
If we assume that the total volume and mass of our patch is conserved through the partitioning then we must have that:
$$
V_0 = V_1 + V^\prime_1
$$
where $V^\prime_1$ is the volume of the remaining mass after the first excursion. Therefore:
$$
(1+\delta_0)^{-1} = x_1 (1+\delta^\prime)^{-1} + (1-x_1)(1+\delta_1)^{-1}
$$
where $X_1=M_1/M_0$. This can be solved for $\delta_1$, with a similar approach for all subsequent excursions. As more and more of the original mass is partitioned into halos we then have that $\delta_i \rightarrow -\infty$, which will result in the subsequent excursions being biased more and more toward low mass progenitors.

### Tests

I implemented the above approach for a case with $\delta^\prime-\delta_0=0.02$ so I can make a direct comparison with Figure 2 of [Jiang & van den Bosch (2014)](https://ui.adsabs.harvard.edu/abs/2014MNRAS.440..193J/abstract). 

Here's the resulting progenitor mass function, and the ratio of the results to the analytic expectation:

![](https://i.imgur.com/umYcj5h.png)
![](https://i.imgur.com/Okj6YFQ.png)

In these figures the blue line is the analytic expectation from extended Press-Schechter theory. Green points show the distribution of primary progenitor halo (i.e. the progenitors generated by the first simulated excursion) masses, $M_1$, yellow points show the distribution for secondary progenitor masses, $M_2$, and red points show the distribution for all other progenitor masses (tertiary and higher progenitors). The blue points are the sum over all of these so show the total progenitor halo mass distribution.

The results are good, but not perfect! The primary progenitor distribution is strongly biased toward high masses (in fact, we specifically know in this case that it is biased by a factor $M_1/M_0$ relative to the extended Press-Schechter solution). This is compensated for by the secondary, tertiary, etc. distributions being biased toward low masses (which they have to be since we ensure that all of the original halo mass is put into progenitors). But, the secondary, tertiary, etc. distributions fail to get enough of the lowest mass halos (and have too many at $M_1/M_0 \approx 0.2$). Overall, this approach performs about as well as the Cole et al. (2000) algorithm (as shown in Figure 2 of [Jiang & van den Bosch (2014)](https://ui.adsabs.harvard.edu/abs/2014MNRAS.440..193J/abstract)), but no better.

### Deriving $\delta_i$ for $i\ge 1$

For our first excursion, we know that the distribution of variances at first crossing is given by the standard extended Press-Schechter solution:
$$
f_1(S_1) = \frac{1}{\sqrt{2 \pi}} \frac{\delta^\prime-\delta_0}{S_1^{3/2}} \exp \left( - \frac{\delta^\prime-\delta_0}{2 S_1} \right).
$$

For our second excursion, starting from $(S^\prime_1,\delta_1)$ the distribution of first crossing variances is:
$$
f_2(S_2) = \frac{1}{\sqrt{2 \pi}} \frac{\delta^\prime-\delta_1}{[S_2-S^\prime_1]^{3/2}} \exp \left( - \frac{\delta^\prime-\delta_1}{2 [S_2-S^\prime_1]} \right).
$$
We know that $S^\prime_1 = S(M_0-M_1)$. If we average over the distribution of $M_1$ the net distribution for the second excursion is:
$$
f_2^\prime(S_2) = \int_0^\infty f_2(S_2|S_1) f_1(S_1) \mathrm{d}S_1
$$
or, explicitly,
$$
f_2^\prime(S_2) = \int_0^\infty \frac{1}{2 \pi} \frac{(\delta^\prime-\delta_1)(\delta^\prime-\delta_0)}{[S_2-S(M_0-M_1)]^{3/2}S_1^{3/2}} \exp \left( - \frac{\delta^\prime-\delta_1}{2 [S_2-S(M_0-M_1)]}  - \frac{\delta^\prime-\delta_0}{2 S_1} \right) \mathrm{d}S_1.
$$
This could similarly be used to find the distribution for $f^\prime(S_3)$, and so on. 

The match the distribution of progenitors from extended Press-Schechter theory we require that:
$$
\sum_{i=1}^\infty f^\prime(S_i) = \frac{M_0}{M} f(S)
$$
The problem then becomes to find $\delta_i(S_i)$ that satisfies this constraint. Unfortunately, that doesn't seem to be remotely tractable! 

So, this approach essentially moves the challenge from being "*how do we draw multiple progenitors from the progenitor mass function ensuring that their masses sum to the original halo mass*", to "*how do we choose the initial overdensity for each excursion given the results of the prior excursions*". In both cases we lack knowledge about how the dependence on previously-sampled progenitors should affect subsequent progenitors.

My hope was that with this excursion set approach we could use the physically-motivated model (defined [here](https://hackmd.io/ng5AtFbeTTSPcZ00eaVzKA#Choosing-span-idMathJax-Element-64-Frame-classmjx-chtml-MathJax_CHTML-tabindex0-stylefont-size-118-position-relative-data-mathmlampx03B4i-rolepresentation%CE%B4i%CE%B4idelta_i-for-ige-1)) to answer this question. And it almost works, but not well enough to be useful.

My guess is that the physically-motivated method doesn't quite work because, in reality, the patches of mass can't really be treated as spatially separate (e.g. we smooth using a sharp-$k$ window function, which introduces correlations between adjacent patches). So, either some new insight would be needed, or you could perhaps find some empirical form for $\delta_i(S_i)$ which gives better results.

## Trials with different approach to sampling from the progenitor mass distribution

### Standard case

Using the standard Cole et al. (2000) algorithm with PCH branching rates (i.e. the best-fit parameters from their 2008 paper) and comparing to Caterpillar progenitor mass functions gives the following results:
![](https://i.imgur.com/ofLURtR.png)
So, quite good agreement as expected. Note that in the $z=0.02$ case the agreement looks good, but previously we saw discrepancies in the $x > 1$ region, which is not well-probed by Caterpillar. Also, the slope at low masses is clearly an imperfect match.

### Using the upper half of the progenitor mass function

If we switch from using the lower-half of the progenitor mass distribution (as suggested by Cole et al. 2000) to the upper-half we get:
![](https://i.imgur.com/arfkzk1.png)
It's clear that this dramatically shifts the distribution at low masses, and leads to insufficiently evolution by the high redshifts. (Of course some of this could be taken out by recalibrating the parameters of PCH.)

But, overall, it doesn't look good (as expected).

### Full Range for Probability and Accretion

In this experiment we use the full range of the progenitor mass distribution to find the branching probability and accretion rate, **but** use only the lower-half to draw branch masses.

So, specifically, if $\mathrm{d}N/\mathrm{d}M_1$ is the progenitor mass distribution then the branching probability is
$$
P = \frac{1}{2} \int_{M_\mathrm{res}}^{M_2-M_\mathrm{res}} \frac{\mathrm{d}N}{\mathrm{d}M_1} \mathrm{d}M_1
$$
where the factor of $1/2$ is included to avoid double counting, and the accretion fraction is given by:
$$
F = \frac{1}{2} \int_0^{M_\mathrm{res}} \frac{\mathrm{d}N}{\mathrm{d}M_1} \frac{M_1}{M_2} \mathrm{d}M_1 + \frac{1}{2} \int_{M_2-M_\mathrm{res}}^{M_2} \frac{\mathrm{d}N}{\mathrm{d}M_1} \frac{M_1}{M_2} \mathrm{d}M_1 
$$

This seems to reduce the overall evolution rate:
![](https://i.imgur.com/smcMDYw.png)
So, should try re-running with an increased $G_0$.

Increaseing $G_0$ by a factor 2 to $G_0 = 1.14$ gives:
![](https://i.imgur.com/cNWThZt.png)
which is very similar to the standard case - so probably no real improvement here - it just lowers the overall rate, but when we compensate for that the results are largely unchanged.

### Exact Progenitor Distribution, But Not Mass Conservation

In this experiment we ensure that we get the exact progenitor mass distribution (rather than the symmetrized one given by Cole et al.), but drop the constraint of mass conservation.

Specifically, after selecting the mass of the progenitor $M_1$ from the lower-half of the distribution, instead of assigning a mass $M_2-M_1$ to the other progenitor we assign a mass $M^\prime$ such that:
$$
\left. \int_{M_2/2}^{M^\prime} \frac{\mathrm{d}N}{\mathrm{d}M} \mathrm{d}M \right/ \int_{M_2/2}^{M_2-M_\mathrm{res}} \frac{\mathrm{d}N}{\mathrm{d}M} \mathrm{d}M = \left. \int_{M_1}^{M_2/2} \frac{\mathrm{d}N}{\mathrm{d}M} \mathrm{d}M \right/ \int_{M_\mathrm{res}}^{M_2/2} \frac{\mathrm{d}N}{\mathrm{d}M} \mathrm{d}M .
$$
That is, we match through the CDF on each half of the distribution.

This doesn't really work well:
![](https://i.imgur.com/ET8hmJ6.png)
Weird features show up at intermediate times. It looks like mass conservation can actually fail significantly in some splits.

### Neistein & Dekel (2007) approach

I coded up an implementation of the [Neistein & Dekel (2007)](https://arxiv.org/abs/0708.1599) tree building approach. While nice in principle it doesn't really seem to work:
![](https://i.imgur.com/uqDtZLz.png)
I don't understand why the low masses diverge so far from the N-body results. They model relies on a calibrated fitting function for the kernel used to sample the 1st, 2nd, 3rd, etc. progenitors - so maybe it's just not reliable in this regime?


## Conclusions?

It seems that the PCH08 approach is still the most successful. It handles sub-resolution accretion, is calibrated to N-body, etc. It fails to handle non-binary mergers - but changing the timestepping to reduce the number of these doesn't seem to significantly affect the results.

Could try further calibration of it, but it seems to be about as good as we can get for now.