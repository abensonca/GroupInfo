# SIDM Evolution Notes

The evolution of an SIDM halo is driven by relaxation, which occurs on the characteristic timescale, $t_\mathrm{c}$. In the context of the gravothermal model, we can think of this as redistribution energy in the halo, and so we can define a "cooling rate" per unit volume due to SIDM effects as
$$
\mathcal{L}_\mathrm{SIDM} = \frac{\phi_\mathrm{SIDM} \rho_\mathrm{SIDM}}{t_\mathrm{c}}
$$
where $\phi_\mathrm{SIDM}$ is the gravitational potential of the SIDM halo, and $\rho_\mathrm{SIDM}$ is the density in the halo.

For a halo that is accreting, there is also a "heating rate" due to new mass being added at each radius
$$
\mathcal{H}_\mathrm{SIDM} = \phi_\mathrm{SIDM} \dot{\rho}_\mathrm{SIDM}
$$
As we are interested in characterizing the evolution *relative* to CDM, we should subtract from this the heating rate in CDM:
$$
\mathcal{H}_\mathrm{CDM} = \phi_\mathrm{CDM} \dot{\rho}_\mathrm{CDM}
$$
I will assume that $\dot{\rho}_\mathrm{CDM} = \dot{\rho}_\mathrm{SIDM}$ - i.e. cosmological accretion does not differ between the two cases. And, for simplicitly, I will assume that:
$$
\frac{\dot{\rho}_\mathrm{SIDM}}{\rho_\mathrm{SIDM}} = \frac{\dot{M}}{M}
$$
i.e. the growth rate in density at any radius is proportional to the mass accretion rate. (This seems like possibly a poor assumption, but this could always just be recharacterized as applying specifically to the rate at $r_\mathrm{eff}$ or something similar.)

Then we can write the net rate of change of energy, relative to CDM, as
$$
\dot{E} = \mathcal{L}_\mathrm{SIDM} + \mathcal{H}_\mathrm{SIDM} -  \mathcal{H}_\mathrm{CDM} = \phi_\mathrm{SIDM} \rho_\mathrm{SIDM} \left( \frac{1}{t_\mathrm{c}} + \frac{\dot{M}}{M} -  \frac{\dot{M}}{M} \frac{\phi_\mathrm{CDM}}{\phi_\mathrm{SIDM}} \right)
$$
Suppose we can parameterize $\phi_\mathrm{CDM} = f(\tau) \phi_\mathrm{SIDM}$ since the parameter $\tau$ describes the structure of the SIDM halo. We don't know the precise form of $f(\tau$)$ (although, I guess it's in princeiple derivable), but we can just Taylor expand it, $f(\tau) = f^{(0)} + f^{(1)} \tau + \ldots$. By construction we must have that $f^{(0)}=1$. The net heating rate then becomes:
$$
\dot{E} = \mathcal{L}_\mathrm{SIDM} + \mathcal{H}_\mathrm{SIDM} -  \mathcal{H}_\mathrm{CDM} = \phi_\mathrm{SIDM} \rho_\mathrm{SIDM} \left( \frac{1}{t_\mathrm{c}} -  \frac{\dot{M}}{M} f^{(1)} \tau \right)
$$
Then, inspired by the parametric approach from Daneng's paper, we identify the term in parentheses as the rate of change of the evolution parameter, $\tau$, so we get:
$$
\dot{\tau} =  \frac{1}{t_\mathrm{c}} -  \frac{\dot{M}}{M} f^{(1)} \tau,
$$
which we could also write as
$$
\dot{\tau} =  \frac{1}{t_\mathrm{c}} -  \alpha \Gamma \tau,
$$
with $\alpha = f^{(1)}$ and $\Gamma = \dot{M}/M$.