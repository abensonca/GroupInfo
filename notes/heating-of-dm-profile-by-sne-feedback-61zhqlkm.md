# Heating of DM profile by SNe feedback

###### tags: `dark matter`

[Pontzen & Governato (2012)](https://ui.adsabs.harvard.edu/abs/2012MNRAS.421.3464P) describe this nicely, but not in a way that's super easy to incorporate into a semi-analytic model because they use finite timesteps and sum energy changes over them.

[Freundlich et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020MNRAS.491.4523F) do something similar (using results from simulations). Interestingly they compute the change in profile using something similar to our tidal heating model, in the sense that it's a no-shell-crossing model with:
$$
\Delta \epsilon = \frac{\mathrm{G} M_\mathrm{i}}{r_\mathrm{i}} - \frac{\mathrm{G} M_\mathrm{i}}{r_\mathrm{f}}.
$$
So, a possible approach is to just use the `darkMatterProfileDMOHeated` class, and create a new `darkMatterProfileHeatingImpulsiveOutflow` class which has a specific heating rate of:
$$
\dot{\epsilon}(r) = \alpha \frac{\mathrm{G}\dot{M}_\mathrm{out}(r)}{r} f\left(\frac{t_\phi}{t_\mathrm{dyn}}\right)
$$
where $\dot{M}_\mathrm{out}(r)$ is the mass outflow rate within some radius $r$, $\alpha$ is some normalization constant that can be tuned, and $f(x)$ is a function that reduces this heating rate to zero in the adiabatic limit, so something like:
$$
f(x) = (1 + x)^{-\gamma}
$$
where $\gamma$ is a parameter that can be tuned also.

The outflow rate $\dot{M}_\mathrm{out}$ would come from the regular feedback classes.
