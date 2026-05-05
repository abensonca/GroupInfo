
# Emission Lines Model Plan

###### status: `active` · last reviewed: TBD

###### tags: `emission lines` `baryonic physics`

## Overview

Goal is to construct a model for emission lines that produces plausible distributions of line luminosities - and so gets close to the observed distributions in observables such as the BPT diagram and emission line luminosity functions.

## Plan

**Bold** indicates questions that we need to figure out answers to.
*Italic* indicates possibly good places to work next.
[AJB] indicates who is working on this step.

* Model components
    * Cloudy table
        * [AJB] *Build a table using each SSP from a provided SSP file (e.g. FSPS) as the source spectrum - these will be a function of population age and metallicity*
        * See discussion from Jarle Brinchman in [this](https://github.com/galacticusorg/galacticus/issues/123) issue, and in particular the Cloudy set up described in [Gutkin, Charlot & Bruzual (2016)](https://ui.adsabs.harvard.edu/abs/2016MNRAS.462.1757G).
            * Useful discussion of abundance ratios, depletion factors, etc.
        * Tabulate over:
            * $Q_\mathrm{H}$ - these can be set directly in the Cloudy parameter file
            * $n_\mathrm{H}$ - **do we want to include this?**
            * log normal distribution? COMPILED, needs testing exponential? based on observations
    * `nodePropertyExtractor`(In progress...)
        * Use the SFH of each galaxy to sum over all stellar ages/metallicities for each emission line DONE
        * First reduce the Cloudy table by averaging over distribution functions of $Q_\mathrm{H}$ and (**possibly?**) $n_\mathrm{H}$ - reduced $Q_\mathrm{H}$ DONE
            * See [this](https://github.com/galacticusorg/galacticus/issues/123) issue
        * Build templates of linear weights by which to multiply the SFH to get the line luminosity
            * The `nodePropertyExtractorSED` class in `source/nodes.property_extractor.SED.F90` does something similar for computing SEDs from SSP spectra DONE
        * What is needed?
            * *New class providing the HII region luminosity function, $\phi(Q_\mathrm{H})$;* DONE
            * New class providing the distribution of $n_\mathrm{H}$; DONE
            * *New class providing the escape fraction of ionizing photons;*
                * This can be simple initially - e.g. assume a single value independent of population age/metallicity - but allow for dependence on these parameters
            * **Possibly?** A model for the fraction of stars remaining in their birth clouds.
    * **AGN spectrum and emission line model?**
        * Emission through AGNs are implemented in GAEA SAM (https://arxiv.org/pdf/2402.03436) using the method by Feltre et al 2016 (https://ui.adsabs.harvard.edu/abs/2016MNRAS.456.3354F/abstract). But they only model Type 2 AGN. 
            * Type 1 vs type 2 AGN?
            * In reality fraction of AGN would be broadline Type 1
            * High densities $n_H>10^9\,cm^{-3}$
            * Forbidden optical transitions are disfavoured.
            * Only Balmer lines are strong
* Constraints
    * Emission line luminosity functions
        * **Which luminosity functions should be included?**
        * Implement `outputAnalysis` classes for each luminosity function
            * Could generalize the `outputAnalysisLuminosityFunctionHalpha` class in `source/output.analyses.luminosity_function.Halpha.F90` to work for other emission lines;
            * Then just need a child class for each specific luminosity function that we want to use as a constraint, e.g. like the `outputAnalysisLuminosityFunctionGunawardhana2013SDSS` in `source/output.analyses.luminosity_function.Halpha.Gunawardhana2013.SDSS.F90`
                * Updating the current files to work with new emission line luminosity class/
    * Line ratio (BPT) diagnostics (In progress...)
        * **How should we compare model and data in these?**
        * **What metric should be used?**
        * Note: Metallicity cut of $7.67\leq 12 + \mathrm{log}_{10}(\mathrm{O/H}) \leq 9.5$ seem to select galaxies in the star forming region for SDSS galaxies (see left panel of figure).
![BPT_obs_SDSSDR7_Galacticus_recent30_sSFR_zmask](https://hackmd.io/_uploads/H1oTEunET.png)

## Notes on account for the number of HII regions

The Cloudy table provides us with the line luminosity per HII region, as a function of age, metallicity, and ionizing photon luminosity. Call this $\mathcal{L}_\lambda(t,Z,Q_\mathrm{H})$. This is in the `lines/balmerAlpha6565` dataset for H$\alpha$ for example.

It also gives us the ionizing photon luminosity per Solar mass for a population of stars as a function of age and metallicity. Call this
$$
q_\mathrm{H}(t,Z) \equiv \frac{Q_\mathrm{H}}{M_\star}
$$
and is in the `ionizingLuminosityHydrogenNormalized` dataset.

In our new class, we compute the mean ionizing luminosity per HII region by averging $Q_\mathrm{H}$ over the HII region luminosity function. Call this $\langle Q_\mathrm{H} \rangle$.

Last, Galacticus tells us the mass of stars formed at a given age and metallicity. Call this $M_\star(t,Z)$.

The total ionizing luminosity produced by the stars of given age and metallicity, is just the luminosity per unit mass, times the mass of such stars:
$$
q_\mathrm{H}(t,Z) M_\star(t,Z)
$$
To find the number of HII regions of this age and metallicity, we just divide this ionizing luminosity by the ionizing luminosity per HII region (on average):
$$
\frac{q_\mathrm{H}(t,Z) M_\star(t,Z)}{\langle Q_\mathrm{H} \rangle}
$$
Then the total line luminosity due to stars of this age and metallicity, $L_\lambda(t,Z)$, is found by multiplying the line luminosity from a single HII region by the number of HII regions:
$$
L_\lambda(t,Z) = \mathcal{L}_\lambda(t,Z) \frac{q_\mathrm{H}(t,Z) M_\star(t,Z)}{\langle Q_\mathrm{H} \rangle}
$$

Currently in the new emissions line class I think what we have is:
$$
L_\lambda(t,Z) = \mathcal{L}_\lambda(t,Z) M_\star(t,Z)
$$
so we're missing the part where we weight by $q_\mathrm{H}(t,Z) / \langle Q_\mathrm{H} \rangle$.

To fix this, we'll first need to read in the dataset `ionizingLuminosityHydrogenNormalized` from the Cloudy table to give us $q_\mathrm{H}(t,Z)$, and then we'll need to compute $\langle Q_\mathrm{H} \rangle$ from the HII region luminosity function.

Then, in the function `emissionLineLuminosityIntegrandTime` we currently have:
```
emissionLineLuminosityIntegrandTime=+emissionLineLuminosityIntegrandTime &
                 & +self%luminositiesReduced(interpolateIndexTime(iTime),interpolateIndexMetallicity(iMetallicity),iLine)&
                 & *interpolateFactorTime(iTime) &
                 & *interpolateFactorMetallicity(iMetallicity)
```
which is effectively averaging the $\mathcal{L}_\lambda(t,Z)$ term over a bin of age and metallicity. We can include the new factors here:
```
emissionLineLuminosityIntegrandTime=+emissionLineLuminosityIntegrandTime &
                 & +self%luminositiesReduced(interpolateIndexTime(iTime),interpolateIndexMetallicity(iMetallicity),iLine)&
                 & *self%ionizingLuminosityHydrogenNormalized(interpolateIndexTime(iTime),interpolateIndexMetallicity(iMetallicity)) &
                 & /self%ionizingLuminosityHydrogenMean &
                 & *interpolateFactorTime(iTime) &
                 & *interpolateFactorMetallicity(iMetallicity)
```
where `self%ionizingLuminosityHydrogenNormalized` is the variable which we read the `ionizingLuminosityHydrogenNormalized` dataset into, and `self%ionizingLuminosityHydrogenMean` has the value of $\langle Q_\mathrm{H} \rangle$.

## Notes from Emission Lines Meeting (02/07/2024)
/usr/bin/time -v ./Galacticus.exe testSuite/parameters/benchmark_darkMatterOnlySubHalos.xml
Importance of accouning for redshift evolution of abundances - at high-$z$ the Fe abundance will be very sub-Solar - this affects the stellar spectra as Fe is the main source of opacity (so affects stellar structure and temperature). If we track the Fe abundance then, as a first order fix, we could just use stellar spectra for a metallicity based on Fe instead of total $Z$. This would require that our Cloudy table allows for different $Z_\mathrm{gas}$ and $Z_\star$.

Importance of variations in N/O ratio as a function of metallicity - this is calibrated observationally, and may be redshift dependent. Would need to build this into the HII region abundances when generating the Cloudy table.

Our HII region luminosity function is independent of age. This seems like a bad approximation as old populations will have very low $Q_\mathrm{H}$. Possibly a simple solution is just to assume that stars older than some $\tau_\mathrm{HII}$ simply do not produce emission lines at all (i.e. they are no longer in HII regions). We could handle this by creating a new class which provides the fraction of stars of a given age that remain within their birth clouds. (This would be useful for dust models also.)

## AGN Spectra Normalization (01/22/2025)

From [Feltre et al. (2016)](https://ui.adsabs.harvard.edu/abs/2016MNRAS.456.3354F/abstract) we are using an AGN spectrum:
$$
S_\nu \propto \left\{ \begin{array}{ll} \nu^\alpha & \hbox{if } 0.001 \le \lambda/\mu\mathrm{m} \le 0.25 \\  \nu^{-1/2} & \hbox{if } 0.25 < \lambda/\mu\mathrm{m} \le 10  \\ \nu^2 & \hbox{if } 10 < \lambda/\mu\mathrm{m}. \end{array} \right.
$$

The spectrum should be continuous, that is, the three segments should match up at the wavelength where they join. Let's write this as:
$$
S_\nu = \left\{ \begin{array}{ll} A_1 \nu^\alpha & \hbox{if } 0.001 \le \lambda/\mu\mathrm{m} \le 0.25 \\  A_2 \nu^{-1/2} & \hbox{if } 0.25 < \lambda/\mu\mathrm{m} \le 10  \\ A_3 \nu^2 & \hbox{if } 10 < \lambda/\mu\mathrm{m}, \end{array} \right.
$$
and define $\nu_{0.25}$ and $\nu_{10}$ as the frequencies corresponding to wavelengths of $0.25\mu$m and $10\mu$m respectively. Then, for continuity, we require that at $\nu_{0.25}$:
$$
A_1 \nu_{0.25}^\alpha = A_2 \nu_{0.25}^{-1/2}
$$
so $A_2 = A_1 \nu_{0.25}^{\alpha+1/2}$. At $\nu_{10}$ we require that:
$$
A_2 \nu_{10}^{-1/2} = A_3 \nu_{10}^2,
$$
so $A_3 = A_2 \nu_{10}^{-5/2} = A_1 \nu_{0.25}^{\alpha+1/2} \nu_{10}^{-5/2}$.

So, we can now write:
$$
S_\nu = A_1 \left\{ \begin{array}{ll}  \nu^\alpha & \hbox{if } 0.001 \le \lambda/\mu\mathrm{m} \le 0.25 \\  \nu_{0.25}^{\alpha+1/2} \nu^{-1/2} & \hbox{if } 0.25 < \lambda/\mu\mathrm{m} \le 10  \\ \nu_{0.25}^{\alpha+1/2} \nu_{10}^{-5/2} \nu^2 & \hbox{if } 10 < \lambda/\mu\mathrm{m}, \end{array} \right.
$$
If we now integrate this over all frequencies, and require that it be normalized to 1 (so that we can just multiply by the AGN luminosity of each individual black hole to get a normalized spectrum for that black hole) we have
$$
\int_0^\infty \mathrm{d}\nu S_\nu = 1.
$$
If we evaluate the intergral using the above form for $S_\nu$ we should get some number times $A_1$. So, we can then solve for $A_1$.



$$
Q=L_{AGN}\cdot\int_{\nu_L}^\infty \mathrm{d}\nu \frac{S_\nu}{h\nu}
$$

Where $h\nu_L=13.6\,\mathrm{eV}$

Stromgren radius $R_s$ is $$R_s^2=\frac{3Q}{4\pi{n_H}^2\epsilon \alpha_B}$$
The ionization parameter U is given by,
$$
U=\frac{Q}{4\pi{R_s}^2n_Hc}$$

$$U_S=\frac{{\alpha_B}^{2/3}}{3c}{\bigg(\frac{3Q\epsilon^2n_H}{4\pi}\bigg)}^{1/3}$$

Volume filling factor is $\epsilon$. For now we will leave this as a variable paramter with default value of 0.01.


# Results

Model with 100 trees per decade, assuming $n_H=1000cm^{-3}$ and volume filling factor of one.
![BPT_AGN_100](https://hackmd.io/_uploads/H1R67Lb_1x.png)

# Checkpoints

1.) Distribution of accretion rates/ eddington ratios

## Issue Resolved
The underlying issue was in the interpolation, specifically the order of interpolating variables