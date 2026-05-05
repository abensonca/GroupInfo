###### status: `active` · last reviewed: TBD

###### tags: `dark matter` `fuzzy dark matter`

### FDM Halo Modeling Framework
1. **Concentration-mass relation** (**finished**)
Another fitting formula: Eq. (12) in [Laroche et al. 2022](https://ui.adsabs.harvard.edu/abs/2022MNRAS.517.1867L/abstract)
2. **Density profile** (**finished**)
(soliton core + NFW-like envelope)
[Schive et al. 2014](https://ui.adsabs.harvard.edu/abs/2014PhRvL.113z1302S/abstract) establish the universal soliton and the core–halo picture; companion works confirm the two-component structure in cosmological SP runs.
See also [Veltmaat et al. 2018](https://ui.adsabs.harvard.edu/abs/2018PhRvD..98d3509V/abstract) for zoom-in confirmations.
3. **Core–halo relation** (**finished**)
Compute core mass using Eq. (15) and core radius using Eq. (14) from [Chan et al. 2022](https://ui.adsabs.harvard.edu/abs/2022MNRAS.511..943C/abstract).
Adopt Eq. (3) from [Schive et al. 2014](https://ui.adsabs.harvard.edu/abs/2014PhRvL.113z1302S/abstract) to get the soliton normalization $\rho_\mathrm{c}$.
Set the transition radius $r_\mathrm{sol}$ by solving $\rho_\mathrm{sol}=\rho_\mathrm{NFW}(r)$.
4. **Tidal heating/stripping of soliton cores** (**finished**)
Compute the core mass loss rate using Eq. (17) from [Du et al. 2018](https://ui.adsabs.harvard.edu/abs/2018PhRvD..97f3507D/abstract), where $Im(E)$ is given by Eq. (7). If the density ratio ($\mu=\rho_c/\rho_\mathrm{host}$) is larger than 300, set $\mu=300$.
(**todo**) [Yang et al. 2025](https://ui.adsabs.harvard.edu/abs/2025arXiv250701686Y/abstract): Shows that realistic Milky Way tides (including the LMC) suppress FDM-induced stellar heating in dwarf satellites by stripping the outer halo and weakening granule perturbations.
5. **Tidal heating for solitonic core and NFW-like envelope** (**finished**)
apply the usual CDM tidal heating/stripping to the NFW-like envelope.
Inside the soliton, evolve $M_\mathrm{c}$, $r_\mathrm{c}$ and $\rho_\mathrm{c}$ with an SP-calibrated tidal mass-loss law from [Du et al. 2018](https://ui.adsabs.harvard.edu/abs/2018PhRvD..97f3507D/abstract).
6. **Core–core merger rule** (**finished**)
See Page 7-8 in [Schwabe et al. 2016](https://ui.adsabs.harvard.edu/abs/2016PhRvD..94d3513S/abstract) (SP-calibrated).
**Two cases that subhalo and host halo will merge**:
* When the subhalo satisfies $M_\rm{c,current}<1.0\times 10^{-3}$$M_\rm{c,initial}$, it is assumed to be merged with the host halo.
* $D<r_\rm{c,host}+r_\rm{c,sub}$
**How to calculate the $M_\rm{c,final}$ after merging?**
* A simple method: The mass of the emerging core is approximately 70% of the sum of the progenitors’ core masses.
* If we can calculated the total energy of the subhalo and the host halo, the following calculation is better.
The final core mass can be calculated based on Eq. (18) for mass ratio $\mu > 1$ and Eq. (19) for $\mu = 1$ in [Schwabe et al. 2016](https://ui.adsabs.harvard.edu/abs/2016PhRvD..94d3513S/abstract).
See also [Mina et al. 2022](https://ui.adsabs.harvard.edu/abs/2022A%26A...662A..29M/abstract) for simulation results, without analytic solution.
7. **Strong quasi-normal oscillations** (**todo**)
The core–halo relation (e.g., [Schive et al. 2014](https://ui.adsabs.harvard.edu/abs/2014PhRvL.113z1302S/abstract); [Chan et al. 2022](https://ui.adsabs.harvard.edu/abs/2022MNRAS.511..943C/abstract)) provides ensemble-/time-averaged, quasi-equilibrium values of $M_\mathrm{c}$ and $r_\mathrm{c}$ at fixed $(M_\mathrm{h}, z)$, with an intrinsic scatter capturing halo-to-halo variability.
This module accounts for:
* quasi-normal oscillations of the core’s density/phase
From the right panel of Figure 2 in [Dutta Chowdhury et al. 2021](https://ui.adsabs.harvard.edu/abs/2021ApJ...916...27D/abstract), the oscillations of the soliton's central density $\rho_0$ are related to the characteristic frequency given by Eq. (4).
* stochastic centroid drift driven by interference (“granule”) fluctuations in the host.
In addition to the oscillations of the central density, the soliton also exhibits stochastic fluctuations in its centroid position relative to the halo center of mass, shown in Figure 5 in [Dutta Chowdhury et al. 2021](https://ui.adsabs.harvard.edu/abs/2021ApJ...916...27D/abstract). Such centroid motions directly affect the orbital trajectories of nearby particles, but their contribution is subdominant compared to the effect of granule fluctuations.
See [Veltmaat et al. 2018](https://ui.adsabs.harvard.edu/abs/2018PhRvD..98d3509V/abstract) and [Hui 2021](https://ui.adsabs.harvard.edu/abs/2021ARA%26A..59..247H/abstract).
8. **Baryon-driven growth/compression of FDM cores** (**todo**)
[Veltmaat et al. 2020](https://ui.adsabs.harvard.edu/abs/2020PhRvD.101h3518V/abstract)
7. **Halo mass function for FDM** (**todo**)
The FDM halo mass function (HMF) requires a mass-dependent collapse barrier to account for suppression of small-scale structure.
- Standard approaches (e.g., applying Sheth–Tormen to a cut-off power spectrum) underestimate the cutoff mass and redshift dependence.
- [Du et al. 2017 ](https://ui.adsabs.harvard.edu/abs/2017MNRAS.465..941D/abstract) solved the excursion set problem with a moving barrier calibrated to FDM linear growth. In this paper, they used Plank 2015 parameters and top-hat filter.
- The mass-dependent collapse barrier is defined by Eq. (9):
$$\delta_c^\rm{fdm} = G(M)\delta_c^\rm{cdm},$$
where $\rm{G}(M)$ is given by Eq.(11), which was obtained by computing the FDM linear growth factor with AxionCAMB and then fitting the numerical results with a convenient analytic expression. They converted $\rm{G}(k)$ to $\rm{G}(M)$ by introducing the Jeans-like mass $M_\rm{J}$ as the characteristic scale separating suppressed and unsuppressed modes.
- First-crossing distribution:
For FDM, the collapse barrier is mass-dependent, so the first-crossing distribution $f(S)$ cannot be solved analytically.  
[Du et al. 2017 ](https://ui.adsabs.harvard.edu/abs/2017MNRAS.465..941D/abstract) computed $f(S)$ numerically using the mid-point rule discretization, leading to the recursion formula Eq. (A3) (see details in Appendix A).
- All of the above steps finally lead to the halo mass function:
$$\frac{dn}{d\ln M} = -\frac{\bar\rho}{M}\, f(S)\, \frac{dS}{d\ln M},$$
where $S=\sigma^2(M)$ is the variance of the smoothed density field, given by Eq. (2).
- Compared to CDM, the FDM HMF predicts a stronger small-mass cutoff and weaker redshift dependence of the suppression.
10. **Granule Perturbations on Orbital Motion** (**todo**)
In our modeling framework, the orbital diffusion of a tracer can be decomposed into two parts: a random walk relative to the soliton center (driven by granule fluctuations), plus the stochastic drift of the soliton centroid itself. When expressed relative to the halo center of mass, the resulting particle trajectory reflects the combination of these two contributions. It can be seen in Figure 6 in [Dutta Chowdhury et al. 2021](https://ui.adsabs.harvard.edu/abs/2021ApJ...916...27D/abstract), the green and orange lines.

### Simulation Data for Comparison
1. **density profile**
Figure 1 in [Schive et al. 2014](https://ui.adsabs.harvard.edu/abs/2014PhRvL.113z1302S/abstract)
Figure 3 in [Chan et al. 2022](https://ui.adsabs.harvard.edu/abs/2022MNRAS.511..943C/abstract)
Figure 13 in [May&Springel2021](https://academic.oup.com/mnras/article/506/2/2603/6308377)
Figure 2 in [Veltmaat et al. 2020](https://ui.adsabs.harvard.edu/abs/2020PhRvD.101h3518V/abstract)
2. **velocity profile**
Figure 2 and 3 in [Liao et al. 2025](https://ui.adsabs.harvard.edu/abs/2025PhRvL.135f1002L/abstract)
3. **concentration-Mass relation**
Figure 3 in [Liao et al. 2025](https://ui.adsabs.harvard.edu/abs/2025PhRvL.135f1002L/abstract)
4. **core-Mass relation**
$r_\rm{c}$-$M_\rm{c}$, $M_\rm{c}$-$M_\rm{h}$ or $r_\rm{c}$-$M_\rm{h}$:
Figure 2, 5 and 7 in [Chan et al. 2022](https://ui.adsabs.harvard.edu/abs/2022MNRAS.511..943C/abstract)
$M_\rm{soliton}$-$M_\rm{h}$: Figure 1 in [Liao et al. 2025](https://ui.adsabs.harvard.edu/abs/2025PhRvL.135f1002L/abstract)
$r_\rm{sol}/r_\rm{c}$-$M_\rm{h}$: Figure 4 in [Chan et al. 2022](https://ui.adsabs.harvard.edu/abs/2022MNRAS.511..943C/abstract)
5. **Evolution of velocity dispersion**
Figure 4 in [Veltmaat et al. 2020](https://ui.adsabs.harvard.edu/abs/2020PhRvD.101h3518V/abstract)
It can also be calculated from [Liao et al. 2025](https://ui.adsabs.harvard.edu/abs/2025PhRvL.135f1002L/abstract).
6. **Evolution of the core mass**
Figure 5 in [Veltmaat et al. 2020](https://ui.adsabs.harvard.edu/abs/2020PhRvD.101h3518V/abstract)
7. **Evolution of the central density**
Figure 6 in [Veltmaat et al. 2020](https://ui.adsabs.harvard.edu/abs/2020PhRvD.101h3518V/abstract)
Figure 5 in [Schwabe&Niemeyer2022](https://ui.adsabs.harvard.edu/abs/2022PhRvL.128r1301S/abstract)
8. **soliton random walk**
distance of the soliton center from the halo center as a function of time: Figure 11 in [Li et al. 2021](https://link.aps.org/accepted/10.1103/PhysRevD.103.023508)
9. **Halo Mass Function**
Figure 12 in [May&Springel2021](https://academic.oup.com/mnras/article/506/2/2603/6308377)
Figure 2 in [Elgamal et al. 2023](https://ui.adsabs.harvard.edu/abs/2024MNRAS.532.4050E/abstract)
10. **Power Spectra**
Power Spectra (linear and non-linear)
Evolution of $P_\rm{FDM}(k,z)$/$P_\rm{CDM}(k,z)$
[May&Springel2021](https://academic.oup.com/mnras/article/506/2/2603/6308377)
11. **tidal heating**
12. **halo mergers**


### Simulations beyond FDM-only
* FDM with baryons
[Veltmaat et al. 2020](https://ui.adsabs.harvard.edu/abs/2020PhRvD.101h3518V/abstract)
* mixed FDM and CDM
[Lague et al. 2024](https://ui.adsabs.harvard.edu/abs/2024PhRvD.109d3507L/abstract)


### Cosmological Simulation Codes for FDM
For the comparison items listed above, AxioNyx (full-wave or mixed-DM) and GAMER-2 ($\psi$DM) are the most suitable choices if one wishes to run simulations. AX-GADGET, PyULtraLight and SCALAR are not open source codes.
1. [AxioNyx](https://github.com/axionyx/axionyx_1.0) (AMR Schrödinger–Poisson; FDM-only or mixed FDM+CDM). It can be used to simulate a wave-function DM component (and optionally CDM) in cosmological volumes; used to produce density slices, non-linear $P(k)$, and halo statistics (e.g., HMF).
2. [GAMER-2](https://github.com/gamer-project/gamer/releases?utm_source=chatgpt.com) (GPU-accelerated AMR; $\psi$DM/FDM module). General AMR code with official release notes listing Fuzzy dark matter (FDM/$\psi$DM) support. Suited for high-resolution boxes and zoom-ins. It is commonly used to analyze soliton–halo structure and subhalo evolution.
3. AX-GADGET (P-GADGET3 module; quantum-pressure approximation). Efficient for large-volume statistics (non-linear P(k), HMF) where a QP term approximates wave effects. It is not a full wave solver.
4. PyUltraLight (Python pseudo-spectral SP solver).
5. SCALAR (RAMSES-based AMR SP solver). Full wave solver on adaptive meshes.

### Notes on density profile:
If we consider a FDM halo, whose virial mass is defined as:
$$M_h = (4\pi x_{vir}^3/3)\zeta(z)\rho_m0$$
Its core-halo mass relation is given by:
$$M_c = \frac{1}{4}a^{-1/2}(\frac{\zeta(z)}{\zeta(0)})^{1/6}(\frac{M_h}{M_{min,0}})^{1/3}M_{min,0}$$ (Eq. 6 in [Schive2014](https://ui.adsabs.harvard.edu/abs/2014PhRvL.113z1302S/abstract)),
where $M_{min,0} = 375^{-1/4}32\pi\zeta(0)^{1/4}\rho_{m0}(H_0m_\psi/\hbar)^{-3/2}\Omega_{m0}^{-3/4}$. 
Its core radius is given by:
$$(\frac{1.6}{m_{22}})a^{1/2}(\frac{\zeta_z}{\zeta_0})^{-1/6}(\frac{M_h}{10^9\,M_\odot})^{-1/3}.$$ (Eq. 7 in Schive2014)
Here $m_{22} = m_\psi/10^{-22}eV$ and we define $\zeta(\Omega_m) = (18\pi^2+82(\Omega_m-1)-39(\Omega_m-1)^2)/\Omega_m$.
The concentration-mass relation here we use is given by Eq.6 from [Gao2008](https://ui.adsabs.harvard.edu/abs/2008MNRAS.387..536G/abstract),
$$\log_{10}(c_{200}) = A\log_{10}(M_{200}) + B,$$
where A and B is given by Table 1.