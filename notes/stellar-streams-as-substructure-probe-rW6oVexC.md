# Stellar Streams as Substructure Probe

###### status: `active` · last reviewed: TBD

###### tags: `dark matter` `stellar streams` `subhalos`

## Erkal's Math



The math starts here: https://academic.oup.com/mnras/article/450/1/1136/1008580 
Here they assume circular orbits, and lots of other simplifying assumptions. Some of the math was first invented by carleberg in 2013(https://arxiv.org/pdf/1307.1929.pdf), but I think that's further back than we need to go. We're trying to get to the main Erkal paper here(https://drive.google.com/drive/folders/1iIhYLN6NOWi-f9Q0OMuEL9nHa5YfHjDL)

There are 3 phases: compression, expansion and caustic. As the perturber approaches, it compresses the stream, but somehow that eventually turns into an expansion and a gap - I guess as some sort of rebound after it shrinks? They claim (in sections 4 and 6) that this model is general for nonspherical orbits, and for realistic streams with distributions of energy and angular momentum.  However, it's unclear how "hand waivy" they have to get to do that, and I'm getting the sense the models are no longer analytic at that point.

In their convention, x is the direction radially out from the halo, y is the direction of the stream, and z is perpendicular to both of those.

We're assuming the flyby is quick, so the impulse approximation holds. If this is true for cdm, it should be valid for all models. Using this, they write
![](https://i.imgur.com/Zi3FPyt.png)

In the first integral this is essentially $(r^2 +r_s^2)^{3/2}$. The perturber is by definition starting at a distance b from the stream, which is in the x-z plane. Then, for a specific particle in the stream at a distance y above the chosen origin, the y distance will be $y+\omega_{\parallel}t$ where $\omega_{\parallel}$ is the relative velocity in the y direction. The impact paremater and relative velocity are perpendicular, so there are no cross terms between b and $\omega_{\perp}$. $r_s$ is the scale velocity for the plummer potential. This is multiplied by a $cos(\theta)$ like in any kinematics problem, which is where the other factors come from. The integrals seem to make sense, but I didn't work them.
We also have:
![](https://i.imgur.com/261wZce.png)
I think the $\Delta r$ term is the reason gaps form.

$r_s$ is the plummer sphere radius variable, while $r_0$ is the unperturbed radius of the orbit.

## Our Work in NFW
In this work, we make a number of improvements on Erkal's work, most significantly using an NFW profile instead of Plummer Spheres. This, unfortunately, means very little can be treated analytically.  But, it is far more accurate, and back of the envelope calculations suggest that this can increase the expected gaps by a factor of roughly 10. This, among other changes, could drastically affect the feasibility of streams probing dark matter substructure. 

To start, we need the general field strength of an NFW halo:  
$$ a = 4 \pi G \rho^* R_s  \left( \frac{\mathrm{log}(1 + r/ R_s)}{r^2/R_s^2} -\frac{1}{r/R_s(1+r/R_s)}\right)$$
The impulse approximation means we assume no change in the position (of the stream) during the interaction - so we can compute the change in velocity assuming a fixed position.  Using this, we find, 
$$ r^2 = b^2 + w_\perp^2t^2+(y+w_\parallel t)^2, $$ 

$$ \Delta v_x =  \int_{-\infty}^{\infty} dt \frac{b_x +w_x t}{r} a(r(t)),$$ and  
$$ \Delta v_y =  \int_{-\infty}^{\infty} dt \frac{y +w_\parallel t}{r} a(r(t))$$ 
Currently, $\Delta v_z$ is not for gap statistics. 

These must be evaluated numerically. From here, we evaluate 
![](https://i.imgur.com/iIM9fEl.png)
which is not necessarily accurate for large gap sizes, but is sufficient for now. As in Erkal's work
 $$ \psi = \psi_0 + \Delta\theta(\psi_0, t), $$
 and  $$ f = \bigg\lvert \frac{\partial\psi}{\partial \psi_0} \bigg\rvert^{-1} $$



For our other improvements, we now are getting the subhalo population directly from Galcticus. Instead of using equations 11-15 in Erkal (2016), all subhalo statistics are a result of N-body simulation, which are in principle nonseparable and non-analytic. This, again, should provide much improved results, but the specific gains are hard to quanitify at this stage. Another advantage is that it will be incredibly easy to substitute in WDM or other subhalo statitics. Profiles beyond NFW could also be included with little trouble, so there is hope that the full range of dark matter candidates can be tested well. There is still some question about whether only infalling halos contribute to gap statistics, but for now we follow Erkal's conditions. Similarly, we clean for only velocity kicks, $\Delta v_y > .1  \mathrm{ km/s}$, because if the velocity kick is smaller than the prexisting velocity dispersion, these changes aren't necessarily meaningful. $\Delta \Psi$ and f are defined the same as they are in Erkal 2014 and Erkal 2016, but with an NFW version of eqn 14 (of Erkal 2014) instead of the approximated plummer version. Plummer spheres are less dense for computational simplicity, so it makes sense that they would create less strong scattering events.  Velocity data is provided by Galacticus, but radial velocities are weighted $\propto v_r$, as in equation 6 of Erkal 2016. This is done because infalling subhalos with larger radial velocities are more likely to pass by our stream in a given time interval than their slower moving counterparts. The resulting $\omega$(relative velocity) statistics are almost identical to Erkal's findings, even though our data is drawn directly from simulation.  Finally, since large scale anisotropies like the LMC have not been incorporated into this work(a possiby significant limitation), the Milky Way is essentially isotropic. Thus, we can "rotate" the relative positions of the subhalo population and a given stream by random rotation matrices without changing the underlying physics. By rotating into several separate frames, we're able to extract more gap statistic information out of each realization, improving the quality of our result.
In a given coordinate system of the galaxy, the stream is definited to be in the x direction, while it's velocity is in the y direction. Namely, the stream is located at $(x,y) = (R_0, 0)$. Thus $$\omega_\parallel = v_y - v_{\mathrm{stream}}, $$ $$\omega_\perp = \sqrt{v_x ^2 + v_z ^2} $$ 

Galacticus calculates the subhalo population at  evenly spaced timesteps between the stream's formation and now(for now 10 time inverals). In a 'rectangular' summation, the population is assumed to represent all interactions between this timestep and the next one. Gap statistics and histograms are computed at each timestep, and then weighed according to the length of the stream, which grows linearly with time.  Mathematically these histograms are weighed as: 
$$ h = \frac{\sum_i h_i * t_i} {\sum_i t_i} $$

 This  gives more accurate subhalo statistics along the whole formation history of the stream.  For the final prediction of total gaps, $N(f)$, we'll instead perform a crude integral of 
 $$N(f) =\sum_i N_i(f) \Delta t_i $$