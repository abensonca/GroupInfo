# Subhalo Tidal Tracks Model

###### tags: `dark matter` `subhalos`

# Overview

As subhalos lose mass due to tidal stripping their structure evolves in a way that follows a so-called "tidal track" which seems to be independent of the details of the mass loss and depends only on the total mass lost (first shown by [Peñarrubia et al. (2008)](https://ui.adsabs.harvard.edu/abs/2008ApJ...673..226P)).

A modern example of this from [Errani & Navarro (2020)](https://ui.adsabs.harvard.edu/abs/2021MNRAS.tmp.1267E/abstract). Simulations with different pericenteric radii (colored points) all fall along the same tidal track (dashed line).

![](https://i.imgur.com/FCSDbSE.png)

# Tidal Heating Model

To capture this behavior in Galacticus we make use of a tidal heating model, which is described in detail in [Pullen et al. (2014)](https://ui.adsabs.harvard.edu/abs/2014ApJ...792...24P/abstract), and is based on the model first proposed by [Taylor & Babul (2001)](https://ui.adsabs.harvard.edu/abs/2001ApJ...559..716T/abstract).

Briefly, it is assumed that each spherical shell of matter in the halo receives some heating (i.e. energy added by tidal effects), corresponding to a change in specific energy of $\Delta \epsilon$. The shell responds by expanding. Under the assumption of no shell crossing the final radius, $r_\mathrm{f}$, of the shell is related to its initial radius, $r_\mathrm{i}$, by
$$
\Delta\epsilon = \frac{\mathrm{G}M_\mathrm{i}}{r_\mathrm{i}}-\frac{\mathrm{G}M_\mathrm{i}}{r_\mathrm{f}}
$$
where $M_\mathrm{i}$ is the mass contained within the shell.

To predict the resulting density profile then we need to compute $\Delta \epsilon (r_\mathrm{i})$.

## Original Tidal Heating Model

Our original tidal heating model largely follows that of [Taylor & Babul (2001)](https://ui.adsabs.harvard.edu/abs/2001ApJ...559..716T/abstract) and assumes
$$
\Delta\dot{\epsilon}(r) = \frac{\epsilon_\mathrm{h}}{3} \left[1+(\omega_\mathrm{p} T_\mathrm{shock})\right]^{-\gamma} r^2 g_{ab} G_{ab}
$$
where $\epsilon_\mathrm{h}$ is a normalization coefficient, $\omega_\mathrm{p}$ is the angular frequency of particles at the half mass radius of the satellite, $T_\mathrm{shock}$ is the shock time-scale, $g_{ab}$ is the tidal tensor, and $G_{ab}$ is the time integral of that tensor.

This result is derived from the work of [Gnedin, Hernquist, & Ostriker (1997)](https://ui.adsabs.harvard.edu/abs/1999ApJ...514..109G/abstract), but accounts only for the first-order perturbation to the energies of subhalo particles. However, the second-order perturbation is known to be of comparable magnitude to the first-order perturbation [Spitzer (1987)](https://ui.adsabs.harvard.edu/abs/1987degc.book.....S/abstract). (Higher order terms are negligble.) 

[Pullen et al. (2014)](https://ui.adsabs.harvard.edu/abs/2014ApJ...792...24P/abstract) assume that the second-order effect can be accounted for by effectively rolling it in to the normalization parameter $\epsilon_\mathrm{h}$. While this seems to work reasonably well for the overall evolution (i.e. total mass loss), as shown by [Yang et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020MNRAS.498.3902Y/abstract), it does not produce the correct tidal track.

For example, in the following figure we reproduce the subhalo-host system simulated by [Errani & Navarro (2020)](https://ui.adsabs.harvard.edu/abs/2021MNRAS.tmp.1267E/abstract) using our original tidal heating model.

![](https://i.imgur.com/E7DBoNH.png)

The black dashed line is the tidal track found by [Errani & Navarro (2020)](https://ui.adsabs.harvard.edu/abs/2021MNRAS.tmp.1267E/abstract), while the solid red line is the result from out model. Clearly our model does not produce the correct tidal track.

## New Tidal Heating Model

We attempt to improve this model by explicitly accounting for the second-order perturbation to subhalo particle energies. Using the results from [Gnedin, Hernquist, & Ostriker (1997)](https://ui.adsabs.harvard.edu/abs/1999ApJ...514..109G/abstract) we now write:
$$
\Delta\epsilon(r) = \Delta \epsilon_1 (r) + \sqrt{2} f_2 (1-\chi_\mathrm{v}) \sqrt{\Delta \epsilon_1(r) \sigma^2_\mathrm{r}(r)}
$$
where $\Delta \epsilon_1(r)$ is the first-order term from the original model, $\chi_\mathrm{v}$ is the position-velocity correlation coefficient introduced by [Gnedin, Hernquist, & Ostriker (1997)](https://ui.adsabs.harvard.edu/abs/1999ApJ...514..109G/abstract), $\sigma_\mathrm{r}(r)$ is the radial velocity dispersion in the subhalo (prior to any tidal heating), and $f_2$ is a new coefficient introduced to allow us to calibrate the strength of the second-order term. [Gnedin, Hernquist, & Ostriker (1997)](https://ui.adsabs.harvard.edu/abs/1999ApJ...514..109G/abstract) find that $\chi_\mathrm{v}$ depends weakly on the density profile - we fix it at $\chi_\mathrm{v}$ (typical of the values that they found). This choice does not matter too much as the effect of $\chi_\mathrm{v}$ is degenerate with that of $f_2$.

The dependence on $\sigma_\mathrm{r}(r)$ in the second-order term gives it a different radial dependence than the first-order term. This changes the radial heating profile - generally boosting the heating at smaller radii relative to the original model.

I then calibrate the value of $f_2$ by running calculations matched to the system simulated by [Errani & Navarro (2020)](https://ui.adsabs.harvard.edu/abs/2021MNRAS.tmp.1267E/abstract) for different ratios of pericentric to apocentric radius ($r_\mathrm{p}/r_\mathrm{a}=0.05, 0.10, 0.20$). Optimal matching is obtained for $f_2=0.406$, resulting in the tidal track shown below.

![](https://i.imgur.com/4peVn2f.png)

## Finite Resolution Effects

With this model for tidal heating validated and calibrated the next step is to examine the effects of a finite resolution (in length and/or mass) in N-body simulations on the evolution of the tidal track. [Errani & Navarro (2020)](https://ui.adsabs.harvard.edu/abs/2021MNRAS.tmp.1267E/abstract) run some simulations to explore this where they vary the properties of a single subhalo orbiting in a host potential.

I recreated their initial conditions in Galacticus, and introduced a finite radius core into the dark matter profile of the subhalo. Specifically, the density profile is given by:
$$
 \rho(r) = \rho^\prime(r) \left( 1 + \left[ \frac{\Delta x}{r} \right]^2 \right)^{-1/2},
$$
where $\Delta x$ is the larger of the resolution length, `[lengthResolution]`, and the radius in the original profile enclosing the mass resolution, `[massResolution]`.

I then attempt to calibrate the choice of the `[lengthResolution]` and `[massResolution]` parameters by matching the results of the [Errani & Navarro (2020)](https://ui.adsabs.harvard.edu/abs/2021MNRAS.tmp.1267E/abstract) simulations.

I assume that `[lengthResolution]`$=\epsilon \Delta x$ and `[massResolution]`$=N m_\mathrm{p}$ where $\Delta x$ here is the resolution length of the simulation ([Errani & Navarro (2020)](https://ui.adsabs.harvard.edu/abs/2021MNRAS.tmp.1267E/abstract) use a grid-based approach - for non-grid approach the softening length would be the natural choice), $m_\mathrm{p}$ is the particle mass, and $\epsilon$ and $N$ are parameters to be calibrated.

I find that $\epsilon=0.23$ and $N=36$ give the best fits to the results of [Errani & Navarro (2020)](https://ui.adsabs.harvard.edu/abs/2021MNRAS.tmp.1267E/abstract). Plots of the tidal track evolution are shown below. The number of particles and length resolution are shown in each plot title. The dashed black line is the fit to the tidal track for well-resolved halos from [Errani & Navarro (2020)](https://ui.adsabs.harvard.edu/abs/2021MNRAS.tmp.1267E/abstract). The vertical dotted line shows $2\Delta x$. The blue points are N-body results from [Errani & Navarro (2020)](https://ui.adsabs.harvard.edu/abs/2021MNRAS.tmp.1267E/abstract), and the red line is from our model including the finite-resolution core. This line is solid for regions where the bound mass of the subhalo is great than $10 m_\mathrm{p}$ and is dashed for regions where the bound mass is less than this.

![](https://i.imgur.com/7jzjUS1.png)
![](https://i.imgur.com/AhMVyz0.png)
![](https://i.imgur.com/wVGLzSE.png)
![](https://i.imgur.com/kvcMuU3.png)
![](https://i.imgur.com/dsf26uR.png)

### Finite Resolution Effects in the Caterpillar Simulations

Using this model for tidal tracks I have run realizations of the Caterpillar LX14 suite of halos using Galacticus - once with infinite resolution (i.e. pure NFW halos for the subhalos prior to tidal heating), and once including the finite resolution core as described above utilizing the Caterpillar LX 14 particle mass ($2.9854 \times 10^4 \mathrm{M}_\odot$) and softening length (76 pc comoving) and the best-fit calibration described above.

The following figure shows the results radial distribution of subhalos (normalized to the host halo virial radius) for both infite ("NFW") and finite ("cored") resolution cases, for four different subhalo mass thresholds.

![](https://i.imgur.com/KYhVZGF.png)

Two clear trends are seen:
1. The effects of finite resolution are neglible at the highest masses shown ($10^8\mathrm{M}_\odot$, corresponding to around 3,300 particles), but become much more significant for the lowest mass sample of subhalos shown ($3\times 10^6\mathrm{M}_\odot$, corresponding to around 100 particles).
2. The effect of finite resolution becomes larger at smaller radii. For the $3\times 10^6\mathrm{M}_\odot$ sample the reduction in the number of subhalos is about a factor 1.8 at 10% of the virial radius and a factor 2.8 at 2% of the virial radius.

A good rule of thumb might be that to get accurate subhalo statistics at 1% of the virial radius you need to at least 1,000 particles per subhalo. Note that this is just to get global properties (e.g. subhalo mass) correct - most likely getting the details of internal structure (e.g. $V_\mathrm{max}$) would require more particles.

## Extension to Profiles Other Than NFW

Ideally we'd like to apply this model to cases other than NFW profiles (e.g. cored profiles that occur in SIDM models).

In exploring this there are two challenges that occur:
1. In some cases shell-crossing can occur;
2. The parameter $f_2$ must be adjusted for different profiles to get a good fit.

For the first of these we modify the model to avoid shell crossing by considering the perturbation parameter:
$$
\xi = \frac{\epsilon}{\mathrm{G}M/r}.
$$
We force this perturbation parameter to be a monotonically-increasing function of radius, such that the heated density profile can not make the slope of the density profile shallower (or, therefore, have a hole in the center) than the original, unheated profile. This is an empirical modification, but I think of it as saying that in the shell-crossing region the shells cross repeatedly, exchange energy, and homegenize this perturbation. Practically, this condition is enforced by tabulating the perturbation profile, then stepping inward looking for cases where the perturbation, $\xi$, is larger than in the previous (outer) shell, and in such cases reducing $\xi$ to enforce monotonicity. As a result of this, we tabulate the entire mass profile and use that tabulation to derive the density profile (and everything else about the mass distribution).

For the second issue my interpretation is as follows. The $f_2$ parameter controls the strength of the second-order term in the heating energy. This second order term represents the increase in the dispersion of energies in the shell. The effect of this increase in *dispersion*, modeled through our simple approach where the rms value of the increase is simply added to the first order term, will depend on the shape of the distribution function. Therefore, we make $f_2$ a function of the slope of the (unheated) density profile. Specifically, we choose
$$
f_2(\alpha) = a_0 + a_1 \alpha,
$$
where $\alpha$ is the logarithmic slope of the density profile and $a_0$ and $a_1$ are parameters to be constrained.

To constrain these parameters I run simulations using density profiles with a range of inner slopes (specifically, I use the [Zhao et al. (1996)](https://doi.org/10.1093/mnras/278.2.488) profile with NFW-like outer profile and varying inner slope, $\gamma$) matched to those run by [Penarrubia et al. (2010)](https://doi.org/10.1111/j.1365-2966.2010.16762.x), and then optimize the free parameters to match the tidal tracks reported by [Penarrubia et al. (2010)](https://doi.org/10.1111/j.1365-2966.2010.16762.x). Specifically, I fit to the cases $\gamma = 0.0, 0.5, 1.0$ from [Penarrubia et al. (2010)](https://doi.org/10.1111/j.1365-2966.2010.16762.x).

I find optimal values $(a_0,a_1) = (+0.03,-0.32)$. Results for these are shown below.

### Models with Monotonicity in the Perturbation, $\xi$, Enforced

#### Inner slope: $\gamma=0.0$

![](https://i.imgur.com/9tTczkD.png)

#### Inner slope: $\gamma=0.5$

![](https://i.imgur.com/iNCYflA.png)

#### Inner slope: $\gamma=1.0$

![](https://i.imgur.com/dxdFUaj.png)

#### Inner slope: $\gamma=1.5$

This case was not used in constraining the parameters. I have not been able to reproduce the [Penarrubia et al. (2010)](https://doi.org/10.1111/j.1365-2966.2010.16762.x) tidal track for $\gamma=1.5$. This could be a failure of our tidal heating model, but could (I guess) also be a failing of the [Penarrubia et al. (2010)](https://doi.org/10.1111/j.1365-2966.2010.16762.x) simulations being unable to fully resolve such a cuspy profile. In any case, given that in our model at small radii the heating is dominated by $\epsilon_2 \propto r$ (ignoring any $\sigma$ dependence), while in this profile $\mathrm{G}M/r \propto r^{1/2}$ it becomes extremely difficult to significantly perturb the inner regions of this profile.

![](https://i.imgur.com/kk4gz4w.png)

### Models without Monotonicity in the Perturbation, $\xi$, Enforced

#### Inner slope: $\gamma=0.0$

The effects of shell crossing are very visible here.

![](https://i.imgur.com/2hg4PXd.png)

#### Inner slope: $\gamma=0.5$

![](https://i.imgur.com/zBlmdak.png)

#### Inner slope: $\gamma=1.0$

![](https://i.imgur.com/BfkJnUg.png)

#### Inner slope: $\gamma=1.5$

![](https://i.imgur.com/V0mgbjD.png)
