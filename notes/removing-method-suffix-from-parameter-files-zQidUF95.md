# Removing "Method" Suffix from Parameter Files

###### tags: `parameters`

[This]([f483d9caf532e5f33cdbe46aad53d076316ec394](https://github.com/galacticusorg/galacticus/commit/f483d9caf532e5f33cdbe46aad53d076316ec394)) patch removed the use of the "`Method`" suffix from class names in parameter files. So, for example `cosmologyParametersMethod` becomes just `cosmologyParameters`. The "`Method`" suffix was needed long ago when Galacticus was first developed, but for a long time now it's just been an annoyance.

The patch also changes parameter which specify which type of galactic component to use to represent a galaxy/halo. So, for example, `treeNodeMethodDisk` becomes `componentDisk`, which is hopefully more descriptive.

Updating parameter files to match these changes can be done easily enough at the command line. To update a single file use:
```
perl -pi -e 's/<((?!readSubhaloAngularMomenta|subhaloAngularMomenta|diskRadiusSolverCole2000|duttonMaccio2014DensityContrast|duttonMaccio2014DensityProfile).+)Method(\s+value)/<\1\2/g; s/<\/(.+)Method>/<\/\1>/g; s/<treeNodeMethod([a-zA-Z]+ )/<component\1/g; s/<\/treeNodeMethod([a-zA-Z]+)>/<\/component\1>/g' parameters.xml
```
replacing `parameters.xml` with the name of your file.

To update all `*.xml` files in a given path you can use:
```
find myPath -name "*.xml" | xargs -n 1 perl -pi -e 's/<((?!readSubhaloAngularMomenta|subhaloAngularMomenta|diskRadiusSolverCole2000|duttonMaccio2014DensityContrast|duttonMaccio2014DensityProfile).+)Method(\s+value)/<\1\2/g; s/<\/(.+)Method>/<\/\1>/g; s/<treeNodeMethod([a-zA-Z]+ )/<component\1/g; s/<\/treeNodeMethod([a-zA-Z]+)>/<\/component\1>/g'
```
replacing `myPath` with the path containing the `*.xml` files that you'd like to update.

(I'd recommend making backups of any files before you update them in this way, just in case something goes wrong.)