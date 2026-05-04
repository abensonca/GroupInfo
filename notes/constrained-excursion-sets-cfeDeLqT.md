# Constrained Excursion Sets

###### tags: `dark matter`, `merger trees`

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

## Ethan Notes 9/15/21

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

### Outdated original notes

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

#### Comparison to [Beghin & Orsingher (1999)](https://www.academia.edu/3480026/On_the_maximum_of_the_generalized_Brownian_bridge)

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


## Negative Assertion in the Excursion Set Approach

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

## Constraining on the presence of the LMC

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

## Limitations of the Brownian bridge solver approach

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

## Notes 11/26/2023

Generate unconstrained trees. Select those branches that meet a constraint. Look at distribution of trajectories. Figure out how to modify branching rate to match that - using Brownian bridge solution as a guide.

Maybe also look at other branches in those trees - do they still follow the regular solution statistics?

## Notes from 06/17/2024

In the current Brownian bridge approach, we build a trajectory back to the time of interest, $\delta_2$, and then insert a jump to our required halo of variance $S_2$. The crucial aspect of this is that the distribution of parent halo masses at $\delta_2-\epsilon$ must be an unbiased sample of those we would get by simply filtering trees to match our constraint.

The Brownian bridge approach ensures that we get a progenitor at $\delta_2-\epsilon$ which has $S < S_2$. Using the reflection principle we can then assert a merger to $(S_2,\delta_2)$ from our Brownian bridge. _But_, this ignores the fact that there will also be trajectories from $(S<S_2,\delta_2-\epsilon)$ which _do not_ cross the barrier at $S_2$ but are below it (and always below it). So, I think we should weight trees by:
$$
p(S_2,\delta_2|S,\delta_2-\epsilon) / p(S_2,<\delta_2|S,\delta_2-\epsilon)
$$
where, for trajectories starting from $(S,\delta_2-\epsilon)$, the numerator is the probability to make a first upcrossing at $(S_2,\delta_2)$, and the denominator is the probability for the trajectory to be below $\delta_2$ at $S_2$ having never crossed the barrier between $S$ and $S_2$ (a similar calculation is performed in the usual numerical calculation of the first crossing solution).