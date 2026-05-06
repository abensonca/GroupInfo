# Improving Monte Carlo Mergers Trees to Better Match N-body Statistics

###### status: `active` · last reviewed: 2026-05-06

###### tags: `dark matter` `merger trees`

## Correlated Random Walks and Other Improvements

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

### Generating Merger Trees Using Random Walks

The basic idea is to simply simulate excursions from the excursion set. This is trivial to do, starting from $(S_0,\delta_0)=(0,0)$ ($S_0$ is the variance [corresponding to halo mass, $M_0$], $\delta_0$ is overdensity) we can take steps in variance $\Delta S$, and select a change $\Delta \delta$ by drawing from a normal distribution with $\hat{\sigma} = \sqrt{\Delta S}$. Then we just look for the variance, $S_1$, at which the excursion first crosses the collapse barrier. Using the $S(M)$ relation, this gives us the mass of the progenitor, $M_1$.

After selecting this first progenitor mass, $M_1$, we have an amount of mass $M^\prime_1 = M_0 - M_1$ remaining which must be partitioned into progenitor halos. To do this we can simulate a new excursion starting from $(S^\prime_1,\delta_1)$ where $S^\prime_1 = S(M^\prime_1)$ and $\delta_1$ is some initial overdensity for this remaining mass which we must determined in some way. This new excursion gives us a new mass at first crossing of $M_2 < M^\prime_1$. We can continue this process of simulating excursions starting from the remaining mass until all mass is partitioned into progenitors (or, in practice, until the mass remaining to be partitioned is less then the mass resolution, at which point we stop).

#### Choosing $\delta_i$ for $i\ge 1$

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

#### Tests

I implemented the above approach for a case with $\delta^\prime-\delta_0=0.02$ so I can make a direct comparison with Figure 2 of [Jiang & van den Bosch (2014)](https://ui.adsabs.harvard.edu/abs/2014MNRAS.440..193J/abstract). 

Here's the resulting progenitor mass function, and the ratio of the results to the analytic expectation:

![](https://i.imgur.com/umYcj5h.png)
![](https://i.imgur.com/Okj6YFQ.png)

In these figures the blue line is the analytic expectation from extended Press-Schechter theory. Green points show the distribution of primary progenitor halo (i.e. the progenitors generated by the first simulated excursion) masses, $M_1$, yellow points show the distribution for secondary progenitor masses, $M_2$, and red points show the distribution for all other progenitor masses (tertiary and higher progenitors). The blue points are the sum over all of these so show the total progenitor halo mass distribution.

The results are good, but not perfect! The primary progenitor distribution is strongly biased toward high masses (in fact, we specifically know in this case that it is biased by a factor $M_1/M_0$ relative to the extended Press-Schechter solution). This is compensated for by the secondary, tertiary, etc. distributions being biased toward low masses (which they have to be since we ensure that all of the original halo mass is put into progenitors). But, the secondary, tertiary, etc. distributions fail to get enough of the lowest mass halos (and have too many at $M_1/M_0 \approx 0.2$). Overall, this approach performs about as well as the Cole et al. (2000) algorithm (as shown in Figure 2 of [Jiang & van den Bosch (2014)](https://ui.adsabs.harvard.edu/abs/2014MNRAS.440..193J/abstract)), but no better.

#### Deriving $\delta_i$ for $i\ge 1$

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

### Trials with different approach to sampling from the progenitor mass distribution

#### Standard case

Using the standard Cole et al. (2000) algorithm with PCH branching rates (i.e. the best-fit parameters from their 2008 paper) and comparing to Caterpillar progenitor mass functions gives the following results:
![](https://i.imgur.com/ofLURtR.png)
So, quite good agreement as expected. Note that in the $z=0.02$ case the agreement looks good, but previously we saw discrepancies in the $x > 1$ region, which is not well-probed by Caterpillar. Also, the slope at low masses is clearly an imperfect match.

#### Using the upper half of the progenitor mass function

If we switch from using the lower-half of the progenitor mass distribution (as suggested by Cole et al. 2000) to the upper-half we get:
![](https://i.imgur.com/arfkzk1.png)
It's clear that this dramatically shifts the distribution at low masses, and leads to insufficiently evolution by the high redshifts. (Of course some of this could be taken out by recalibrating the parameters of PCH.)

But, overall, it doesn't look good (as expected).

#### Full Range for Probability and Accretion

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

#### Exact Progenitor Distribution, But Not Mass Conservation

In this experiment we ensure that we get the exact progenitor mass distribution (rather than the symmetrized one given by Cole et al.), but drop the constraint of mass conservation.

Specifically, after selecting the mass of the progenitor $M_1$ from the lower-half of the distribution, instead of assigning a mass $M_2-M_1$ to the other progenitor we assign a mass $M^\prime$ such that:
$$
\left. \int_{M_2/2}^{M^\prime} \frac{\mathrm{d}N}{\mathrm{d}M} \mathrm{d}M \right/ \int_{M_2/2}^{M_2-M_\mathrm{res}} \frac{\mathrm{d}N}{\mathrm{d}M} \mathrm{d}M = \left. \int_{M_1}^{M_2/2} \frac{\mathrm{d}N}{\mathrm{d}M} \mathrm{d}M \right/ \int_{M_\mathrm{res}}^{M_2/2} \frac{\mathrm{d}N}{\mathrm{d}M} \mathrm{d}M .
$$
That is, we match through the CDF on each half of the distribution.

This doesn't really work well:
![](https://i.imgur.com/ET8hmJ6.png)
Weird features show up at intermediate times. It looks like mass conservation can actually fail significantly in some splits.

#### Neistein & Dekel (2007) approach

I coded up an implementation of the [Neistein & Dekel (2007)](https://arxiv.org/abs/0708.1599) tree building approach. While nice in principle it doesn't really seem to work:
![](https://i.imgur.com/uqDtZLz.png)
I don't understand why the low masses diverge so far from the N-body results. They model relies on a calibrated fitting function for the kernel used to sample the 1st, 2nd, 3rd, etc. progenitors - so maybe it's just not reliable in this regime?


### Conclusions?

It seems that the PCH08 approach is still the most successful. It handles sub-resolution accretion, is calibrated to N-body, etc. It fails to handle non-binary mergers - but changing the timestepping to reduce the number of these doesn't seem to significantly affect the results.

Could try further calibration of it, but it seems to be about as good as we can get for now.

## Conditions and Constraints


### Test-and-Reject

This is the current approach - simply generate full merger trees, then test them to see if they meet required conditions. If they do not, discard them and try another tree. This is obviously inefficient for strong (or multiple) conditions.

### Conditioning the Branching Rate PDFs

[Notes](https://www.overleaf.com/read/yzcsjyprqvzn) on how we might modify the branching rate PDFs to enforce certain conditions. This seems like the ideal solution, if the math can be made tractable.

### Focused Test-and-Reject

Example: LMC merger onto the Milky Way. In this case, first generate the main branch only of the merger tree back to the earliest time at which an LMC merger is required. Then test for an LMC merger. If one exists, then finish building the remainder of the tree. If no LMC merger exists, destroy the tree back to the latest time at which an LMC merger is required, and try again.

* Probably need some limit on the number of attempts allowed before it gives up an just tries an entirely new tree.
* Would need to added a class which controls:
    * which branches in a tree under construction are followed;
    * tests whether a condition is met;
    * resets the tree walk as necessary to allow construction of the remainder of the tree after the condition is met

Would need to test this by comparing against the original test-and-reject method (both to benchmark speed and to test that the statistical properties of the resulting merger trees are unaffected).

## Constrained Excursion Sets

Is it possible to solve the constrained excursion set problem? Suppose that we have an excursion starting from $\delta_0(S_0)$. And suppose that we want to constrain the excursion to also pass through the point $\delta_1(S_1)$ with $S_1 > S_0$.

The set of excursions passing through these points should then be described by the [Brownian bridge](https://en.m.wikipedia.org/wiki/Brownian_bridge). 

The Brownian bridge tells us the distribution function $\delta(S)$ at any point, $S_0 < S < S_1$, and the covariances between those points.

We want to compute the first crossing distribution, $f(S)$, from this. We can't do the simple trick of evaluating the fraction of excursions above the barrier and then discounting half of them as having first-crossed at some smaller $S$ because the symmetry (i.e. that for every excursion which first crossed earlier there is a mirrored one which did not) is broken by the "drift" term in the Brownian bridge.

Is it possible though to use the approach in the appendix of [Benson et al. (2012)](https://ui.adsabs.harvard.edu/abs/2013MNRAS.428.1774B/abstract) to solve for $f(S)$. Specifically, if we take equation (A3) and use the distribution $P_0(\delta,S)$ from the Brownian bridge can we get a solution for $f(S)$? 

In the unconditioned case with a constant barrier function  this is straightforward. Then, $P_0(\delta,S)$ is just a Gaussian, so we get equation (A5), and the constant barrier means that the second integral is zero. This leaves:
$$
1 = \int_0^S f(S^\prime) \mathrm{d}S^\prime + \hbox{erf}\left[\frac{B}{\sqrt{2S}}\right],
$$
or
$$
\int_0^S f(S^\prime) \mathrm{d}S^\prime = 1 - \hbox{erf}\left[\frac{B}{\sqrt{2S}}\right].
$$
Taking the derivative with respect to $S$ then gives:
$$
f(S) = \frac{B}{\sqrt{2 \pi S^3}} \exp\left(-\frac{B^2}{2S}\right),
$$
the usual Press-Schechter solution.

It seems like the possibly difficult part about doing this in the constrained case is that in the second integral in equation (A3) of [Benson et al. (2012)](https://ui.adsabs.harvard.edu/abs/2013MNRAS.428.1774B/abstract) we need to be sure to use the correct probability distribution function taking into account the covariances in the excursion between the points $S$ and $S^\prime$ in the Brownian bridge. It should be straightforward to write this down (as the covariance has a simple form), but I'm not sure if the integrals are then solvable analytically.

There do seem to be some studies on this problem, although I've yet to get access to the actual papers:

* [Atkinson & Singham (2015)](https://faculty.nps.edu/mpatkins/docs/3_brownianBridgeStatProb.pdf) do the multi-dimensional case and have a couple references to the one-dimensional case, including:
  * [Abundo (2002)](https://www.sciencedirect.com/science/article/abs/pii/S0167715202001086) seems to have results on first crossing distributions for Brownian bridges
  * [Beghin & Orsingher (1999)](https://www.academia.edu/3480026/On_the_maximum_of_the_generalized_Brownian_bridge) 
 * Also see [Metzler (2009)](https://www.sciencedirect.com/science/article/pii/S0167715209004180)

### Ethan Notes 9/15/21

For a Brownian bridge with $B(S_1)=\delta_1$, $B(S_2) = \delta_2$, the distribution before accounting for barriers becomes:

\begin{equation}
P_{0}(\delta,S) = \mathcal{N}(\delta \lvert 0,S)\rightarrow P_{0}'(\delta,S) = \mathcal{N}(\delta \lvert \mu(S),S'(S)),
\end{equation}

where

\begin{equation}
\cases{\mu(S) = \delta_1 + \frac{S-S_1}{S_2-S_1}(\delta_2-\delta_1)\\ S'(S) = \frac{(S_2-S)(S-S_1)}{S_2-S_1}}
\end{equation}

and with covariance between $B(x)$ and $B(S)$ for $x<S$ of:

\begin{equation}
\mathrm{cov}(B(x),B(S)) = \frac{(S_2-S)(x-S_1)}{S_2-S_1}.
\end{equation}

Note that $\mathrm{cov}(B(x),B(S)) = S'(x)$.

Eq. (A3) from [Benson et al. (2012)](https://ui.adsabs.harvard.edu/abs/2013MNRAS.428.1774B/abstract) follows directly, taking care to account for the covariance between $S$ and $\tilde{S}$:

\begin{equation}
1 = \int_{0}^S f(\tilde{S})\mathrm{d}\tilde{S} + \int_{- \infty}^{B(S)}\left[P_{0}'(\delta,S) - \int_0^S f(\tilde{S})P_{0}'(\delta-B(\tilde{S}),\mathrm{var}(S)-\mathrm{cov}(B(\tilde{S}),B(S)))\mathrm{d}\tilde{S}\right]\mathrm{d}\delta.
\end{equation}

This becomes

\begin{equation} 1 =
\int_0^S f(\tilde{S})\left[1 - \mathrm{erf}\left(\frac{B(S)-\mu(\tilde{S}) - B(\tilde{S})}{\sqrt{2(S'(S)-S'(\tilde{S}))}} \right)\right] \mathrm{d}\tilde{S} + \mathrm{erf}\left(\frac{B(S)-\mu(S)}{\sqrt{2S'(S)}} \right).
\end{equation}

In the case of a constant barrier, $B(S) = B(\tilde{S}) \equiv B$, this simplifies to

\begin{equation} 1 =
\int_0^S f(\tilde{S})\left[1 + \mathrm{erf}\left(\frac{\mu(\tilde{S})}{\sqrt{2(S'(S)-S'(\tilde{S}))}} \right)\right] \mathrm{d}\tilde{S} + \mathrm{erf}\left(\frac{B-\mu(S)}{\sqrt{2S'(S)}} \right).
\end{equation}

Note that, even in the constant barrier case, differentiating with respect to $S$ no longer yields an analytic solution because the function inside the integrand now depends on $S$.

#### Updated calculation (08-September-2022)

In eq. (A3) from [Benson et al. (2012)](https://ui.adsabs.harvard.edu/abs/2013MNRAS.428.1774B/abstract) we have,

\begin{equation}
1 = \int_{0}^S f(\tilde{S})\mathrm{d}\tilde{S} + \int_{- \infty}^{B(S)}\left[P_{0}'(\delta,S) - \int_0^S f(\tilde{S})P'(\delta,S|B(\tilde{S}),\tilde{S}) \mathrm{d}\tilde{S}\right]\mathrm{d}\delta,
\end{equation}

where the two terms represent:
1. The probability of first crossing at $S < \tilde{S}$;
2. The probability to be below $B(S)$ at $S$ having never crossed the barrier at any smaller $S$.

In that second term we have two terms inside the integral:
1. The distribution function for $\delta$ at $S$, unconditioned on first crossing;
2. The probability that a trajectory that first crossed at $\tilde{S}$ is now at $(\delta,S)$, multiplied by the fraction of trajectories which _do_ cross at $\tilde{S}$, and integrated over all $\tilde{S} < S$.

In the standard excursion set problem the distribution function $P'(\delta,S|B(\tilde{S}),\tilde{S})$ is trivially found by shifting the origin of the excursion to $(B(\tilde{S}),S)$, because every step in the walk is uncorrelated. In the case of the Brownian bridge that's no longer true, so it becomes a little more complicated.

I've found it useful to think about how we construct $P'(\delta,S|B(\tilde{S}),\tilde{S})$ in the standard excursion set problem as follows:
1. We are considering a trajectory which starts at $B(\tilde{S},\tilde{S})$ and ends at $(\delta,S)$.
2. In the standard excursion set problem there is no net drift in the trajectories (i.e. upward and downward excursions are equally likely), so the effective difference in $\delta$ between these two points is $\Delta \delta = \delta - B(\tilde{S})$.
3. In the standard excursion set problem, the covariance between trajectories at $\tilde{S}$ and $S$ is just $\mathrm{Cov}(\tilde{S},S) = \mathrm{min}(\tilde{S},S) = \tilde{S}$. Therefore, the residual variance, $\Delta S$, between these two points is just $\Delta S = S - \mathrm{Cov}(\tilde{S},S) = S - \tilde{S}$.

The distribution function required is then:
\begin{equation}
P'(\delta,S|B(\tilde{S}),\tilde{S}) = \mathcal{N}(\Delta \delta, \Delta S) = \frac{1}{\sqrt{2 \pi (S - \tilde{S})}} \exp\left[ - \frac{(\delta - B(\tilde{S}))^2}{2(S - \tilde{S})}\right]
\end{equation}

as expected.

In the case of the Brownian bridge, we have two differences:
1. There is now a net drift in the trajectories, described by the function $\mu(S)$ given above. Brownian bridge distributions for aribtrary endpoints $(\delta_1,\delta_2)$ are equivalent to the standard Brownian bridge (with endpoints $(0,0)$) plus this drift term. So, we can subtract the drift from our start and end points when finding $\Delta \delta$ and will then be able to use the standard Brownian bridge distribution function. Specifically:
\begin{equation}
\Delta \delta = [ \delta - \mu(S) ] - [ B(\tilde{S}) - \mu(\tilde{S}) ] = \delta - B(\tilde{S}) - \frac{S-\tilde{S}}{S_2-S_1}(\delta_2-\delta_1)
\end{equation}
2. For the Brownian bridge, the covariance is 
\begin{equation}
\mathrm{Cov}(B({\tilde{S}}),\delta) = \frac{[S_2-S][\tilde{S}-S_1]}{S_2-S_1}.
\end{equation}
The residual variance between the two points is then
\begin{equation}
\Delta S = \mathrm{Var}(S) - \mathrm{Cov}(B({\tilde{S}}),\delta) = \frac{(S_2-S)(S-S_1)}{S_2-S_1} - \frac{(S_2-S)(\tilde{S}-S_1)}{S_2-S_1}.
\end{equation}
which simplifies to
\begin{equation}
\Delta S = \frac{(S_2-S)(S-\tilde{S})}{S_2-S_1}.
\end{equation}

In the limit that $S_2 \rightarrow \infty$ we would expect to recover the distribution function for the unconstrained case. For the offset $\Delta \delta$ we have
\begin{equation}
\Delta \delta = \delta - B(\tilde{S}) - \frac{S-\tilde{S}}{S_2-S_1}(\delta_2-\delta_1) \rightarrow \delta - B(\tilde{S})
\end{equation}
as expected, and for the residual variance we have
\begin{equation}
\Delta S = \frac{(S_2-S)(S-\tilde{S})}{S_2-S_1} \rightarrow S - \tilde{S}
\end{equation}
also as expected.

#### Outdated original notes

Assuming a constant barrier and that the final integral still vanishes after integration over $\delta$ (I'm not sure about the latter assumption), the result follows from the unconditioned case with a replacement of variables $\delta \rightarrow \delta - \mu$, $S\rightarrow S'$:

\begin{equation}
\int_0^S f(\tilde{S})\mathrm{d}\tilde{S} = 1 - \mathrm{erf}\left(\frac{B-\mu}{\sqrt{2S'}} \right),
\end{equation}

Solving for $f(S)$ yields

\begin{equation}
f(S \lvert B(S_1)=\delta_1, B(S_2) = \delta_2) = \frac{1}{\sqrt{2\pi S'^3}}\exp\left(-\frac{(B-\mu)^2}{2S'}\right)\left[(B-\mu)\frac{S_2 + S_1 - 2S'}{S_2 - S_1} + \frac{2(\delta_2-\delta_1)S'}{S_2 - S_1}\right].
\end{equation}

After some simplification that needs to be checked,

\begin{equation}
f(S \lvert B(S_1)=\delta_1, B(S_2) = \delta_2) = \frac{1}{\sqrt{2\pi S'^3}}\exp\left(-\frac{(B-\mu)^2}{2S'}\right)\frac{\delta_2(S-S_1)^2 - \delta_1(S-S_2)^2 + B(S_1+S_2)(S_2 - S_1 - 2S)}{(S_2 - S_1)^2}.
\end{equation}

Note that this reduces to the expected answer in the limit $S_2\rightarrow \infty$.

##### Comparison to [Beghin & Orsingher (1999)](https://www.academia.edu/3480026/On_the_maximum_of_the_generalized_Brownian_bridge)

 Remark 2.4 is analogous to our setup. The first-crossing distribution for times within the Brownian bridge ($0<t<u$) is given by the first case in Eq. (2.15):

\begin{equation}
f_{\beta}(t\lvert B(u) = \eta) = \beta\sqrt{\frac{u}{(u-t)2\pi t^3}} \exp\left({-\frac{(u\beta-\eta t)^2}{2ut(u-t)}}\right).
\end{equation}

To compare, we replace $\beta\rightarrow B$, $t\rightarrow S$, $u\rightarrow S_2$, $\eta = \delta_2$:

\begin{equation}
f_{B}(S\lvert B(S_2) = \delta_2) = B\sqrt{\frac{S_2}{(S_2-S)2\pi S^3}} \exp\left({-\frac{(S_2B-\delta_2 S)^2}{2S_2 S(S_2-S)}}\right).
\end{equation}

In our expression, we set $S_1 = 0$ and $\delta_1 = 0$, which yields

\begin{equation}
f(S \lvert B(S_2) = \delta_2) = \frac{1}{\sqrt{2\pi S'^3}}\exp\left(-\frac{(B-\mu)^2}{2S'}\right)\left[\frac{\delta_2 S^2 + BS_2(S_2-2S)}{S_2^2}\right]
\end{equation}

\begin{equation}
 = \sqrt{\frac{S_2}{(S_2-S)^32\pi S^3}} \exp\left({-\frac{(S_2B-\delta_2 S)^2}{2S_2 S(S_2-S)}}\right) \left[\frac{\delta_2 S^2 + BS_2(S_2-2S)}{S_2}\right].
\end{equation}

The expressions are somewhat similar. To match, the term in brackets would need to yield $B(S_2-S)$, which it doesn't (though it's close for $S_2\gg S$). Maybe there is a different assumption, e.g. about the limits of integration (see Eq. (2.12)). Need to check this ...

Some of the subsequent results in this paper might be more directly applicable since they include drift terms and two-sided constraints, but first-crossing distributions aren't provided for those cases.


### Negative Assertion in the Excursion Set Approach

Building on Trey's thoughts on this. Suppose we have a halo of mass, $M_0$, and we want to assert that it _does not_ merge with a progenitor with mass greater than $M_1$. 

In terms of the excursion set approach I think this means that such a halo _can_ have a first crossing between $S_0=\sigma^2(M_0)$ and $S_{01}=\sigma^2(M_0-M_1)$ (in this case we have one progenitor of mass between $M_0-M_1$ and $M_0$ - and so the second progenitor must have a mass $<M_1$), or it _can_ have a first crossing at $>S_1=\sigma^2(M_1)$ (in this case we have one progenitor of mass $<M_1$, and a second progenitor of mass $>M_0-M_1$). But, it _can not_ have a first crossing between $S_{01}$ and $S_1$.

![](https://i.imgur.com/TMICaw0.png)

where the two black trajectories are acceptable, but the red one is not.

Then we'd need to figure out the first crossing distribution, $f(S)$, given these conditions. The approach we've previously taken (e.g. above) is to write a probability equation for trajectories at some variance $S$ that is schematically:
$$
(\mathrm{total\, probability}) = \mathrm{(crossed\, at }<S) + \mathrm{(not\, yet\, crossed)}
$$

In the case with a negative constraint we want to exclude trajectories that cross in a certain range of $S$, so we modify this to be:
$$
(\mathrm{total\, probability}) = \mathrm{(crossed\, at }<S) + \mathrm{(not\, yet\, crossed)} + \mathrm{(excluded)}
$$

For $S<S_{01}$ no trajectories are excluded so this probability equation is unchanged, and so the first crossing distribution should just be that for an unconditioned excursion, $f^\prime(S)$.

For $S_{01}<S<S_1$ then we have $f(S)=0$ by construction.

For $S>S_1$ writing out this equation explicility gives:
\begin{eqnarray}
1 &=& \int_{0}^S f(\tilde{S})\mathrm{d}\tilde{S} \nonumber \\
& & + \int_{- \infty}^{B(S)}\left[P_{0}'(\delta,S) - \int_0^S f(\tilde{S})P'(\delta,S|B(\tilde{S}),\tilde{S}) \mathrm{d}\tilde{S} - \int_{S_{01}}^{S_1} f^\prime(\tilde{S})P'(\delta,S|B(\tilde{S}),\tilde{S}) \mathrm{d}\tilde{S}\right]\mathrm{d}\delta \nonumber \\
& & + F,
\end{eqnarray}

where in the second line we do the usual thing of starting with the unconditioned distribution of trajectories $P_0^\prime(\delta,S)$, and subtract off the contribution from trajectories which crossed at some lower $S$ and are now below the barrier (first integral in the [] on the second line). We now must also subtract off the contribution from any trajectories that were excluded and would now be below the barrier - this is the second integral in the [] on the second line (note that in this, we use $f^\prime(S)$ - the first crossing distribution with no negative assertion applied). Lastly we must add on the "(excluded)" probability term,
$$
F = \int_{S_{01}}^{S_1} f^\prime(S) \mathrm{d}S,
$$
which is just a constant.

I haven't yet gone through the next steps to see how tractable this is. The constant $F$ term should be no problem. It's less clear to me if the second integral term on the second line causes any complications - I think that, given knowledge of the unconstrained solution $f^\prime(S)$ it should be straightforward to evaluate, so hopefully it isn't a big problem.

If so, then we have an equation to solve for $f(S)$ (the first crossing distribution with a negative constraint) which hopefully looks similar enough to the original case that we can use the existing machinery to solve it. The last thing to keep in mind would be that this would give use the first crossing probability for only the set of trajectories that _were not_ excluded by the constraint. Since we excluded a fraction $F$ of all trajectories then the to get the first crossing probability for the not-excluded subset we just renormalize $f(S) \rightarrow f(S)/[1-F]$.

### Constraining on the presence of the LMC

Suppose we want to generate a Milky Way halo of mass $M_{\mathrm{MW},z=0}$ at $z=0$, and require that it merges with an LMC halo of mass $M_{\mathrm{LMC},z=z_\mathrm{LMC}}$ at redshift $z_\mathrm{LMC}$.

In this case we can not simply use the above constrained merger tree approach to require that a progenitor at coordinates $(M_{\mathrm{LMC},z=z_\mathrm{LMC}},z_\mathrm{LMC})$ because this would result in a merger between the LMC and the MW halos at some redshift $z < z_\mathrm{LMC}$ (i.e. not _at_ $z=z_\mathrm{LMC}$).

Instead we can (by creating a suitable `mergerTreeBuildController` object) simply _insert_ an LMC at $(M_{\mathrm{LMC},z=z_\mathrm{LMC}},z_\mathrm{LMC})$ and make it merge with the main branch of the MW merger tree.

The problem then is that the mass of the main branch of the MW merger tree at $z=z_\mathrm{LMC}$, $M_{\mathrm{MW},z=z_\mathrm{LMC}}$, will not be an unbiased set set of $M_{\mathrm{MW},z=z_\mathrm{LMC}}$ drawn from all possible MW merger trees. (For an extreme example of why this must be, it is clear that we must have $M_{\mathrm{MW},z=z_\mathrm{LMC}} > 2 M_\mathrm{LMC}$ such that it is possible to have a merger event with a halo of mass $M_\mathrm{LMC}$ and have the Milky Way halo still be more massive that $M_\mathrm{LMC}$.)

Therefore, what we need to know is the distribution of $M_{\mathrm{MW},z=z_\mathrm{LMC}}$ conditioned on there being a merger with the LMC halo at that redshift. Call this $p(M_{\mathrm{MW},z=z_\mathrm{LMC}}|M_\mathrm{LMC})$.

We can use Bayes theorem to write this as:
$$
p(M_{\mathrm{MW},z=z_\mathrm{LMC}}|M_\mathrm{LMC}) = p(M_\mathrm{LMC}|M_{\mathrm{MW},z=z_\mathrm{LMC}}) \frac{p(M_{\mathrm{MW},z=z_\mathrm{LMC}})}{p(M_\mathrm{LMC})}
$$
where $p(M_\mathrm{LMC}|M_{\mathrm{MW},z=z_\mathrm{LMC}})$ is the distribution of $M_\mathrm{LMC}$ given $M_{\mathrm{MW},z=z_\mathrm{LMC}}$, and $p(M_{\mathrm{MW},z=z_\mathrm{LMC}})$ and $p(M_\mathrm{LMC})$ are the unconditioned distributions of the two halo mases. We can ignore the latter, as it's constant (for our fixed choice of $M_\mathrm{LMC}$) and we can just renormalize the distribution function, so:
$$
p(M_{\mathrm{MW},z=z_\mathrm{LMC}}|M_\mathrm{LMC}) \propto p(M_\mathrm{LMC}|M_{\mathrm{MW},z=z_\mathrm{LMC}}) p(M_{\mathrm{MW},z=z_\mathrm{LMC}})
$$

For the conditional term, $p(M_\mathrm{LMC}|M_{\mathrm{MW},z=z_\mathrm{LMC}})$ this is just the usual merger rate that we use to build merger trees, specifically ([PCH08](https://ui.adsabs.harvard.edu/abs/2008MNRAS.383..557P/abstract)):
$$
p(M_\mathrm{LMC}|M_{\mathrm{MW},z=z_\mathrm{LMC}}) \propto \sqrt{\frac{2}{\pi}} \frac{M_\mathrm{MW}}{M_\mathrm{LMC}^2} \frac{\sigma_\mathrm{LMC}^2}{[\sigma_\mathrm{LMC}^2-\sigma_\mathrm{MW}^2]^{3/2}} \left| \frac{\mathrm{d} \log \sigma_\mathrm{LMC}}{\mathrm{d}\log M_\mathrm{LMC}} \right| G\left( \frac{\sigma_\mathrm{LMC}}{\sigma_\mathrm{MW}},\frac{\delta_\mathrm{MW}}{\sigma_\mathrm{MW}} \right)
$$
where $\sigma_\mathrm{LMC} = \sigma(M_\mathrm{LMC})$ etc., and where I've left out the redshift dependent terms as they're constant (at fixed $z_\mathrm{LMC}$ so are irrelevant after renormalization). In the above, $G()$ is the modification function that [PCH08](https://ui.adsabs.harvard.edu/abs/2008MNRAS.383..557P/abstract) introduced to make their merger trees agree closely with N-body results.

For the term $p(M_{\mathrm{MW},z=z_\mathrm{LMC}})$ things are a little more difficult. This would be the unconditioned distribution of $M_{\mathrm{MW},z=z_\mathrm{LMC}}$ (i.e. the distribution resulting from a set of merger trees with no conditions applied to them), but for the _main branch_. Extended Press-Schechter theory doesn't give us a way to compute this directly (it predicts the distribution function for all progenitor masses at some earlier redshift, but not for the most massive progenitor.)

[PCH08](https://ui.adsabs.harvard.edu/abs/2008MNRAS.383..557P/abstract) look at these distributions (their Figure 2) and show that their algorithm nicely matches the distributions measured from N-body simulations. So, we could estimate $p(M_{\mathrm{MW},z=z_\mathrm{LMC}})$ empirically by just generating a large number of merger trees.

Alternatively, if we look at [Cole2007](https://ui.adsabs.harvard.edu/abs/2008MNRAS.383..546C/abstract), specifically their Figure 4, they show distributions of primary progenitor mass, and overplot (as dotted lines) their _"global fit"_ (their equation 7) to the progenitor mass function. From this it might be possible to find a similar _"global fit"_ to the distribution of the primary progenitor masses - it would look similar, but with some (probably exponential?) cut off at low masses. Having such a fit would be extremely useful for this type of constraint problem.

Assuming that we could find a global fit for $p(M_{\mathrm{MW},z=z_\mathrm{LMC}})$ (or, even just measure it empirically from a large sample of trees), then the process of generating constrained MW trees with an LMC would be:
1. Sample a MW mass, $M_{\mathrm{MW},z=z_\mathrm{LMC}}$, from the distrbution function $p(M_{\mathrm{MW},z=z_\mathrm{LMC}}|M_\mathrm{LMC})$;
2. Use the constrained tree solver to generate a main branch from $z=0$ to $z_\mathrm{LMC}$ with the condition that there exists a progenitor at $(M_{\mathrm{MW},z=z_\mathrm{LMC}},z_\mathrm{LMC})$.
3. Insert a merger with the LMC at this redshift.

Another challenge here is that we would need to tabulat constrained merger tree branching rates as a function of the constrained mass.

### Limitations of the Brownian bridge solver approach

I spent some time the past few days trying to understand why the results for LMC infall times that you find with the filtered trees and the constrained trees differ. I ruled out various numerical issues, and I think have convinced myself that there are two factors:
1. The choice of sampling from the full range of mass $M_\mathrm{res} < M < M_\rm{parent}$ when selecting progenitor halo masses (instead of sampling from $M_\mathrm{res} < M < M_\rm{parent}/2$ as we do in the unconstrained case). 
2. The limited accuracy of the excursion set solver.

Taking point 2 first - it seems that when tabulating the branching rates with our LMC constraint the numerical solution truncates to zero at a mass $> M_\mathrm{LMC}$ (because the numerical solution becomes negative which would be unphysical). This means that we don't have the correct branching rates for masses close to M_LMC. This problem seems to be related to the finite numerical precision of the excursion set solver (even though we use quad precision for it), or possibly the finite numerical precision of the error function implementation that we use. When solving the excursion set problem we have the subtract off the fraction of trajectories that have crossed the barrier at lower variance from the fraction that have crossed at the current variance. Those numbers both become very close to 1 for larger variances - and so small numerical errors can lead to big problems. I'm not sure that there's a simple way around this problem - other than just increasing the numerical precision further (which would be difficult).

For the second point, I looked at the predicted distribution of progenitor halo masses at a very tiny timestep before $z=0$. Specifically, I forced the calculation to take just a single, very tiny timestep, and then looked at the results. I've attached a plot which shows the results. Look first at the "unconstrained" case - this is just running a model with no constraint and no filtering. For such a tiny timestep the MW halo is mostly unchanged - so there is always a point at 1 on the y-axis at close to the initial MW mass (1.3e12). There's then a distribution of progenitors at low number.

![](https://hackmd.io/_uploads/HJJOBfOh2.png)

If you then look at the "filtered" points - these are from unconstrained trees to which I then applied our LMC filter. The result makes sense - there's now an enhancement in progenitors of LMC mass (and a corresponding number of MWs with reduced mass) - with the lower mass distribution being largely unaffected. This all seems very reasonable.

Looking next at the "constrained_full" points - this is from running our constrained trees. The results are very different. I think I've been able to track this down to point 1 in the above. Because we have to sample from the full $M_\mathrm{res} < M < M_\rm{parent}$ range it seems that we underestimate the overall branching rate (and also the rate of subresolution accretion). So, we get too few branchings to progenitors. There _is_ an enhancement at $\sim 1.5 \times 10^{11}\mathrm{M}_\odot$ - this looks like almost an LMC, but I think is actually spurious and arises because of the inaccuracy in the numerical solver.

I also don't see an easy way around this problem - we can't sample from the $M_\mathrm{res} < M < M_\rm{parent}/2$ range as that will give completely wrong results (this is the "constrained" points on the plot - which are so wrong you can't even see them).

So, I think that, unfortunately, to make this work accurately we would need to solve both problems. Problem 2 is just technical/numerical so potentially could be solved by going to some higher order solver. Problem 1 is a long-standing issue that we don't know how to solve (we need to be able to sample from the full range of mass while asserting mass conservation in the two progenitors produced, and probably allowing for N>2 progenitors in branching events also).

### Notes 11/26/2023

Generate unconstrained trees. Select those branches that meet a constraint. Look at distribution of trajectories. Figure out how to modify branching rate to match that - using Brownian bridge solution as a guide.

Maybe also look at other branches in those trees - do they still follow the regular solution statistics?

### Notes from 06/17/2024

In the current Brownian bridge approach, we build a trajectory back to the time of interest, $\delta_2$, and then insert a jump to our required halo of variance $S_2$. The crucial aspect of this is that the distribution of parent halo masses at $\delta_2-\epsilon$ must be an unbiased sample of those we would get by simply filtering trees to match our constraint.

The Brownian bridge approach ensures that we get a progenitor at $\delta_2-\epsilon$ which has $S < S_2$. Using the reflection principle we can then assert a merger to $(S_2,\delta_2)$ from our Brownian bridge. _But_, this ignores the fact that there will also be trajectories from $(S<S_2,\delta_2-\epsilon)$ which _do not_ cross the barrier at $S_2$ but are below it (and always below it). So, I think we should weight trees by:
$$
p(S_2,\delta_2|S,\delta_2-\epsilon) / p(S_2,<\delta_2|S,\delta_2-\epsilon)
$$
where, for trajectories starting from $(S,\delta_2-\epsilon)$, the numerator is the probability to make a first upcrossing at $(S_2,\delta_2)$, and the denominator is the probability for the trajectory to be below $\delta_2$ at $S_2$ having never crossed the barrier between $S$ and $S_2$ (a similar calculation is performed in the usual numerical calculation of the first crossing solution).
## Constrained Merger Trees

### Conditioned Excursion Sets

We've explored possible solutions using constrained excursion sets using a [Brownian bridge](https://en.wikipedia.org/wiki/Brownian_bridge) approach. But, I think there are some limitations to this that I've not previously fully understood.

Before going into these I think it's worth restating the goal. Ideally, we would like to impose a merger event with given properties (primary and secondary halo masses, time) into our merger tree. In the excursion set approach a merger corresponds to a change in the [supremum](https://en.wikipedia.org/wiki/Infimum_and_supremum) of the excursion (that is, a point where the previous maximum, $\delta_\mathrm{max}$, of the excursion is exceeded). If the previous maximum occured at $(S_0,\delta)$, and is exceeded at $(S_1,\delta+\epsilon)$ (where here $\epsilon$ is a infinetesimal) then we consider that the mass of the trajectory jumps from $M_0=M(S_0)$ to $M_1=M(S_1)$ at time $\delta$, corresponding to a merger with a secondary halo of mass $M_2=M(S_0)-M(S_1)$.

Such a trajectory might look this like:
![](https://i.imgur.com/XCTaRRp.png)
In order to impose such an event in our merger tree - using an excursion set approach - we would need to force _two_ conditions: first that the trajectory first crosses $\delta$ at $S_0$, and second that it then crosses $\delta+\epsilon$ at $S_1$. 

The corresponding trajectories are actually _conditioned Brownian bridges_ (related to [Brownian excursions](https://en.wikipedia.org/wiki/Brownian_excursion)), because we not only require that trajectory to pass through specified start and end points, but also require that it not cross the barrier anywhere between those start and end points.

For example, consider the part of the trajectory between $S_0$ and $S_1$. In order to get a merger of mass $M_2=M(S_0)-M(S_1)$ we require that this trajectory does not cross $\delta$ at any $S$ in the range $[S_0,S_1)$. So, our Brownian bridge must be conditioned to stay below $\delta$ (equivalent to conditioning a bridge to be always negative since we can apply an arbitrary vertical translation). While it's easy to simulate such trajectories ([using the reflection principle](https://stats.stackexchange.com/a/305058)$^\dagger$), what we would need is a model for the distribution $P(\delta|S)$ and its covariance so that we could solve the first crossing problem, and I'm not aware that this is known. _But_, of course, by definition the first crossing distribution here is just $P(\delta|S) = \delta(S-S_1)$ (where I'm re-using $\delta$ here to mean the Dirac $\delta$-function). So, we don't need to solve for any first crossing distribution, and imposing this on our tree is simply a case of sampling from this distribution (i.e. just inserting a halo of mass $M_2$ directly).

A similar situation applies for the region $0 < S < S_0$. Here, we would like to know the first crossing distribution for smaller values of $\delta$, so that we can construct a mass history for the merger tree which is consistent with first crossing at $(\delta,S_0)$. This is again a conditioned Brownian bridge, conditioned to stay below $\delta$. But, in this case we _do_ need to know the distribution function and covariance of the set of all such excursions for $0 < S < S_0$.

The problems with this approach then are:
1. We need to use conditioned Brownian bridges, but I'm not aware of a result for the distribution function and covariance that we would need to solve the excursion set first-crossing problem for these:
2. Even if we could solve this, in practice when constructing merger trees we modify the branching rate function by multiplying by an empirical function $G()$ to give us a better match to N-body simulations. I don't think it is clear that this same empirical correction function would be the relevant one for the subset of excursions corresponding to the conditioned Brownian bridge.

---

$^\dagger$ I think this could be done in the "excursion set simulator" merger tree builder that I experimented with. In that we just generate a trajectory from the excursion set, and look for first-crossings to build a mass history. It seemed to work moderately well (i.e. as well as other methods). You could build in reflection to this by simply looking for steps which exceed the barrier and performing the relevant reflection to force the trajectory back below the barrier. Although, this approach did need to subsample trajectories to get the correct mass-weighting, and it's not immediately obvious to me how that would be included in this case.

#### What is the Brownian bridge approach good for?

Since we've developed this (unconditioned) Brownian bridge technology, what is it good for? The trajectory $(\delta,S)$ is the overdensity at some point in the density field when smoothed on a scale corresponding to a variance $S$. The Brownian bridge therefore allows us to construct the excursion set which is conditioned to have some specified overdensity when smoothed on some scale. Translated into physical terms, we can fix the overdensity on a certain mass scale - that is we can fix the environment on a certain mass scale, and construct excursions on larger mass scales that are consistent with that environment.

So, for example, suppose we care about regions which are highly overdense, e.g. $\delta\approx 12$ on, for example, scales corresponding to $10^{12}\mathrm{M}_\odot$. This could allow us, for example, to explore regions which might contain halos which  host the high-mass SMBHs seen at $z\approx 6$. Using the Brownian bridge we can then generate merger trees, rooted at $z=0$, which would be consistent with this high-overdensity region at $z\approx 6$.

Note that I'm being purposely careful with language here - because the halo mass at this time $\delta$ depends on the first-crossing point, we could have a halo more massive than $10^{12}\mathrm{M}_\odot$ - we don't put a constraint on halo mass, just on the overdensity of the environment. This relates back to the classic cloud-in-cloud problem where the region could also be sufficiently overdense to collapse on some larger scale. However, my intuition is that, for extreme cases (i.e. very overdense regions, corresponding to $M \gg M_*(\delta)$) then it is most likely that you _would_ get a distribution of halo masses at $z=6$ that is sharply peaked close to $10^{12}\mathrm{M}_\odot$.

### Semi-refined approach

Back to the original problem. We would like to impose a merger of a given mass halo, $M_2$ with the main branch of our tree at a given time, $t_2$. As we've seen above, inserting the actual merger is trivial, since the PDF is a $\delta$-function. But, we need to build the main branch of the tree back to $t_2$ first, and assign the appropriate weight to the tree such that the distribution of trees is consistent with that we would obtain with a simple brute-force down-sampling approach.

To be more specific, suppose that we want to ensure that $M_1$ (the mass of the main branch) at $t_2$ has the same distribution as obtained from the brute-force downsampling approach. I think that this can be obtained by simply building the main branch (from $z=0$) back to $t_2$ and then assigning a probability:
$$
p(M_1|M_2,t_2) = \left\{ \begin{array}{ll} R(M_1|M_1+M_2,t_2) & \hbox{if } M_1 \ge 2 M_2, \\ 0 & \hbox{if } M_1 < 2 M_2, \end{array} \right.
$$
where $R(M_1|M_0,t)$ is the merger rate function for a halo of mass $M_0$ at time $t$ to experience a merger event with a primary progenitor of mass $M_1$. Note that the probability assigned to the tree is zero if $M_1 < 2 M_2$ since in such cases the tree can not have a merger in which the secondary has a mass $M_2$.

A slightly-more-refined-than-brute-force, "semi-refined" approach then would be as follows:
1. Generate a formation history for the main branch from $z=0$ back to $t_2$.
2. If $M_1$ (the mass of the main branch at $t_2$) is less than $2 M_2$ then discard the tree and go back to step 1. (In fact, we can reject the tree early if at any step in constructing the branch the mass drops below $2 M_2$.)
3. Once a suitable $M_1$ is generated, insert a merger with a halo of mass $M_2$, and multiply the weight of the tree by the probability $p(M_1|M_2,t_2)$ defined above.

The distribution of $M_1$ at $t_2$ should then match that obtained from the brute-force down-sampling approach. 

This approach still involves some brute-forcing, but I expect that (in the specific case we care about - the LMC-MW merger) we will reject very few cases in step 2 above because the typical Milky Way progenitor mass at $t_2$ will be much larger than $M_\mathrm{LMC}$.

I suggest that we try this approach and validate it against the brute-force down-sampling approach by comparing distributions of $M_1$ and time $t_2$.

#### Marginalizing over LMC properties

In practice there is some distribution over $(M_2,t_2)$ constrained by observations. If we know that PDF (at least to some approximation), we can in principle just sample from it each time we start growing a tree. I think it is important that when a tree is rejected (for having $M_1 < 2 M_2$ at $t_2$) we need to resample from the distribution of $(M_2,t_2)$. This is because the distribution of $M_1$ will depend both on the "prior" distribution over $(M_2,t_2)$, but also on the "likelihood" of a consistent with each $(M_2,t_2)$.

#### Including negative constraints

For a realistic LMC-MW history we probably want to additionally assert that there are no other LMC-like mergers. This is a negative assertion, so I think can be trivially imposed by cutting off the merger rate function for masses above those that would correspond to such a merger.

#### Galacticus implementation

To impose these constraints we need some controller object which is aware of all of the parts needed to achieve them. In the case of just the positive constraint (imposing a merger at the desired time) such a controller would need to:
1. Choose an appropriate mass and time for the merger event.
2. If on the main branch, limit the step size such that it does not exceed time $t_2$.
3. At time $t_2$, decide whether to keep the tree:
    1.  If it is to be kept, insert the merger, and apply the appropriate weight.
    2.  If it is to be rejected, prune the tree back to $z=0$, draw a new mass and time for the merger.
4.  Once the merger is inserted, continue building the tree as normal.

If we want to include some negative constraints then we would additionally need to modify the branching rate distribution.

The above then involves the following classes in Galacticus:
* [`mergerTreeBuildController`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBuildControllerClass)
    * Choose ($M_2,t_2$);
    * Decide whether to accept/reject the Milky Way progenitor at $t_2$;
    * Insert the LMC halo at $t_2$;
* [`mergerTreeBranchingProbability`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBranchingProbabilityClass)
    * Maximum allowed timestep (to limit to $t_2$);
    * Branching rates (to allow negative constraints to be applied);

The [`mergerTreeBuildController`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBuildControllerClass) class is sufficiently flexible to do the above. The [`mergerTreeBranchingProbability`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBranchingProbabilityClass) could also be made to do this, but there is the problem that it needs to be aware of ($M_2,t_2$) so that it can impose the appropriate step-size and truncations in the branching rates.

A solution might be to extend the functionality of the [`mergerTreeBuildController`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBuildControllerClass) class such that, at each step, it provides the [`mergerTreeBranchingProbability`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBranchingProbabilityClass) object to the [`mergerTreeBuilder`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBuilderClass). Then, for example, the [`mergerTreeBuildController`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBuildControllerClass) could accept a user-defined [`mergerTreeBranchingProbability`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBranchingProbabilityClass) object as usual, but use the decorator pattern to wrap this inside another object that imposes a maximum timestep to not exceed $\delta_2$, if on the main branch at $t > t_2$. That is:
* If on main branch and $t > t_2$ return a [`mergerTreeBranchingProbability`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBranchingProbabilityClass) which provides a timestep of $\Delta w^\prime_\mathrm{max} = \hbox{min}(w_2-w,\Delta w_\mathrm{max})$;
* otherwise return a [`mergerTreeBranchingProbability`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBranchingProbabilityClass) which provides a timestep of $\Delta w_\mathrm{max}$.

A similar approach could be used for the negative assertion imposition perhaps.

In this way, the logic associated with the condition(s) to be applied are kept local within a single [`mergerTreeBuildController`](https://github.com/galacticusorg/galacticus/releases/download/bleeding-edge/Galacticus_Development.pdf#class.mergerTreeBuildControllerClass)  object.

#### Notes on inserting a target halo

I think that, in the new constrained runs, the reason they drop to very low mass very quickly is just a consequence of us sampling from the full range, 0 to M, for the branching masses and then marking whatever mass halo is returned as the "main branch". Most progenitors are very low mass, so this will almost inevitably lead to the first step in the tree jumping to a low mass branch. So, I don't think this approach is going to work well.

Thinking more about this (and remembering some of my prior thinking on it), I think that the problem with interpreting these results is that we fix a point (S2,δ2) on the trajectory, but this does not guarantee that we get a halo at that point. We solve the first crossing distribution, and build a tree based on that, so we have a trajectory that passes through (S2,δ2), but typically will first cross much earlier (i.e. att S < S2).

So maybe our approach is valid, but the interpretation of the condition approached is more complicated/less relevant. It's still unclear to me exactly which branch through the tree this should be applied to.

A different approach would be to use the excursion set simulator tree builder. I think this could be modified to generate a trajectory from the Brownian bridge and then use the reflection principle to create a trajectory that first crosses at (S2,δ2). Then build the rest of the tree as normal. The challenge there is that trajectories need to be weighted to convert from volume to mass sampling. It's not really clear to me how to do that?

Alternatively, we could keep the current approach but slightly modified. First, reatin the sampling from the full range, 0 to M, but always use the most massive progenitor as the main branch. In this attached sketch I've shown a single trajectory from the Brownian bridge (frmo the green to the red point) as the solid blue line. It should be the case that our conditioned solver means that this trajectory must first cross δ2 (corresponding to the upper horizontal dashed line) at some S=Sf (corresponding to the orange dot) between S1 and S2 - and then the trajectory moves above the δ2 line, so we never get a halo at (S2,δ2).

![](https://i.imgur.com/j1MQqIz.png)


But, I think we can apply the reflection principle here - we take the parts of the trajectory above δ2 and reflect them through that line, giving the dot-dashed blue lines. This is then an equally probable trajectory as the original. In particular, that implies that the trajectory for S < Sf corresponding to the first crossing (orange point) is a valid trajectory, correctly sampled from the distribution function of all trajectories in this Brownian bridge.

So, suppose we build our tree main branch back to time δ2, where it has a mass Sf < S2. Through the construction above we can now insert a progenitor at this time corresponding to S2 (i.e. at δ2 the trajectory jumps from Sf to S2). That progenitor will either be a halo on the main branch, or a halo that merges with the main branch, depending on whether M(Sf) > 2 M(S2). But, either way, we have now placed a halo at (S2,δ2) precisely, with a valid main branch at δ < δ2. 

It seems like this does a lot of what we want it to do. The only thing that I think is still slightly problematic is that this requires that the (S2,δ2) progenitor be either on the main branch, or merges directly with it - it doesn't allow for cases where that progenitor first merged with some other progenitor in a side branch. But, maybe this isn't a big deal.

For practically implementing this in Galacticus - I think we have most of what's needed - the conditioned branching rates are already all implemented. The remaining thing would be to identify when the main branch reaches δ2 and then insert the required halo directly. This is probably best done via the `mergerTreeBuildController` class - it could probably just check if the last-inserted halo is a) on the main branch, and b) exists at δ > δ2 while its parent exists at δ < δ2 (such that this represents the step straddling δ2). Then, it would replace that halo (and any sibling) with the required target progenitor (plus a second progenitor to hold the remainder of the mass). 

I think a good first step would be to go back to the case where we always follow the main branch (so remove the edits in the `mergerTreeBuilderCole2000` class), run the constrained case again, and check that the main branch mass at δ2 is always such that S < S2. If it is, then I think that shows our constrained trajectories are working as expected, and we can figure out the `mergerTreeBuilderController` to insert the target halo.

### "Intelligent" Brute Force Approach (18-July-2025)

This approach is implemented in Galacticus since 19-December-2024 via the `mergerTreeBuilderConstrained` class. This uses the classic brute force approach (i.e. generate a merger tree, check if it meets our required constraints, and reject it if it doesn't), but does so more efficiently - particularly when multiple constraints are applied.

In summary this approach:
* Breaks the process of building a merger tree into an aribtrary number of phases. 
* Typically, in each phase, we apply a single constraint, once that constraint is met, we move to the next phase which will apply the next constraint, and so on.

This approach has two advantages:
1. For each constraint we build "just enough" tree to be able to check the constraint. For example, suppose we are constraining MW trees to have an LMC - typically this is a constraint to have a progenitor of a certain mass infalling at a certain redshift. We then need only build the tree with mass resolution just enough to resolve potential LMCs, and back to just a sufficiently high redshift to find potential LMCs. This is cheap to do (low resolution, and only building to a relatively low redshift). If the tree does not have an LMC we reject it and try again. If it does have an LMC, we move to the next phase. This makes it very fast to satisfy our first constraint.
2. For the next constraint, we start from the previous "just enough" tree, and grow it further (in both mass resolution and redshift) to test if it meets this next constraint. If it does, we accept the tree, if it does not, we restore to the "just enough" tree from the prior phase (so, in our example above, if we are now trying to add a GSE merger, we don't need to go through the process of finding a tree with an LMC again) and try again.

Some caveats:
1. We always need a final phase that builds out the remainder of the tree (to whatever mass resolution and redshift we want) - this is straightforward.
2. The approach works for constraints that are "non-overlapping" in a window of mass resolution and redshift, so that we can test each constraint independently. I think it can probably work (although less efficiently) even for overlapping constraints, but this needs more careful though.
3. We have to be careful about the weights assigned to trees. In the example above, it's possible that not all MW+LMC trees are equally likely to have a GSE merger. This would naturally be accounted for in the classic brute force approach (where we remake the "LMC" part of the tree on each trial), but in this approach, once we've generated the LMC part of the tree it is kept fixed until we find a GSE merger, _even if_ this particular MW+LMC tree is very unlikely to have a GSE merger. To address this, the weight of each tree is divided by the number of attempts that it took to meet each constraint at each phase.  This effectively gives us a Monte Carlo estimate of the relative likelihood of each MW+LMW tree to have a GSE merger, for example. This is something we should probably test to verify that it works reliably.

An example of this approach can be found in the `testSuite/parameters/constraintMilkyWay.xml` file, which implements the example above.

In that file we start tree building with:
```
  <mergerTreeConstructor value="build"/>
  <mergerTreeBuilder value="constrained">
    <!-- A three stage build, which builds: 1) LMC; 2) GSE; 3) everything else -->
```
which selects the `constrained` tree builder. As noted, it uses three phases. For each phase we specify a tree builder (to build the "just enough" tree) and a filter (to test if the tree meets the constraint). For the first phase:
```
    <!-- Stage 1: LMC -->
    <mergerTreeBuilder value="cole2000">
      <accretionLimit   value="0.1"/>
      <mergeProbability value="0.1"/>
      <mergerTreeBuildController value="massTimeWindow">
	<massMinimum value="1.2e11"/>
	<timeMinimum value="11.6"  />
      </mergerTreeBuildController>
    </mergerTreeBuilder>
    <mergerTreeFilter value="anyNode">
      <!-- Label as LMC -->
      <label            value="LMC"/>
      <labelDescription value="Label indicating if this node is on the LMC branch."/>
      <labelBranch      value="true"/>
       <!-- Apply all LMC conditions -->
      <galacticFilter value="all">
	<!-- Consider the main branch (i.e. Milky Way halo) of the tree only -->
	<galacticFilter value="mainBranch"/>
	<!-- Consider only halos infalling at the right time. -->
	<galacticFilter value="intervalPass">
          <nodePropertyExtractor value="time"/>
          <thresholdLow  value="11.6"/>
          <thresholdHigh value="12.0"/>
 	</galacticFilter>
	<!-- Consider only halos with a rank-2 child with a mass above 1.0e11 -->
	<galacticFilter value="childNode">
          <childRank value="2"/>
          <galacticFilter value="intervalPass">
            <nodePropertyExtractor value="massBasic"/>
            <thresholdLow  value="1.2e11"/>
            <thresholdHigh value="1.4e11"/>
          </galacticFilter>
	</galacticFilter>
      </galacticFilter>
    </mergerTreeFilter>
```
builds a tree to just enough mass resolution and redshift to allow testing for an LMC, then looks for mergers with halos in the right mass and redshift range to be an LMC (and then labels that branch fot the tree as "LMC").

In the second phase we have:
```
    <!-- Stage 2: GSE -->
    <mergerTreeBuilder value="cole2000">
      <accretionLimit   value="0.1"/>
      <mergeProbability value="0.1"/>
      <mergerTreeBuildController value="massTimeWindow">
	<massMinimum value="1.3e11"/>
	<timeMinimum value="2.8"   />
      </mergerTreeBuildController>
    </mergerTreeBuilder>
    <mergerTreeFilter value="anyNode">
      <!-- Label as GSE -->
      <label            value="GSE"/>
      <labelDescription value="Label indicating if this node is on the GSE branch."/>
      <labelBranch      value="true"/>
      <!-- Apply all GSE conditions -->
      <galacticFilter value="all">
	<!-- Consider the main branch (i.e. Milky Way halo) of the tree only -->
	<galacticFilter value="mainBranch"/>
	<!-- Consider only halos infalling at the right time. -->
	<galacticFilter value="intervalPass">
          <nodePropertyExtractor value="time"/>
          <thresholdLow  value="2.8"/>
          <thresholdHigh value="5.8"/>
 	</galacticFilter>
	<!-- Consider only halos with a rank-2 child with a mass above 1.0e11 -->
	<galacticFilter value="childNode">
          <childRank value="2"/>
          <galacticFilter value="intervalPass">
            <nodePropertyExtractor value="massBasic"/>
            <thresholdLow  value="1.3e11"/>
            <thresholdHigh value="2.5e11"/>
          </galacticFilter>
	</galacticFilter>
      </galacticFilter>
    </mergerTreeFilter>
```
which extends the LMC tree to a mass and redshift to allow us to test for a GSE merger, and then performs that test.

The final stage:
```
    <!-- Stage 3: Finalize -->
    <mergerTreeBuilder value="cole2000">
      <accretionLimit   value="0.1"/>
      <mergeProbability value="0.1"/>
      <mergerTreeBuildController value="uncontrolled"/>
    </mergerTreeBuilder>
    <mergerTreeFilter value="always"/>
```
builds the remainder of the tree.

Some notes/caveats:
1. The filters used to test if a tree meets a constraint are currently quite simple - they just check for halos in a given mass/redshift range. These could be made probabalistic, such that we could input a distribution of masses/redshifts for, e.g., the LMC, and trees would be accepted/rejected stochastically based on that probability distribution. This might be useful given that the constraints on masses/infall times are quite broad.
2. There is currently no method to ensure that these constrained halos are on reasonable orbits. This, in principle, is easy to implement. Currently orbits are assigned by drawing from a cosmological distribution. We could make a new orbit class which checks if the branch is labelled and if, for example, it finds a branch labelled "LMC" it sets some fixed orbital parameters suitable for the LMC, otherwise reverting back to sampling from a cosmological distribution. The difficultly is that constraints on orbital parameters are typically at $z=0$, not at the infall time, which is when Galacticus needs them. Two options:
    1. In some cases at least, other works have traced orbits back to the infall time, so we could use those as constraints.
    2. We could attempt, given the $z=0$ constraints on the orbit, attempt to make an estimate of the properties at infall. In principle, we know the host halo potential as a function of time, so we can just integrate backward in time to get orbital parameters at infall. This wouldn't account for any baryonic contribution to the potential (since we don't know that until we actually evolve the tree forward in time). Also, integrating backward in time when there is a dissipitative force (like dynamical friction) can be unstable - but maybe this isn't a problem here - it would just make the orbital parameters at infall more uncertain, but that's probably realistic.
3. Constraints on other properties and "negative" constraints: after each stage tree build, a `mergerTreeFilter` is applied which returns `true` or `false` depending on if the tree meets some set of criteria. Those criteria can be anything we want, including a "negative" constraint (i.e. the absence of a merger over some redshift interval). Some small caveats to the "anything we want" statement:
    1. We may need to implement specific `mergerTreeFilters` if there are very specific tests needed. Things like mass and redshift ranges are implemented, but more complicated things might need additional work. I don't expect this to be difficult though.
    2. Currently, when the filter is applied the tree is currently in a state where only the masses and redshifts of each halo have been determined - halo concentrations etc. have not yet been determined. So a filter on properties like `Vmax` would be more difficult. We can get around this in some cases by computing these quantities after each stage of build and before the filter is applied. But, some of these are computed using the full tree structure, which we don't yet have at this point. Probably this can be handled by applying a coarse-grained filter in quantities that we do have (mass, redshift), and applying a filter on Vmax etc. after the full tree is finished. This would reduce efficiency, but maybe not by too much.
	
	
## Sampling from the halo progenitor mass function

Extended Press-Schechter theory gives us the progenitor mass function (at any timestep, but usually we consider a small timestep). As shown by [Zhang, Fakhouri & Ma (2008)](https://ui.adsabs.harvard.edu/abs/2008MNRAS.389.1521Z/) an algorithm which accurately samples from this distribution function is both necessary and sufficient to get the evolution of the mass function correct across all timesteps.

The challenge is that we need to sample from the mass function with the constraint that the total mass of the halo is conserved in its progenitors. Which means that samples from the distribution function can not be independent. Extended Press-Schechter theory doesn't tell us anything about the nature of the correlations between samples.

Suppose that we decide that we want to sample $N>1$ progenitors from the distribution function. (As $N\rightarrow \infty$ this should converge in some way such that the results are independent of $N$ I think - at least for the CDM case where we have an infinite number of progenitors.) Without loss of generality we can rescale the mass of the parent halo to $M=1$. The problem of sampling the masses of these progenitors then reduces to sampling from a distribution function on the standard $N-1$ dimensional simplex such that the mean of the marginal distributions of that distribution function equals the target progenitor mass function. That is, we define a multivariate distribution function in the $N$ dimensional space of of progenitor halo masses, restricted to the region
$$
\sum_{i=1}^N m_i = 1,
$$
where the $m_i$ are the random variables corresponding to our progenitor halo masses. This restriction is to the standard simplex in $N-1$ dimensions, and guarantees mass conservation. We then have marginal distributions for each progenitor mass, $p_i(m_i)$. We combine these to find the total progenitor mass function, and require that it equals that predited by extended Press-Schechter theory
$$
\frac{1}{N}\sum_{i=1}^N p_i(m) = p_\mathrm{ePS}(m).
$$
If we can find a suitable distribution function on the $N-1$ simplex, our problem is resolved. (Although, there's no guarantee that there's a unique solution - so finding a _single_ solution might not give us the right answers for higher-order correlations and structure in the merger tree.)

There are only a few distributions defined on the simplex directly (e.g. [Dirichlet](https://en.wikipedia.org/wiki/Dirichlet_distribution), which has beta distribution marginals, but probably isn't flexible enough for our purposes), but it's possible to transform from our variables on the simplex, $(x_1 \ldots x_N)$, to a subset of real space, the so-called "center logratio transform", clr : $S^N \rightarrow U,\, U \subset \mathbb{R}^N$, i.e.:
$$
\mathrm{clr}(x) = \left[ \log \frac{x_1}{g(x)} \cdots \frac{x_N}{g(x)} \right],
$$
where $g(x) = \left(\prod_{i=1}^N x_i\right)^{1/N}$ is the geometric mean of the $x_i$ (see the Wikipedia article on [Compositional data](https://en.wikipedia.org/wiki/Compositional_data) for other [examples](https://en.wikipedia.org/wiki/Compositional_data#Linear_transformations)). Any distribution function can then be defined on this subset, $U$, of $\mathbb{R}^N$ space and mapped back to the simplex. It seems like it might be conceptually simpler to use one of the other possible transforms which map to the entirety of $\mathbb{R}^{N-1}$ - seems like this would make it easier to define a distribution function and sample from it. For example, the "additive logratio transform", alr : $S^N \rightarrow \mathbb{R}^{N-1}$ defined by:
$$
\mathrm{alr}(x) = \left[ \log\frac{x_1}{x_N} \cdots  \log\frac{x_{N-1}}{x_N} \right],
$$
might be useful. For $N=2$ this is, of course, just the real line, and a trivial remapping of the extended Press-Schechter progenitor mass function, $p_\mathrm{ePS}(x_1,x_2)$, to the variable $y=\log x_1/x_2 = \log x_1/(1-x_1)$, such that
$$
p(y) = x_1 (1-x_1) p_\mathrm{ePS}(x_1,x_2).
$$

The question then is whether we can find a distribution function on $U$ or $\mathbb{R}^N$ which reproduces the progenitor mass function from extended Press-Schechter theory. It seems like looking at N-body results might be helpful here - it would be possible to construct the distribution on $U$ or $\mathbb{R}^N$ using N-body data and look for plausible functional forms. Although, a challenge might be that the N-body data doesn't probe masses below the resolution scale - for large $N$ presumably most of the progenitors are very low mass. Instead all we would have is some constraint on the integral of the distribution function below the resolution scale.
