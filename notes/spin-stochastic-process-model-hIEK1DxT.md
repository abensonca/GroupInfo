# Spin Stochastic Process Model

###### tags: `dark matter`

## Goal

The goal here is to create a model for halo spins which:
1. captures the time variation in spin as the halo grows in mass;
2. reproduces the measured distribution function of halo spins;
3. can be applied to halos defined with smooth mass accretion histories.

## Model

### General Idea

Since [Benson, Behrens, & Lu (2020)](https://ui.adsabs.harvard.edu/abs/2020MNRAS.496.3371B/abstract) show that spin evolution can be modeled as a random walk process driven by merging of dark matter halos, I want to consider a similar approach.

The [Benson, Behrens, & Lu (2020)](https://ui.adsabs.harvard.edu/abs/2020MNRAS.496.3371B/abstract) model can not be applied in this case though as we want a model which can be applied to halos with smooth mass accretion histories (so, no merger events).

Given that we have no knowledge of the mergers in such a scenario we can use a fully stochastic model instead - i.e. something similar to a Wiener process (but, as we will see below, with time-dependent variance).

### Model Description

The three components of the angular momentum vector are treated as independent Wiener processes with time-dependent variance. Specifically, each component of the angular momentum vector obeys:

$$
J_\mathrm{i}(t_2) = J_\mathrm{i}(t_1) + \left[ \sigma^2 \left\{ J_\mathrm{v}^2(t_2) - J_\mathrm{v}^2(t_1) \right\} \right]^{1/2} N(0,1)
$$

  where $J_\mathrm{v}(t) = M_\mathrm{v}(t) V_\mathrm{v}(t) R_\mathrm{v}(t)$ is the characteristic virial angular momentum, $M_\mathrm{v}(t)$, $V_\mathrm{v}(t)$, and $R_\mathrm{v}(t)$ are the virial mass, velocity, and radius respectively, $\sigma^2$ represents the variance in angular momentum per unit increase in $J_\mathrm{v}^2$, and $N(0,1)$ is a random variable distributed as a standard normal.

The spin is then found from the magnitude of the total angular momentum, $|J| = \sum_{i=1}^3 J_\mathrm{i}^2$.

This model captures the idea that the increase in angular momentum from a merging event should be of order $\Delta M V_\mathrm{v}(t) R_\mathrm{v}(t)$ (since merging of halos have velocities which scale with $V_\mathrm{v}(t)$ and occurs at separation $R_\mathrm{v}(t)$). Additionally, because this is a Wiener process the resulting distribution of $J_\mathrm{i}(t)$ at any given time is independent of the number of steps used to get from $t=0$ to that time. (That is, the results are independent of how finely we sample the mass accretion history of each halo.)

### Initial Conditions

We have to assign a spin to the earliest time halo in a branch of the merger tree. For this it seems reasonable to simply sample a value from a measured distribution function. Providing this halo is at a time sufficiently early then the choice of initial condition should not matter (because, in a Wiener process the variance between the initial state and the final state grows monotonically larger as the time between the initial and final state increases).

## Results

I guessed a value of $\sigma^2 \approx 0.001$ which implies $\sigma \approx 0.032$ which is typical of cosmological halo spins. This turns out to work surprisingly well, but could of course be calibrated more precisely. (I tried some fine-tuning of this parameter, but there was no significant improvement - this is close to the optimal value.)

Here are results from a model in which I use $\sigma^2=0.001$ and use the cosmological spin distribution of [Benson (2017)](https://ui.adsabs.harvard.edu/abs/2017MNRAS.471.2871B/abstract) to set initial conditions. The blue line shows the distribution of [Benson (2017)](https://ui.adsabs.harvard.edu/abs/2017MNRAS.471.2871B/abstract), while the yellow points show the results at $z=0$ of this model applied to an ensemble of halo MAHs in which I sample the MAH in steps of $\Delta M/M = 0.10$.

![](https://i.imgur.com/bK94Pfc.png)

The agreement is remarkably good. The 3-D random walk that the Wiener process represents ensures that we get the correct $\lambda^3$ scaling at low spin. The model also seems to very nicely reproduce the exponential cut off at large spin.

### Testing Independence of Step Size

Repeating the above test but with more finely sampled halo MAHs of $\Delta M/M = 0.01$ I get the following results.

![](https://i.imgur.com/kX0XzxV.png)

### Testing Independence of Initial Conditions

It could be concerningly circular to use the [Benson (2017)](https://ui.adsabs.harvard.edu/abs/2017MNRAS.471.2871B/abstract) distribution to set the initial conditions, and then compare the output of the model to this same distribution.

To test this I repeated the above calculation but assigned all halos an initial spin of $\lambda = 0.042$ (close to the median of the cosmological distribution). The final distribution from the model is almost unchanged, indicating the expected lack of dependence on the initial conditions.

![](https://i.imgur.com/aokx1cy.png)

### Spin vs. Time

The following figure shows the spin vs. time for a single halo:

![](https://i.imgur.com/ua5Ry3L.png)

This shows plausible-looking fluctuations. The curve looks smoother at later times both because the MAH I use here has larger timesteps at later times (where growth is slower), and because the growth in $J_\mathrm{v}(t)$ itself is slower at later times. So, this also captures the dependence of the spin evolution timescale on the timescale for the growth rate of structure.