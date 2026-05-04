# Fuzzy Dark Matter Granule Structure

## Goals

Build a semi-analytic treatment of the effects of fuzzy DM granule perturbations on the orbital motion of particles (black holes, subhalos, etc.).

First, we can try to reproduce the diffusion study of [Dutta Chowdhury et al. (2021)](https://ui.adsabs.harvard.edu/abs/2021ApJ...916...27D).

## Methods

Use the Paley-Wiener representation of Brownian motion (see section 6 of this [paper](http://www.columbia.edu/~mh2078/MonteCarlo/MCS_SDEs.pdf)) to generate a random perturbation to the acceleration of the particle as a function of time.
$$
a_x(\tau) = a_{x,0} \frac{\tau}{\sqrt{2\pi}} + \frac{2}{\sqrt{\pi}} \sum_{n=1}^m a_{x,n} \frac{\sin(n\tau/2)}{n},
$$
(for the $x$-component of acceleration, with similar expressions for the $y$ and $z$-components) where $\tau$ is a dimensionless time that runs from 0 to $2\pi$, defined as
$$
\tau = 2 \pi \frac{t}{t_\mathrm{max}},
$$
where $t_\mathrm{max}$ is the maximum time that we want to run the simulation for, and we want to choose $m$ such that the frequency of the fastest mode in the Paley-Wiener expansion equals the frequency of the granule structure oscillations:
$$
2 \pi = \frac{m}{2} \tau_\mathrm{granule} = \frac{m}{2} \frac{2 \pi}{f_\mathrm{granule} t_\mathrm{max}},
$$
where $\tau_\mathrm{granule}$ is the oscillation period of the granules in the dimensionless time, and we can use $\tau_\mathrm{granule} = 2\pi/ f_\mathrm{granule} t_\mathrm{max}$. Then:
$$
m = 2 f_\mathrm{granule} t_\mathrm{max}.
$$
Of course, $m$ has to be an integer, so probably what we want to do is first compute $m$ using the above, and then increase $t_\mathrm{max}$ to make $m$ equal to the next largest integer.

From [Dutta Chowdhury et al. (2021; eqn. 4)](https://ui.adsabs.harvard.edu/abs/2021ApJ...916...27D) we have  an expression for the granule frequency:
$$
f_\mathrm{granule} = 10.94 \hbox{Gyr}^{-1} \left( \frac{\rho_0}{10^9 \mathrm{M}_\odot \hbox{kpc}^{-3}} \right)^{1/2}.
$$
They all tell us (eqn. 11 and 12) the effective mass of the granule quasi-particles:
$$
m_\mathrm{eff} = \rho (f \lambda_\mathrm{db})^3,
$$
where $f=0.282$ for a Gaussian velocity distribution in the halo particles and
$$
\lambda_\mathrm{db} = \frac{h}{m_\mathrm{b} \sigma_\mathrm{Jeans}},
$$
where $h$ is Planck's constant, $m_\mathrm{b}$ is the mass of the fuzzy DM particle, and $\sigma_\mathrm{Jeans}$ is the velocity dispersion in the halo found by solving the Jeans equation. $\sigma_\mathrm{Jeans}$ is obtained by solving the spherical Jeans equation under the assumption of velocity isotropy with the time averaged density profile of the halo.

They also show that the effective diameter of the quasi-particle is $d\approx 0.35 \lambda_\mathrm{db}$.

From this we can estimate that the amplitude of the acceleration due to a nearby quasi-particle will be:
$$
a \approx \frac{\mathrm{G} m_\mathrm{eff}}{d^2}.
$$

For the Paley-Weiner series, we can then choose the coefficients $a_{x,n}$ by sampling random numbers from a normal distribution with mean zero and $\sigma = \alpha \mathrm{G} m_\mathrm{eff}/d^2$, where $\alpha$ is some dimensionless parameter of order unity that we can tune to get the correct accelerations and match the diffusion to N-body simulation results.

## May 15
The central density, $\rho_0$ fluctuates by about a factor of 2 around a time averaged value of $1.04\times10^8 \mathrm{M}_\odot \hbox{kpc}^{-3}$.

Using the parameters from the paper, $\rho_0 = 1.04\times10^8 \mathrm{M}_\odot \hbox{kpc}^{-3}$, $t_\mathrm{max} = 10 \hbox{Gyr}$, $f_\mathrm{granule} = 3.258 \hbox{Gyr}^{-1}$.
We can choose m = 71, and then set $t_\mathrm{max} = 10.062 \hbox{Gyr}$. So $\tau_\mathrm{granule} = 0.177$.
Using the Paley-Wiener representation of Brownian motion, the x-component of acceleration is the following figure.
![image](https://hackmd.io/_uploads/HkLWbW67A.png)
The following figure shows the sum truncated one.
![image](https://hackmd.io/_uploads/HyDQ--pm0.png)
Density profile distribution: 
$$
r\leq r_\mathrm{sol},\,\,\rho_\mathrm{sol}(r) = \frac{\rho_0}{(1+0.091(r/r_c)^2)^8}
$$
$$
r>r_\mathrm{sol},\,\,\rho_\mathrm{nfw}(r) = \frac{\rho_\mathrm{s}}{(r/r_s)(1+r/r_s)^2}
$$
The following figure shows the density profile at $\mathrm{t = 0}$.
![image](https://hackmd.io/_uploads/B1UPWb6XR.png)
## May 23
Jeans Equation when the velocity dispersion is isotropic:
$$
\frac{d}{dr}\rho\sigma^2 = -\frac{\mathrm{G M(r)}}{r^2}\rho.
$$
$$
\sigma(r)^2 = \frac{G}{\rho(r)}\int_\mathrm{r}^{\infty} \frac{\mathrm{M(r')}}{r'^2}\rho(r')dr'
$$
![image](https://hackmd.io/_uploads/BJjrkXnY0.png)
![image](https://hackmd.io/_uploads/BJWDkXhK0.png)
From the paper, we have $\mathrm{m_b = 8\times10^{-23} eV}$, $\lambda_\mathrm{db}=\frac{\mathrm{hc^2}}{\mathrm{mv}}=120.47\mathrm{kpc}\times\frac{\mathrm{10^{-22}eV}}{\mathrm{m_b\times\sigma_{Jeans}}}$.
The distribution of the de Broglie wavelength:
![image](https://hackmd.io/_uploads/ry0ty72KA.png)
The distribution of the amplitude of the acceleration due to a nearby quasi-particle:
![image](https://hackmd.io/_uploads/rJNpy73FR.png)
## June 6
Choose the coefficients $\mathrm{a_x^{n}}$ by sampling random numbers from a normal distribution with mean zero and $\sigma=\alpha\frac{\mathrm{Gm_{eff}}}{\mathrm{d^2}}$.
The particle starts at a point in orbit corresponding to $\mathrm{r_c}$. Use $\frac{\mathrm{GM_r}}{\mathrm{r^2}} = \frac{\mathrm{v^2}}{\mathrm{r}}$ to get the initial velocity of the particle. I tried to use $\mathrm{dt} = \tau_\mathrm{granule} \approx \mathrm{0.176 Gyr}$. The particle can't move as an orbit. So I set $\mathrm{dt = 0.01 Gyr}$ and $\mathrm{t_{max}=10 Gyr}$.


## Using a random walk in velocity instead of acceleration

If we want a random walk in velocity, then we write
$$
v_x(\tau) = v_{x,0} \frac{\tau}{\sqrt{2\pi}} + \frac{2}{\sqrt{\pi}} \sum_{n=1}^m v_{x,n} \frac{\sin(n\tau/2)}{n}.
$$
If we take the derivative of this with respect to time we get for the acceleration:
$$
\frac{\mathrm{d}\tau}{\mathrm{d}t} \frac{v_0}{\sqrt{2\pi}}
$$
for the first term, and
$$
\frac{\mathrm{d}\tau}{\mathrm{d}t}  \frac{v_n}{\sqrt{2\pi}} \cos(n\tau/2)
$$
for the other term, and we know that:
$$
\tau = 2 \pi \frac{t}{t_\mathrm{max}},
$$
so these simplify to:
$$
\frac{\sqrt{2\pi}}{t_\mathrm{max}} v_0
$$
and
$$
\frac{\sqrt{2\pi}}{t_\mathrm{max}} v_n \cos(n\tau/2).
$$
This suggests that the amplitude of the coefficients in the series, $\sigma_\mathrm{V}$ could be written as:
$$
\frac{\sqrt{2\pi}}{t_\mathrm{max}} \sigma_\mathrm{V} = a_\mathrm{FDM}
$$
with
$$
a_\mathrm{FDM} \approx \frac{\mathrm{G} m_\mathrm{eff}}{d^2}
$$
as usual, or
$$
\sigma_\mathrm{V} = \alpha a_\mathrm{FDM} t_\mathrm{max} / \sqrt{2\pi},
$$
so the terms in the acceleration will also be drawn from a normal distribution of zero mean, but width
$$
\sigma_a = \alpha a_\mathrm{FDM} 
$$
So, we can write the series for the acceleration (e.g. for the $x$-direction) as:
$$
a_x(\tau) = a_{x,0} + \sum_{n=1}^m a_{x,n} \cos(n\tau/2),
$$
where the $a_{x,n}$ coefficients are drawn from a normal distribution with zero mean and width $\sigma_a$. So, you would just need to change your current implementation to include the $a_{x,0}$ term, and remove the $2/\sqrt{\pi}n$ factors from the other terms.

When we integrate this it will give the form of the original random walk in the velocity, so we should get a correct random walk in velocity. And, with this form, the acceleration isn't forced to be zero at $\tau=0$ (which always seemed arbitrary to me), and we shouldn't get the periodic behavior in the acceleration either.

Velocity dispersion:
$$<(\Delta v)^2> = \frac{1}{N}\sum^N_{i=1}{(\Delta v_i)^2},$$
where $\Delta v_i = v_i - \bar{v}$, $v_i$ is the velocity at different radius and $\bar{v}$ is the mean velocity.
Velocity dispesion at x-direction is $\sigma_x = <(\Delta v)^2>$
Velocity dispersion is $\sigma = \sqrt{\sigma_x+\sigma_y+\sigma_z}$

Considering the interaction between the granules, we correct the formula of time.
$$\tau_\mathrm{granule} \rightarrow \tau_\mathrm{granule} + \frac{2 \pi \delta t}{t_\mathrm{max}}(1 + \frac{t_\mathrm{granule}}{t_\mathrm{v}}),$$
where $t_\mathrm{granule}=\frac{1}{f_\mathrm{granule}}$, $\tau_\mathrm{granule} = \frac{2\pi}{f_\mathrm{granule}t_\mathrm{max}}$ and $t_\mathrm{v} = \frac{2 d_\mathrm{eff}}{v}$,
$$t \rightarrow t + \delta t.$$
To match the value of the massless result in that paper, let $\alpha = 0.05$.
![image](https://hackmd.io/_uploads/By5W3TZ9C.png)


## Dynamical Friction
### Classical
(Chapter 3 in [Lancaster et al. (2019)](https://ui.adsabs.harvard.edu/abs/2020JCAP...01..001L/abstract))
Reference force : $F_\mathrm{rel} = 4\pi \bar{\rho}(\frac{GM}{v_\mathrm{rel}})^2$,
where $\bar{\rho}$ is mean density and $v_\mathrm{rel}$ is the velocity relative to the background.
$b$ can be approximately equal to the orbital radius and $l_{90} \approx \frac{GM}{v_\mathrm{rel}^2}$.
Coulomb logarithm : $\Lambda = \frac{b}{l_{90}}$,
where $b$ is the maximum distance at which the field particles are still interacting with the satellite and $l_{90}$ is the distance at which a field particle has to approach the satellite to be deflected by $90^\circ$.
$$X = \frac{v_{rel}}{\sqrt{2}\sigma},$$
where $\sigma$ is the one-dimensional velocity dispersion of the Maxwellian distribution of the field stars (here we use $\sigma = \sigma_\mathrm{Jeans}$), and
$$G(X) = \frac{1}{2X^2}[erf(X)-\frac{2X}{\sqrt{\pi}}e^{-X^2}].$$
Dynamical friction force is
$$F_\mathrm{DF} = 2\pi F_\mathrm{rel}X^2G(X)ln\Lambda.$$
![image](https://hackmd.io/_uploads/HJTOhTbq0.png)
![image](https://hackmd.io/_uploads/rJ1pn6b5C.png)

We want the dynamical friction to be smaller, so we try to select the maximuim one between $l_{90} \approx \frac{GM}{v_\mathrm{rel}^2}$ and $d_\mathrm{eff}$ as $l_{90}$.

### Fuzzy DM
(Section 4.5 in [Lancaster et al. (2019)](https://ui.adsabs.harvard.edu/abs/2020JCAP...01..001L/abstract))
Background de Broglie wavelength: $\widetilde{\lambda} = \frac{\hbar}{mv_\mathrm{rel}}$ (Eq. 2.2)
The de Broglie wavelength associated with dispersion: $\widetilde{\lambda}_\mathrm{\sigma} = \frac{\hbar}{m_\mathrm{p}\sigma}$ (Eq. 2.5)
Classical Mach number: $M_\sigma = \frac{\widetilde{\lambda}_\mathrm{\sigma}}{\widetilde{\lambda}} = \frac{v_\mathrm{rel}}{\sigma}$ (Eq. 2.8)
Cutoff scale: $\widetilde{b} = \frac{b}{\widetilde{\lambda}}$
If the cutoff scale $\widetilde{b}$ is much larger than dispersion de Broglie wavelength $\widetilde{\lambda}_\sigma$, the dynamical fraction can be given by
$$F_\mathrm{DF} = C_\mathrm{rel}\,F_\mathrm{rel},$$
where $C_\mathrm{rel} = M_\sigma^2\,\mathrm{log}(\frac{2\widetilde{b}}{M_\sigma})G(\frac{M_\sigma}{\sqrt2})$ (Eq. 4.39).
![image](https://hackmd.io/_uploads/rkwDa6Z9R.png)
![image](https://hackmd.io/_uploads/HkTu6ab5R.png)

# Notes on implementing a full model in Galacticus

## Halo density profiles

Xiaolong suggests using a density profile for the soliton of:
$$
\rho_\mathrm{s}(r) = \frac{\rho_0}{\left(1 + \left[0.23  \frac{r}{r_\mathrm{c}}\right]^2 \right)^8},
$$
where $\rho_0$ is the central density of the soliton and $r_\mathrm{c}$ is the soliton radius. These are related by:
$$
r_\mathrm{c} \propto \rho_0^{1/4}.
$$
For the outer profile he suggests:
$$
\rho_\mathrm{o}(r) = \frac{\rho_\mathrm{s}}{\left(1 + \left[\frac{r}{r_\mathrm{s}}\right]^2\right)^2}
$$
These would be summed to find the total profile. We would need to see if we can compute analytically the mass enclosed within a given radius for these profiles - and maybe some other properties (the potential etc.) too.

We'll also need a model for the parameters $r_\mathrm{s}$, $\rho_\mathrm{s}$, $r_\mathrm{c}$, and $\rho_0$.

Some relevant integrals of these density profiles can be found analytically. (See shared Mathematica notebook.)

### Soliton radius

(From Xiaolong) The soliton radius can be computed from the core-halo mass relation. There are several choices: (1) [Schive et al. 2014](https://arxiv.org/abs/1407.7762), this is probably the most popular model, which simply assumes a power law of 1/3; (2) the one based on the merger history ([Du et al. 2017](https://arxiv.org/abs/1609.09414)); (3) power law including a large scatter described in [Chan et al. 2022](https://arxiv.org/abs/2110.11882).

In our [recent work](https://arxiv.org/abs/2301.09769) on soliton merger rate, we have a comparison of different models in Fig. 11. I have a local version of Galacticus that implements these relations. I would need to clean up the codes a bit before committing the changes. I can do this early week next week if needed.

Another interesting model is [Kawai et al. 2024](https://arxiv.org/abs/2312.10744) which argues that the scatter in the relation might be caused by the scatter of concentration-halo mass relation.

## Model for the velocity dispersion

For this we need to solve the Jeans equation, and then divide by $\sqrt{2}$ to account for the quantum pressure term. It would be nice if there was an analytic solution to the Jeans equation, but I doubt that there is! We can always solve numerically, and then include the $\sqrt{2}$ factor.

## Granule acceleration

Here we would just need to adapt our model to function in Galacticus. The overall approach would be the same. For each subhalo we would assign a set of random coefficients to determine the random walk of accelerations. Then, at each evolution step, we just need to evaluate the acceleration - Galacticus will then include this in its ODE solver along with all of the other accelerations (it will already handle the non-granule acceleration term).

### Finite-size objects

We have calibrated $\alpha$ in our model for point-mass objects. If we have an extended object with finite size, it should effectively smooth over some larger region containing many granules, and average the perturbations from them - making $\alpha$ effectively smaller.

If we assume that the perturbations from granules are uncorrelated, then I'd expect the amplitude of the accelerations to scale as $1/\sqrt{N}$ where $N$ is the number of granules averaged over. For an object of size $r_{1/2}$ (its half-mass radius), the number of granules averaged over is $\sim (r_{1/2}/d_\mathrm{eff})^3$. So, a simple model would be:
$$
\alpha(r_{1/2}) = \alpha_0 \left[ \hbox{max}\left(1,\frac{r_{1/2}}{d_\mathrm{eff}} \right) \right]^{-3/2}
$$
where $\alpha_0$ is the value for a point object, and if $r_{1/2} < d_\mathrm{eff}$ we just set the result to $\alpha_0$.

### Updated calculation (09/05/2024)

I thought more about the effects of finite size subhalos on the granule acceleration. I think we can derive the expected scaling relatively simply. A full calculation could be done - but I don't think that's necessary as I wouldn't trust the normalization anyway (e.g. we'd have to assume a uniform host halo etc.), but we have already calibrated the normalization, so all we care about is the scaling.

The simple way to think about this is to consider a random walk process. Suppose we have $N$ granules, each providing an acceleration drawn from a Gaussian with width $\sigma$. If the accelerations are independent random variables then, when we sum them, we can think of the vector making a random walk in a 3D acceleration space as we add the contribution from each granule. For Gaussian random walks, the expectation value for the distance from the origin (i.e. the magnitude of the acceleration in this case) just scales as $\sigma\sqrt{N}$ (with some coefficient that I'm ignoring as all we care about is the scaling). Suppose now that we consider some spherical shell around our perturber with radius r. The number of granules in this region is $N \propto r^3$, and the acceleration is $\sigma \sim Gm/r^2$ (where $m$ is the mass of the granule). So, in our random walk resulting from adding the accelerations from all of these granules, we expect a magnitude of the acceleration of  $\sigma \sqrt{N} \propto r^{-2} \sqrt{r^3} \propto 1/\sqrt{r}$. 

From this we see that the contributions will be dominated by nearby granules (i.e. the further away they are the smaller their net contribution). So, what matters to set the value of α is the minimum distance to a granule. This is why we've used d_eff for the case of a point mass perturber. Given the above scaling, for a finite-size perturber we can just assume $\alpha(r_{1/2}) = \alpha_0 \left[\hbox{max}(1,r_{1/2}/d_\mathrm{eff})\right]^{-1/2}$. 

## Dynamical friction

Galacticus has models for the dynamical friction. We can simply add a new one implementing the fuzzy DM dynamical friction model that we have used above.

## To compute the density profile of a lens halo
The mass of a lens halo is $10^{13} \mathrm{M}_\odot$ at $z = 0.5$. Use the cosmology parameters from Planck18. Use the method in [Schive et al. (2014)](https://arxiv.org/abs/1407.7762) to compute the core mass and the core radius.

## Compare with  Dutta Chowdhury et al. 2021
Corrected $r_\mathrm{half} = \frac{r_\mathrm{vir}}{2}(\frac{M_\mathrm{particle}}{M_\mathrm{vir}})^{\frac{1}{3}}$.
Massless particle, $\alpha = 0.05$
![image](https://hackmd.io/_uploads/BJGK5y4TC.png)
![image](https://hackmd.io/_uploads/S1ln5JNpA.png)
$M_\mathrm{particle} = 10^5 M_\odot$, $\alpha = 0.06$, $r_\mathrm{half} = 0.557$ (Classical Dynamical Friction)
![image](https://hackmd.io/_uploads/SkCaqk4aR.png)
![image](https://hackmd.io/_uploads/S1-ej1N6C.png)
$M_\mathrm{particle} = 10^7 M_\odot$, $\alpha = 0.15$, $r_\mathrm{half} = 2.585$ (Classical Dynamical Friction)
![image](https://hackmd.io/_uploads/r1dZjyVaC.png)
![image](https://hackmd.io/_uploads/rJ5zjyNTR.png)

## Relation to diffusion coefficients

Let's consider our random walk as a sequence of discrete steps. The characteristic timescale for a step will be the granule timescale, $t_\mathrm{granule} = 1/f_\mathrm{granule}$. The characteristic change in velocity will then be $a_\mathrm{grandule} t_\mathrm{granule}$.

After $m$ steps, the mean squared velocity change will therefore be $\overline{v^2} = m (a_\mathrm{grandule} t_\mathrm{granule})^2$. In the continuum limit we can therefore write
$$
\overline{v^2} =  a_\mathrm{grandule}^2 t_\mathrm{granule} ( m t_\mathrm{granule}) =  a_\mathrm{grandule}^2 t_\mathrm{granule} t.
$$
For a diffusion process, with second order diffusion coefficient, $D$, we have (by definition):
$$
\overline{v^2} = D t.
$$
Therefore we can make the correspondence:
$$
a_\mathrm{grandule}^2 t_\mathrm{granule}  = D,
$$
or
$$
a_\mathrm{granule}   = \sqrt\frac{D}{t_\mathrm{granule}},
$$
It would be interesting to compare the values of $a_\mathrm{granule}$ and $\sqrt\frac{D}{t_\mathrm{granule}}$ using the equation for $D$ (the sum of the second order diffusion coefficients) to see if they are comparable. If they are maybe we can just use $\sigma_V = \alpha \sqrt{D t_\mathrm{granule}}$ as the amplitude of the random coefficients in our random walk series.

### Compare $a_\mathrm{granule}$ and $\sqrt\frac{D}{t_\mathrm{granule}}$ algebraically
$$
a_\mathrm{granule} = \frac{Gm_\mathrm{eff}}{d^2} = \frac{G\rho f^3\lambda_\mathrm{db}^3}{0.35^2\lambda_\mathrm{db}^2} = \frac{0.282^3}{0.35^2}G\rho\lambda_\mathrm{db} = 0.183G\rho\lambda_\mathrm{db}
$$
Second order of the energy diffusion coeficient:
$$
D = \frac{1}{2}\frac{4\sqrt{2}\pi G^2\rho m_\mathrm{eff}}{\sigma_\mathrm{h}}\ln\Lambda_\mathrm{FDM}\frac{erf(X_\mathrm{eff})}{X_\mathrm{eff}}
$$
$$
\sqrt\frac{D}{t_\mathrm{granule}} = G\rho\lambda_\mathrm{db}f^{\frac{3}{2}}\sqrt{\frac{4\pi}{\sigma_\mathrm{jeans}}}\sqrt{\ln\Lambda_\mathrm{FDM}}\sqrt{\lambda_\mathrm{db}}\sqrt{10.94\mathrm{Gyr}^{-1}(\frac{\rho}{10^9M_\odot\mathrm{kpc}^{-3}})^{\frac{1}{2}}}\sqrt{\frac{erf(X_\mathrm{eff})}{X_\mathrm{eff}}},
$$
$$
\sqrt\frac{D}{t_\mathrm{granule}} = 0.00987G\rho^{\frac{5}{4}}\lambda_\mathrm{db}^{\frac{3}{2}}\sqrt{\ln\Lambda_\mathrm{FDM}}\sqrt{\frac{erf(X_\mathrm{eff})}{v}},
$$
$\sqrt{\frac{erf(X_\mathrm{eff})}{X_\mathrm{eff}}}$ depends on velocity, because of $X_\mathrm{eff} = \frac{v}{\sqrt{2}\sigma_\mathrm{h}} = \frac{v}{\sigma_\mathrm{jeans}}$. And $\ln\Lambda_\mathrm{FDM} = \frac{1}{2}\ln(1+(\frac{4\pi r}{\lambda_\mathrm{db}})^2) \approx \ln(\frac{4\pi r}{\lambda_\mathrm{db}})$, so $\sqrt{\ln\Lambda_\mathrm{FDM}}$ maybe can cancel out the term $\sqrt{\lambda_\mathrm{db}}$.

alpha:
  

| $M_\mathrm{particle}$  | $a_\mathrm{granule}$ | $\sqrt\frac{D}{t_\mathrm{granule}}$ |
| ---------------------- | -------------------- | ----------------------------------- |
| $10^5\,M_\odot$        | 0.06                 | 0.06                                |
| $10^6\,M_\odot$        | 0.085                 | 0.09                               |
| $5\times10^6\,M_\odot$ | 0.14                 | 0.14                                |
| $10^7\,M_\odot$        | 0.16                 | 0.14                                |

# Notes on correction of Eq. 5 and 9 in the paper
The random walk in the velocity of the particle should be
$$
v_x(\tau) = \frac{1}{\sqrt{m}}\left(v_{x,0} \frac{\tau}{\sqrt{\pi}} + \frac{2}{\sqrt{\pi}} \sum_{n=1}^m v_{x,n} \frac{\sin(n\tau/2)}{n}\right).
$$
Here the first term has been changed. If we consider when n→0, the limit will be:
$$
\lim_{n \to 0} \frac{\sin(n\tau/2)}{n} = \frac{\tau}{2},
$$
then the first term should be corrected as the previous equation, rather than the one we initially wrote. The previous version included an extra $1/\sqrt2$ factor, which was incorrect.
Then take the derivative of this with respect to $\tau$,
$$
\frac{dv_x(\tau)}{d\tau} = \frac{1}{\sqrt{m}}\left(\frac{1}{\sqrt{\pi}} v_{x,0}+\frac{1}{\sqrt{\pi}}\sum_{n=1}^m v_{x,n} \cos(n\tau/2)\right).
$$
Then we have
$$
\frac{dv_x(\tau)}{d\tau}\frac{d\tau}{dt} = \frac{1}{\sqrt{m}}\left(\frac{2\sqrt{\pi}}{t_\mathrm{max}} v_{x,0}+\sum_{n=1}^m \frac{2\sqrt{\pi}}{t_\mathrm{max}} v_{x,n} \cos(n\tau/2)\right).
$$
This suggests that the amplitude of the coefficients in the series could
be written as:
$$
\frac{2\sqrt{\pi}}{t_\mathrm{max}} v_{x,n} = a_\mathrm{eff} = \sigma_a
$$