# Emission Lines for OpenUniverse Work

###### status: `active` · last reviewed: TBD

###### tags: `emission lines` `baryonic physics`

## Required lines for _Roman_

The _Roman_ telescope does relatively low resolution spectroscopy using either a prism or a grism (see [here](https://roman.gsfc.nasa.gov/science/WFI_technical.html)):
* Prism: $7,500Å < \lambda < 18,000Å$; $\lambda/\Delta\lambda = 100$;
* Grism: $10,000Å < \lambda < 19,300Å$; $\lambda/\Delta\lambda = 600$.

For redshift determination two lines are needed, which will depend on the redshift interval:
* Primary lines:
  * $0.15 < z < 2.0$ - H$\alpha$ is within the wavelength range;
  * $0.50 < z < 2.9$ - [OIII] is within the wavelength range;
* Secondary lines:
  * [OIII] can act as the secondary line to H$\alpha$ for $0.5 < z < 2.0$;
  * $1.0 < z < 4.2$ - [OII] is within the wavelength range so can act as the secondary line to [OIII].
  * $z < 0.5$ - [SIII] is within the wavelength range so can act as a secondary line to H$\alpha$.

Because of the relatively low resolution these lines will be contaminated. For example H$\alpha$ will be contaminated by [NII], while [OIII] may be contaminated by H$\beta$ in prism observations.

Specific lines that we need to accurately model then are:

* H$\alpha$ 6565Å - primary ELG redshift line for _Roman_ HLSS at $z<2$;
* [OIII] 4933Å, 4960Å, 5008Å - primary ELG redshift line for _Roman_ HLSS at $z > 2$; secondary ELG redshift line for _Roman_ HLSS at $z<2$;
* [SIII] 9071Å, 9533Å - secondary ELG redshift line for _Roman_ HLSS at $z<0.5$;
* [OII] 3727Å, 3730Å - secondary ELG redshift line for _Roman_ HLSS at $z>2$; 
* H$\beta$ 4863Å - contaminant for _Roman_ HLSS primary line [OIII]
* [NII] 6550Å, 6585Å- contaminant for _Roman_ HLSS primary line H$\alpha$;

## Line Modelling Considerations

* [NII] - the ionization energy of neutral nitrogen is only 14.53 eV, so N II exists in both ionized and neutral ISM phases - it will be non-trivial to model this line, so maybe it is better to just use Cloudy and do interpolation;
* [SIII] - The ground electron configuration for S III is 1s$^2$ 2s$^2$ sp$^6$ 3s$^2$ 3p$^2$, so it must have 5 energy levels identical to the O III ion - it should be easy to add this into our current model model.

## Sub-grid Model for SAMs

1. From Shengqi's study of the FIRE simulations: OIII and H$\beta$ lines mostly come from HII regions near star particles with $Q>10^{50} \mathrm{s}^{-1}$, while HII regions sourced by fainter star particles with $Q \sim 10^{48} \mathrm{s}^{-1}$ can be important for OII lines.
2. From Shengqi's study of the FIRE simulations: $V_\mathrm{OII}/V_\mathrm{HII}$ (the volume ratio of OII and HII regions) shows a strong correlation with $\log Q$, so it is wrong to model a galaxy as one big HII region and use the galaxy-wide total $Q$ to compute $L_\mathrm{OII}$. In this case Cloudy will derive a very small $V_\mathrm{OII}/V_\mathrm{HII}$ fraction and underestimate the OII line luminosity.
3. Any sub-grid model probably then needs to consider a spectrum of HII regions, with some distribution function in age and $Q$ (for example), over which the results of the fine-grained model are averaged.
4. We may need to have some escape fraction for HII regions - some fraction of photons escape from the HII region through low density channels. This would weaken the emission lines (and nebular continuum), and would also allow more ionizing photons to escape the galaxy.(Based on Dan Stark's talk at RSE@70.)

## Dust Models

* Previously we have ignored dust grains in the HII regions by switching them off in Cloudy;
* Dust extinction has mostly been treated using models similar to that of [Charlot & Fall (2003)](http://adsabs.harvard.edu/abs/2000ApJ...539..718C).

## Available Datasets for Constraining Models

* H$\alpha$ - luminosity functions at different redshifts are given by [Sobral et al. (2013)](http://adsabs.harvard.edu/abs/2013MNRAS.428.1128S) and [Gunawardhana et al. (2013)](http://adsabs.harvard.edu/abs/2013MNRAS.433.2764G) (both already coded up in Galacticus)
* [SIII] - [Kehrig et al. (2006)](https://ui.adsabs.harvard.edu/abs/2006A%2526A...457..477K) - has the [SIII]9069 line flux for 34 galaxies (see Table 1), relative to H$\beta$. 

## Current Implementation in Galacticus

Currently, Galacticus interpolates in a table of Cloudy models to estimate emission line luminosities. The tables is a function of density $n_\mathrm{H}$, metallicity $Z$, and the ionizing fluxes in the H, He, and O continuua. This was motivated by the work of [Panuzzo et al. (2003)](http://adsabs.harvard.edu/abs/2003A%26A...409...99P).

Some problems that I'm aware of with this implementation:
* There is no sub-grid model - was we have to make some guess for the properties of HII regions, and there's not a good treatment of variation in the HII region luminosity, metallicity, density, etc.
* We probably need a better calculation of the spectra of the ionizing stars. Originally I just used the integrated spectrum of the galaxy, but really we just want the young stars (that are still in HII regions). This can be computed in Galacticus, but maybe we also need to account for a range of HII region ages?

### Existing Publications

* [Merson et al. (2018)](https://ui.adsabs.harvard.edu/abs/2018MNRAS.474..177M) "Predicting Hα emission-line galaxy counts for future galaxy redshift surveys";
* [Zhai et al. (2019)](https://ui.adsabs.harvard.edu/abs/2019MNRAS.490.3667Z) "Prediction of Hα and [OIII] emission line galaxy number counts for future galaxy redshift surveys"