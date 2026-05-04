# Subhalo Orbits Model Papers

###### tags: `dark matter`

## Overview

An accurate and physical model for the evolution of dark matter substructure is crucial for predicting the abundance and spatial distribution of dark matter subahloes within their massive hosts. While N-body simulations are widely used to study the statistics of subhales in different dark matter scenarios, semi-analytic models are useful tools for fast generating a large number of realizations. By comparing existing and new models to a large set of high-resolution idealized N-body simulations, we carefully examining each physical effect presented in the evolution of dark matter sub-haloes and calibrate the free parameters in the models.

## Paper 1: Orbital evolution

[Link to paper on Overleaf](https://www.overleaf.com/3567158855ykjsrbxvznpp)

### Outline

In this work, we will focus on the orbital evolution of sub-haloes. In additional to the classical Chandrasekhar dynamical friction, we present a detailed study of the self-friction effect originated from matters striped away from the subahloes and propose a new model to describe the extra orbital decay due to this effect.

The classical dynamical friction effect is described by the Chandrasekhar formula

\begin{equation}
\textbf{a}_{\text{df}}=-4\pi G^2 \ln\Lambda M_{\text{sat}}\rho_{\text{host}}(r_{\text{sat}})\dfrac{\textbf{V}_{\text{sat}}}{V_{\text{sat}}^3}
\left[{\rm erf}(X_v)-\dfrac{2X_v}{\sqrt{\pi}}\exp(-X_v^2)\right],
\end{equation}
where $r_{\text{sat}}$ is the sub-halo position within the host, $X_v=V_{\text{sat}} / \sqrt{2}\sigma_v$ with $\sigma_v$ the velocity dispersion of DM particles in the host.

When a sub-halo evolves in its host halo, the particles outside the tidal radius is gradually stripped away and become unbound. The interaction between these unbound particles and the bound particle remaining within the sub-halo leads to an addional decay of the sub-halo orbit, which is called the self-friction effect. We propose that the self-friction accerlation is proportional to the mass lost by the subhalo during one orbital time and inversely proportional to the square of mean distance of these unbound particles, i.e. tidal radius. This gives

\begin{equation}
\textbf{a}_{\text{self}}=-\alpha_{\text{self}}G\dot{M}_{\text{sat}}T_{\text{orbit}}\frac{1}{r_t^2}\frac{\Delta r_t}{r_t}\frac{\textbf{V}_{\text{sat}}}{V_{\text{sat}}},
\end{equation}

where $\alpha_{\text{self}}$ is a free parameter, $r_t$ is the tidal radius, and $\Delta r_t$ is the difference of $r_t$ on the near side and far side of the sub-halo with respect to the host. Here we also include a correction term $\frac{\Delta r_t}{r_t}$, which characterizes the asymmetry in the spatial distribution of unbound particles. Note that a symetric distriubtion of unbound particles on the near side and far side will contribution zero net acceleation.

### Things to do
1. A global MCMC fitting of free parameters in the dynamical friction and self-friction models including all idealized N-body simulations currently available.
2. Check the effect of self-friction on subhalo mass function and radial distribution.
3. Think about the aplication of the model predictions.

## Paper 2: Tidal mass loss

[Link to paper on Overleaf](https://www.overleaf.com/5471935121dnfxykqnqykx)

### Outline and tasks

In this work, we will focus on the tidal mass loss and the density evolution of subhaloes.

1. We check different tidal radius definitions and the time scale for tidal mass loss. We find that a simple model assuming that the mass outside the tidal radius is lost on one orbital time scale can well describe the mass evolution of subhaloes if the density evolution of subhloes are well modeled.
2. To model the evolution of subhalo density profile, we make use of the impulse approximation for tidal heating with and without adiabatic corrections. We find that a global change of the efficiency of tidal heating provide a better description than the radius-dependent adiabatic corrections.
3. We also propose a toy model of the mass loss caused by particles "leak" through the tidal surface, which provides an explanation for the slowly continuous mass loss near apocenters. We calibrate the free parameters in the tidal mass loss and tidal heating models by comparing the mass evolution and density evolution to idealized N-body simulations. The best-fit parameters are in good agreement with those calibrated to cosmological N-body simulations in our previous work.
4. Applying the subhalo models and calibrated parameters to merger trees generated using extended Press–Schechter formalism, we compute the subhalo mass function and radial distribution function for Milky-like halos and compare them with cosmological simulations.
