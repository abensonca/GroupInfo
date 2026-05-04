# SIDM Halo Core Collapse

###### tags: `dark matter`

## Goals

Build a semi-analytic model of core collapse in SIDM halos, and calibrate this against Carton Zheng's N-body simulations of the core collapse process.

## Progress

Finished repeating Essig et al. (2019). The code is explaind [here](https://www.overleaf.com/read/vypzswhyjdks).

Fangzhou finds (also shown in Essig et al. (2019) supplementary material Figure 1 and Figure 3) that the Essig2019 gravothermal solutions provides central density versus halo evolution time $\rho_c(t)$ relation in very good agreement with isolated N-Body simulation and Carnton's idealized simulation results. However, the gravothermal solution $\rho_c(t)$ does not agree with cosmological Pippin simulations. We believe this difference is caused by the mass accretion heating effect. 

In order to add halo mass accretion effect into Essig2019, we need to know $r_s(t)$, and $\rho(r,t)$. We adopt the halo mass evolution model proposed by Wechsler2002 Eq (3):
$$M(z)=M_0e^{-\alpha z},$$
here $M_0$ is the halo mass at $z=0$. This model introduce an extra free parameter $\alpha$, which may vary from halo to halo. For simplicity, we assume the mass accretion radial profile for SIDM halo is not very different from the CDM halo. We adopt the halo concentraltion evolution model given by Gao2008 Eq (6):
$$\log_{10}c(M,z)=A(z)\log_{10}(M(z))+B(z),$$
where $A(z)$ and $B(z)$ are linearly interpolated from Gao2008 Table 1. We can then estimate the halo virial radius growth following:
$$r_\mathrm{s}(M,z)=\left(\dfrac{M(z)}{4\pi\rho_\mathrm{crit}(z)\delta_c(M,z)[\ln(1+c(z))-c(z)/(1+c(z))]}\right)^{1/3}\,,\\ \rho_\mathrm{crit}(z)=\dfrac{3H^2(z)}{8\pi G}\,, \delta_c=\dfrac{\mathrm{const}\times c^3}{\ln(1+c)-c/(1+c)}\,.$$
the constant used for computing $\delta_c$ is determined by the simulation $\rho_s(z=0)$. The NFW profile evolve as:
$$\rho_\mathrm{NFW}(z,r)=\dfrac{\rho_\mathrm{crit}\delta_c}{(r/r_s)(1+r/r_s)^2}$$

In order to transfer redshift z to halo evolution time $t$, for now we assume that the SIDM halo evolution starts at $z=1$.

With the above halo accretion model, I introduce the halo accretion heating effect with the following treatments:
1). I want to keep $r_s$, $\rho_s$, and other rescaling parameters sugeested by Pippin simulation, therefore I decide to use the unitless quantities $\hat{r}$, $\hat{\rho}$, ... to absorb the time evolution of each mass shell. I set the initial conditions as:
$$\hat{r}_\mathrm{ini}^\mathrm{grid}=\hat{r}^\mathrm{grid}(z=0)\dfrac{r_s(z=z_\mathrm{ini})}{r_s(z=0)}\\
\hat{\rho}_\mathrm{ini}(r_\mathrm{ini}^\mathrm{grid})=\dfrac{\rho_\mathrm{crit}(z_\mathrm{ini})\delta_c(z_\mathrm{ini})/(\rho_\mathrm{crit}(z=0)\delta_c(z=0))}{\hat{r}_\mathrm{ini}^\mathrm{grid}(1+\hat{r}_\mathrm{ini}^\mathrm{grid})^2}$$
between Essig2019 supplimentary material step 2 and step 3. Specifically, after determining the time step $dt$ and specific energy change $du$, I do:
$t=t+dt\,, u=u+du\,, f_\rho=\dfrac{\rho_\mathrm{NFW}(t,r)}{\rho_\mathrm{NFW}(t-dt,r)}\,, \rho=\rho\times f_\rho$
$M_\mathrm{shell}=M_\mathrm{shell}\times f_\rho\,, M(r)=\Sigma M_\mathrm{shell}(r_\mathrm{shell}<r)\,, f_M=\dfrac{M}{M_\mathrm{previous\ time \ step}}\,, \mathrm{recompute}\ u$

I find that by setting $\alpha=0.1$ and $\beta=0.6$, the gravothermal solution with the mass accretion effect agrees well with Pippin's simulations:
![](https://i.imgur.com/52pN7zn.png)
(<font color="#f00">$\alpha=0.1$ seems to be a very small value compared with halos studied in Wechsler2002, but Pippin halo indeed has much smaller mass than the Wechsler2002 halos. Can I get the Pippin halo mass at $z=1$?</font>)

## Substructure heating 
$$C=n\dfrac{dE}{dt}=n_\mathrm{sat}\dfrac{\frac{1}{2}M_\mathrm{sat}dv^2}{dt}=n_\mathrm{sat}M_\mathrm{sat}v\dfrac{dv}{dt}=f_g\rho v\times 4\pi G^2\ln\Lambda M_\mathrm{sat}\rho\dfrac{\vec{v}}{v^3}\times[erf(X)-\dfrac{2X}{\sqrt{\pi}}\exp(-X^2)]$$
I assume $X=1/\sqrt{2}$, $\ln\Lambda=1.5$. One can show that the unitless $C$ term is:
$$\bar{C}=\dfrac{\ln\Lambda \bar{M}_\mathrm{sat}\bar{\rho}^2}{\bar{v}}$$
I assume $\bar{M}_\mathrm{sat}=f_g\bar{M}_\mathrm{shell}$, where $f_g=0.1$:
$$\dfrac{d\bar{u}}{d\bar{t}}=\dfrac{\bar{C}}{\bar{\rho}}=\dfrac{\ln\Lambda f_g^2\bar{M}_\mathrm{shell}\bar{\rho}}{\bar{v}}\times[erf(X)-\dfrac{2X}{\sqrt{\pi}}\exp(-X^2)]$$

## Self interaction friction heating
$$C=n_\mathrm{sat}M_\mathrm{sat}v\dfrac{dv}{dt}=f_g\rho v\chi_d(\sigma/m)vv_0\rho\approx f_g\chi_d\rho^2v^2\sqrt{\dfrac{2GM}{r}}(\sigma/d)\Longrightarrow \bar{C}=f_g\chi_d\bar{\rho}^2\bar{v}^2\sqrt{\dfrac{2GM}{r}}(\bar{\sigma/m})$$
here $v_0$ is the relative velocity between the satellite and the background before collision. I assume $v_0=\sqrt{2GM/r}$. I assume $f_g=0.1$ and $\chi_d=0.35$.

## An empirical model for Pippin
$$\hat{\rho}(\hat{r})=\dfrac{\rho_0\hat{r}}{\hat{r}/r_0+(\hat{r}/r_0)^\alpha}$$
Here $\rho_0$ is about the halo central density, $r_0$ is the core radius, and $\alpha\approx3$ gives the $\hat{\rho}(\hat{r})$ slope in the outter region close to the NFW profile. This model matches very nicely with Pippin at $z=0$ with:
$$
\log_{10}\rho_0=1.10+1.67\log_{10}\hat{\sigma}+1.12(\log_{10}\hat{\sigma})^2+0.169(\log_{10}\hat{\sigma})^3\\
\log_{10}r_0=-0.454-0.572\log_{10}\hat{\sigma}-0.393(\log_{10}\hat{\sigma})^2-0.0591(\log_{10}\hat{\sigma})^3\\
\log_{10}\alpha=0.554-0.0350\log_{10}\hat{\sigma}-0.0315(\log_{10}\hat{\sigma})^2-0.00536(\log_{10}\hat{\sigma})^3
$$
![](https://i.imgur.com/cOWfTuB.png)
The empirical model (dashed) and Pippin (solid) comparisons are shown below:
![](https://i.imgur.com/p0s22VZ.png)

If we assume the heating term is proportional to DM particle cross section such that $\sigma$ and $t$ are degenerated, i.e. the SIDM halo evolution is determined by $\sigma\times t$, we can rewrite the above empirical model as:
$$
\log_{10}\rho_0=1.36-0.699\log_{10}\hat{\sigma}\hat{t}-0.218(\log_{10}\hat{\sigma}\hat{t})^2+0.169(\log_{10}\hat{\sigma}\hat{t})^3\\
\log_{10}r_0=-0.595-0.269\log_{10}\hat{\sigma}\hat{t}-0.0737(\log_{10}\hat{\sigma}\hat{t})^2-0.0591(\log_{10}\hat{\sigma}\hat{t})^3\\
\log_{10}\beta=0.526-0.0196\log_{10}\hat{\sigma}\hat{t}-0.0108(\log_{10}\hat{\sigma}\hat{t})^2-0.00536(\log_{10}\hat{\sigma}\hat{t})^3$$


## An empirical triple power law model for gravothermal solutions
SIDM halo central density diverges at $$\log(\beta\hat{\sigma}\hat{t})=E=2.196$$
For $\log(\beta\hat{\sigma}\hat{t})\leq E-2$, the halo density profile can be described as the initial NFW profile multiplies a tanh central cut:
$$\hat{\rho}=\dfrac{tanh(\hat{r}/r_c)}{\hat{r}(1+\hat{r})^2}\\
\log r_c=A_{r_c}(\log(\beta\hat{\sigma}\hat{t}))^2+B_{r_c}\log(\beta\hat{\sigma}\hat{t})+C_{r_c}\\
A_{r_c}=-0.04867,\,
B_{r_c}=0.4526,\,
C_{r_c}=-0.7800
$$
For $\log(\hat{\sigma}\hat{t})>E-2$, the halo density profile can be described by a triple power law:
$$\hat{\rho}(\hat{r})=\dfrac{\rho_c}{1+\left(\dfrac{\hat{r}}{r_c}\right)^{s}\left(1+\dfrac{\hat{r}}{r_o}\right)^{3-s}},\ s=2.19$$
$$\log\rho_c=A_{\rho_c}(\log\beta\hat{\sigma}\hat{t}-(E+3))^2+C_{\rho_c}+\dfrac{D_{\rho_c}}{(E+0.0001-\log\beta\hat{\sigma}\hat{t})^{0.02}}\\
A_{\rho_c}=0.05771,\ C_{\rho_c}=-21.64,\ D_{\rho_c}=21.11\\
\log r_c=A_{r_c}(\log\beta\hat{\sigma}\hat{t}-(E+2))^2+C_{r_c}+\dfrac{D_{r_c}}{(E+0.0001-\log\beta\hat{\sigma}\hat{t})^{0.005}}\\
A_{r_c}=-0.04049,\ C_{r_c}=43.07,\ D_{r_c}=-43.07\\
\log r_o=A_{r_O}(\log\beta\hat{\sigma}\hat{t}-(E+2))^2+C_{r_o}+\dfrac{D_{r_o}}{(E+0.04-\log\beta\hat{\sigma}\hat{t})^{0.005}}\\
A_{r_o}=0.02403,\ C_{r_o}=-4.724,\ D_{r_o}=5.011
$$
This model can reproduce the gravothermal solution to better than 15\% fractional error before SIDM halo enters the SMFP regime:
![](https://i.imgur.com/cQpKiWv.png)
![](https://i.imgur.com/m79aEqS.png)

## Map from constant cross section to velocity dependent case 
Till this point we have only considered gravothermal solutions under constant SIDM particle cross section $\sigma$. However, many current SIDM zoom-in simulations adopt velocity dependent $\sigma(v)$ models, which is motivated by observations. In this section I introduce a simple method that maps constant $\sigma$ gravothermal solutions to the velocity dependent case. I will take a general model $\sigma(v)=\sigma_c\left(1+\dfrac{v^2}{v_c^2}\right)^{-2}$ as an example, but this mapping method works for arbitrary $\sigma(v)$ model.

In the previous sections we have shown that when assuming a constant $\sigma$, the time variable for the gravothermal solution is $\beta\sigma t$ under the LMFP regime. Through comparing constant $\sigma$ gravothermal solutions with $\sigma(v)$ gravothermal solutions, it seems that there is a non-linear time mapping $\beta\sigma t\rightarrow \beta\sigma t'$ such that $X(t)=X'(t')$, here X stands for SIDM density/enclosed mass/velocity dispersion/luminosity... profiles given by the gravothermal solutions. $X$ is the gravothermal solutions for constant $\sigma$, while $X'$ is solutions for the $\sigma(v)$ case.

In the constant $\sigma$ lookup table, given an array of the halo evolution time $\beta\sigma t$, we can derive $\beta\sigma dt$. If we now are about the $\sigma(v)$ model, the actual time step used by the gravothermal solutions should be $\beta\sigma\left(1+\dfrac{v'(t')^2}{v_c^2}\right)^{-2}dt'$, where $t'$ is the halo evolution time provided by Galacticus. Assuming the bracket is not contributed by $\sigma(v)$, but by a nontrivial $dt$ mapping, we have $dt=\left(1+\dfrac{v'(t')^2}{v_c^2}\right)^{-2}dt'=\left(1+\dfrac{v(t)^2}{v_c^2}\right)^{-2}dt'\Longrightarrow dt'=\left(1+\dfrac{v(t)^2}{v_c^2}\right)^{2}dt$. Here we have used the one-on-one assumption $v'(t')=v(t)$. In another word, we only need to change $dt$ in the original lookup table to $\left(1+\dfrac{v(t)^2}{v_c^2}\right)^{2}dt$, and integrate to get a new time grid axis, then we have finished the mapping between gravothermal solutions under constant $\sigma$ and $\sigma(v)$.

## Useful papers

* [Essig et al. (2019)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.123.121102) "Constraining Dissipative Dark Matter Self-Interactions"
* Carton's paper "[Core-collapse, evaporation and tidal effects: the life story of anself-interacting dark matter subhalo](https://www.overleaf.com/project/5e5ec98327c8960001685905)"" on Overleaf
* [Turner et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv201002924T/abstract) - shows an $r^{-3}$ central slope for core-collapsed density profiles
* [Wechsler et al. 2002](https://iopscience.iop.org/article/10.1086/338765)
* [Gao et al. (2008)](http://adsabs.harvard.edu/abs/2008MNRAS.387..536G)

## Halo density profile growth model

As discussed in our group meeting today (10-August-2021) I think it might be useful to think about the mass accretion onto our halo in terms of $\dot{\rho}(r,t)$ - the growth rate of density as a function of radius and time.

Suppose we assume that this growth of density follows what we would get for an NFW halo in CDM.

From something like the Wechsler et al. (2002) model we have $M(t)$ for NFW CDM halos. We also know how the virial radius of the halo should grow:
$$
R_\mathrm{v}(t) = \left( \frac{3 M(t)}{4 \pi \bar{\rho}(t) \Delta(t)} \right)^{1/3}
$$
where $\bar{\rho}(t)$ is the mean density of the universe, and $\Delta(t)$ is the density contrast for halos.

We can also use a model to predict the concentration of the halo $c(M,t)$, e.g. the model of [Gao et al. (2008)](http://adsabs.harvard.edu/abs/2008MNRAS.387..536G) is a simple example.

Then the scale radius of the NFW halo is just:
$$
r_\mathrm{s}(t) = R_\mathrm{v}(t)/c(M,t)
$$

Once we know $M(t)$, $R_\mathrm{v}(t)$, and $R_\mathrm{s}(t)$ we can find the NFW density profile as a function of time, $\rho(r,t)$. Then we just need to take the time derivative of this to get $\dot{\rho}(r,t)$. Then the mass added to each shell in a timestep would be something like:
$$
\Delta M = \dot{\rho}(r,t) 4 \pi r^2 \Delta r \Delta t
$$