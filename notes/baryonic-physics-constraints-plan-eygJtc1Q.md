# Baryonic Physics Constraints Plan

###### status: `active` · last reviewed: TBD

###### tags: `baryonic physics` `emission lines` `parameters` `constraints`

## Overview

Goal is to construct a set of constraints that can be used to calibrate key model properties for emission lines work.

## Plan

**Bold** indicates questions that we need to figure out answers to.
*Italic* indicates possibly good places to work next.
[AJB] indicates who is working on this step.

* Mass-metallicity relation
    * This already exists in the `outputAnalysisMassMetallicityBlanc2019` class in `source/output.analyses.mass_metallicity_relation.Blanc2019.F90`
    * [AJB] *Add to the current constraints pipeline*
        * *Estimate random and systematic error model priors?*
* Black hole mass-velocity dispersion relation
    * *Find a suitable observational sample*  
        * Would [McConnel & Ma (2013)](https://ui.adsabs.harvard.edu/abs/2013ApJ...764..184M) sample work?
    * *Implement an `outputAnalysis` class for this* (In progress...)
        * Use the `outputAnalysisBlackHoleBulgeRelation` class in `source/output.analyses.black_hole_bulge_relation.F90` as an template 
    * New class for balck hole mass velocity dispersion implemented. 
        * Needs fixing
    * Add to the current constraints pipeline
        * Estimate random and systematic error model priors
* Star formation rate function
    * Find a suitable observational sample Robotham 2011. Started creating the hdf5 file
    * Implement an `outputAnalysis` class for this (Completed, PR to github)
        * Use the `outputAnalysisMassFunctionStellar` class (and child classes) in `source/output.analyses.mass_function_stellar.F90` as an template

* Updated $H_{\alpha}$ luminosity function - Sobral+2013 to work with updated emission line class
    * Accounts for evolution of redshift interval
    * Details?
* New output analyses classes for OII luminosity function, and NII luminosity function for data from Favole+2024

IN PROGRESS
    * Add to the current constraints pipeline
        * Estimate random and systematic error model priors
