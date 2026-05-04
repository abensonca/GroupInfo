# Sampling from the halo progenitor mass function

###### tags: `dark matter` `merger trees`

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