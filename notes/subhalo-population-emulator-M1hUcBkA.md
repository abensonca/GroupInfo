# Subhalo Population Emulator

###### status: `active` · last reviewed: TBD

###### tags: `dark matter` `subhalos` `merger trees`

## Extension to WDM

(Or, really to any models with some "hidden" parameter.)

For our current, CDM emulator we describe subhalos by six parameters, $x_{1\ldots6}$. Galacticus predicts some joint distribution function over this 6D parameter space, $p(x_{1\ldots6})$. We train a normalizing flow to map that distribution function into a 6D standard multivariate normal distribution, $\mathcal{N}(x^\prime_{1\ldots6})$, from which we can sample rapidly (and then reverse the mapping to recover a sample from the distribution on the orignial parameter space).

Suppose that we now want to emulate WDM, where we have some parameter $m_\mathrm{WDM}$ that describes the particle properties of dark matter (and the limit $m_\mathrm{WDM}\rightarrow \infty$ corresponds to the CDM case).

We can run Galacticus for a bunch of different values of $m_\mathrm{WDM}$ (either some uniform distribution, or randomly sampled values). Then, let's treat $m_\mathrm{WDM}$ as a $7^\mathrm{th}$ variable in our model parameter space. Galacticus can now be thought of as predicting the distribution function, $p(x_{1\ldots6},m_\mathrm{WDM})$. Note that the distribution along the $m_\mathrm{WDM}$ direction is going to depend on how we chose which values of $m_\mathrm{WDM}$ to evaluate at. But, it will turn out that doesn't matter - since we're going to construct a way to choose whatever specific value of $m_\mathrm{WDM}$ that we want.

Now we train a new normalizing flow on this 7D distribution function. But, for this normalizing flow, we make the distribution function in the latent space a combination of the original 6D standard multivariate normal, and a uniform distribution in the new dimension, $\mathcal{N}(x^\prime_{1\ldots6}) U(x^\prime_7)$.

Then, define the loss function as a combination of the usual log-likelihood, plus a constraint that will force $x^\prime_7 = m_\mathrm{WDM}$. (Or, any bijective mapping from $m_\mathrm{WDM}$ to $x^\prime_7$ - all we care about here is that we can choose some value of m_\mathrm{WDM}$ and know what the corresponding value of $x^\prime_7$ will be. So, we could, for example, use $x^\prime_7 = m_\mathrm{WDM}/m_\mathrm{max}$ where $m_\mathrm{max}$ is the largest WDM particle mass we consider, or $x^\prime_7 = \log(m_\mathrm{WDM}/m_\mathrm{max})$, etc.). So, something like:
$$
\sum_{i=1}^N \log \mathcal{L}_i + \sum_{i=1}^N (m_{\mathrm{WDM},i - x^\prime_{7,i}})^2/\sigma^2
$$
where here $\sigma$ is some parameter that controls how strong the constraint to make $x^\prime_7 = m_\mathrm{WDM}$ is - the smaller we make $\sigma$ the more the loss function should push the emulator toward this condition. But, we don't want to make $\sigma$ too small such that the original likelihood condition becomes overwhelmed. So, some testing will be required here.

Once we have a trained emulator that behaves in this way we can generate a population of subhalos for any given $m_\mathrm{WDM}$. We simply first find the corresponding $x^\prime_7$ - this is now fixed for all subhalos in the population that we want to create. We then sample $x^\prime_{1\ldots6}$ as usual from the multivariate normal. We now have $x^\prime_{1\ldots7}$ so we just feed these in to the emulator inverse to get the corresponding sampled point from the original parameter space. Because we enforced the emulator to have $x^\prime_7 = m_\mathrm{WDM}$ that means the inverse must have $m_\mathrm{WDM} = x^\prime_7$. So, we should get, for every emulated point, our targetted value of $m_\mathrm{WDM}$, and a set of parameters $x_{1\ldots6}$ for the subhalo consistent with being drawn from the original distribution function, conditioned on $m_\mathrm{WDM$}$, i.e. $p(x_{1\ldots6},m_\mathrm{WDM}|m_\mathrm{WDM})$, which is what we wanted. (Technically there will be some small variation around the target $m_\mathrm{WDM}$ which should scale with the value of $\sigma$ in our loss function - so we can tune how close we want the match to be.)

Qualitatively, we want to be able to take a slice through the 7D distribution function predicted by Galacticus at some fixed $m_\mathrm{WDM}$ and sampled from the conditioned 6D distribution function. The problem with a standard normalizing flow is that we sample in the latent space, and in that space the simple slice along the $m_\mathrm{WDM}$ dimension corresponds to some complicated, distorted 6D volume which would be impossible to sample from. In what's described above we're essentially putting another constraint on the normalizing flow, forcing it to make the slices in $m_\mathrm{WDM}$ also correspond to simple slices along one dimension in the latent space also - and then we can trivially sample from those.
