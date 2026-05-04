# Emission Line Modeling

###### tags: `emissionLines`

I've been working on improving the emission line modeling in Galacticus. I think this has resulted in some improvements, but it's still far from perfect.

There are essentially two components to the process of predicting emission lines from Galacticus, both of which need to be correct to get reasonable results:

1. Tables of emission line luminosities from individual HII regions as a function of (metallicty, density, stelalr SED) computed using Cloudy;
2. Galaxy properties (gas-phase metallicity, stellar SED, density) predicted by Galacticus.

The Galacticus galaxy properties are used to interpolate in the Cloudy tables to find emission line luminosities for each galaxy.

## HII Region models

I've updated the way the Cloudy models are generated, largely motivated by the work of [Yeh et al. (2013)](https://ui.adsabs.harvard.edu/abs/2013ApJ...769...11Y/abstract) which was recommended by Jarle Brinchmann.

### Model Specification

A summary of the changes are as follows:

1. Update to the latest Cloudy code (version 17.02);
2. Reparameterize the high-energy stellar SED in terms of $Q(\mathrm{O})/Q(\mathrm{He})$ rather than $Q(\mathrm{O})/Q(\mathrm{H})$ (which avoids unphysical cases where $Q(\mathrm{O}) > Q(\mathrm{He})$);
3. Ranges of $Q(\mathrm{He})/Q(\mathrm{H})$ and $Q(\mathrm{O})/Q(\mathrm{He})$ were chosen to span the typical range for young ($<10$Myr) stellar populations;
4. Use Cloudy's "ISM" abundances model, including dust grains;
5. Assume constant pressure (including gravity), i.e. hydrostatic models;
6. Set an inner radius to the HII region base d on the characteristic radius [(Yeh et al. 2013; eqn. 1)](https://ui.adsabs.harvard.edu/abs/2013ApJ...769...11Y/abstract).

### Diagnostic Plots

To test whether these new models span a sufficient range of physical conditions I constructed various line-ratio diagnostic plots. 

In each plot the distribution of star forming galaxies from the SDSS is shown by the contours. SDSS DR14 data are taken from the [MPA-JHU catalog](https://www.sdss.org/dr14/spectro/galaxy_mpajhu/).

Our Cloudy models are shown by points. Point color indicates metallicity from $10^{-3}\mathrm{Z}_\odot$ (red) to $3\mathrm{Z}_\odot$ (blue). Point size indicates $\log_{10}[Q(\mathrm{He})/Q(\mathrm{H})]$ from $-2.6$ (smallest) to $-0.44$ (largest).

![](https://i.imgur.com/QPEnSB3.png)
![](https://i.imgur.com/spJRvKT.png)
![](https://i.imgur.com/Pvt4vxn.png)
![](https://i.imgur.com/Qr1OzWl.png)
![](https://i.imgur.com/JdwH6jC.png)
![](https://i.imgur.com/yCS6drg.png)

In all cases the Cloudy models seem to span the distribution of the SDSS galaxies (for metallicities that are reasonable for such galaxies), and in many cases they also follow the overall shape of the contours.

This suggests that this set of Cloudy models is reasonable.

## Galacticus Galaxies

The next step then is to generate Galacticus galaxies, use their properties to interpolate in the Cloudy tables, and figure out the resulting line ratios.

I ran a model outputing star-forming galaxies in the range $0.0 < z < 0.3$ with masses $M_\star > 10^9\mathrm{M}_\odot$---approximately representative of SDSS galaxies.

### "Original" Model

In our previous work we've used a simple model in which we compute the total ionizing luminosity in the H, He, and O continuua for each galaxy, assuming a single HII region mass. This means that $Q(\mathrm{H})$ has little variation from galaxy to galaxy, and that the ratios $Q(\mathrm{He})/Q(\mathrm{H})$ and $Q(\mathrm{O})/Q(\mathrm{He})$ are just the mean values for young (< 10 Myr) stellar populations.

The diagnostic diagrams are shown below - colors indicate metallicity as in the Cloudy diagnostic diagrams above. 

![](https://i.imgur.com/32Tpc9s.png)
![](https://i.imgur.com/YLSzLQ3.png)
![](https://i.imgur.com/5y8Q60y.png)
![](https://i.imgur.com/qGVa19V.png)
![](https://i.imgur.com/uf578ne.png)
![](https://i.imgur.com/QhbFTfz.png)

Overall, these models clearly don't match the peak of the distribution of SDSS galaxies.

### Improved Model

In this model I make two significant changes:
1. The young (< 10 Myr) stellar population of each galaxy is resolved into 10 sub-populations in bins of age of 1 Myr. I then find the emission line strengths due to emission in each age bin and sum them to get the total. Since the ratios $Q(\mathrm{He})/Q(\mathrm{H})$ and $Q(\mathrm{O})/Q(\mathrm{He})$ vary rapidly over the 0-10 Myr age range this gives better sampling of the possible line ratios if we have HII regions of different ages in the galaxy.
2. I assumed a distribution of HII region masses, with a simple power-law mass function and integrated over all HII region masses. This leads to a range of $Q(\mathrm{H})$ in each galaxy.

The diagnostic diagrams are shown below.

![](https://i.imgur.com/vocTopz.png)
![](https://i.imgur.com/r3HpDBA.png)
![](https://i.imgur.com/U0ygU9a.png)
![](https://i.imgur.com/a5aP0nV.png)
![](https://i.imgur.com/x8nbXzo.png)
![](https://i.imgur.com/W429WNs.png)

There's some improvement here - for example in the [O III]/[H$\beta$] vs. [S II]/[H$\alpha$] diagram there's now a much more reasonable range of [O III][H$\beta$]. But, the results are still not all that good.

For example, there's a very strong correlation between [S II] and [N II] which results in an almost constant ratio for these lines. By looking in the Cloudy models it seems that maybe we're missing models with sufficiently low $Q(\mathrm{O})/Q(\mathrm{He})$ to population the higher ratios. But that is constrained by our stellar population spectra - low ratios of $Q(\mathrm{O})/Q(\mathrm{He})$ occur for the older (i.e. close to 10 Myr) populations, but for those the overall HII region luminosity is much lower than for younger populations so they don't contribute much to the total

## Possible Extensions

The current model isn't super successful - there are clear offsets in line ratios from the SDSS data.

Maybe we need to account for stochasticity in the HII regions - although this seems unlikely to be a significant effect in galaxies which contains 100's or 1000's of HII regions.

Possibly our model galaxies just don't have the correct properties (e.g. metallicities, gas densities, etc.).

Maybe younger populations are more strongly dust-attenuated so that their contribution is down-weighted.