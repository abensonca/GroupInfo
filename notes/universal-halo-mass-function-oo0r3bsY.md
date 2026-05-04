# Universal Halo Mass Function

###### tags: `dark matter`

For the MW zoom-in mass functions, there is definitely a clear trend in the offset (between model prediction and measured HMF) and environmental overdensity, as shown in this plot (offset here is the mean $\log_{10}$ of the ratio of model to N-body mass function between masses of $10^7$ and $10^9\mathrm{M}_\odot$).

![](https://i.imgur.com/6LiLgaQ.png)

The overall offset (i.e. that the best fit line here would not go through 0,0) can be taken out by recalibrating the HMF fitting function. Looking at the most underdense case I don't see anything obviously wrong with the data from the simulation. 

![](https://i.imgur.com/1UmfBa8.png)

The image here shows the selected region (green sphere) with all selected halos shown as tiny colored spheres inside it. The blue dots are all $z=0$ halos from the Rockstar merger tree file - the select region seems to lie within the extent of these blue dots, so should be a reasonable region to use. The red points and shaded region are the volume in the initial conditions from which all particles in the selected $z=0$ region arise from. This also looks reasonable.

After some investigation, I think I understand the origin of this trend. I'm using the Bhattacharya mass function as the model here. It's Sheth-Tormen-like but allows for an additional modification to the exponent of the peak height at low masses. In the fit I'm using this exponent is 1.8, instead of 1.0 as it would be in Sheth-Tormen. Since the peak-background split model modifies the effective peak height this will lead to a stronger environment dependence in the Bhattacharya model than with Sheth-Tormen. Running the numbers for this it quantitatively explains the magnitude of the trend in offset with environmental overdensity. Sheth-Tormen would get much closer to the correct offset trend (i.e. no trend with environment), but would still not be perfect.

So, maybe this is actually a useful feature of this approach. If we require the peak-background split approach to work then it gives us some more leverage on what the peak height dependence in the mass function can be at low masses. It may mean that I need to generalize the fitting function to allow a successful match to be found, but that's not a problem.

So, I think the next steps in this project are:
Try fitting these HMFs (simultaneously with HMFs from cosmological boxes) and figure out how to get a good fit;
1. Extract similar HMFs from the LMC zoom-ins;
2. Possibly extract HMFs from MW and LMC zoom-ins at $z>0$;
3. Possibly extract HMFs from some of the non-CDM zoom-ins.

If there's a single mass function fit that can match all of the above across a wide range of mass, redshift, environment, and DM-type then I think that would be extremely powerful and useful.

## Investigation of systematics in high-mass, high-z MDPL mass functions

From [Klypin et al. (2016)](https://ui.adsabs.harvard.edu/abs/2016MNRAS.457.4340K/abstract) there's a clear bias between BigMDPL and MDPL simulations. Look at the $z=2.5$ line in this figure from the paper for example. The triangles (MDPL) are significantly higher than the circles (BigMDPL), by around 20%.

![](https://i.imgur.com/YQ12QNk.png)

I see something similar in my own analysis. At $z=2$ (top panel in the following) BigMDPL (yellow) is suppressed below MDPL2 (green). (Note that these are the mass functions normalized to the best-fit to MDPL2 at each redshift).

![](https://i.imgur.com/K1Hm3cx.png)

So, what does the model predict? Run model mass functions for MDPL2 and BigMDPL, and look at the ratio (BigMDPL/MDPL2) at $\log_{10}(M/\mathrm{M}_\odot)=13.05$ and $14.05$ as we vary parameters:

1. Identical parameter files ($z=2.000$): 1.0, 1.0
2. Redshifts back to the actual snapshots: 0.848, 0.625
3. Reintroduce cosmological cube power spectra: 0.848, 0.625
4. Reintroduce mass error convolution: 0.848, 0.625

So the largest effect is just the redshift offset.
