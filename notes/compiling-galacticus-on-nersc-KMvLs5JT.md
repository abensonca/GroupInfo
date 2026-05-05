# Compiling Galacticus on NERSC

###### status: `reference` · last reviewed: TBD

###### tags: `build` `computing` `NERSC`

NERSC is an external resource on which we run Galacticus. It has all of the tools and libraries needed to compile and run Galacticus pre-installed, so building your own copy of Galacticus is generally straightforward.

Some basic information on Caltech HPC:
* [Login](https://docs.nersc.gov/connect/)
* [Resources](https://docs.nersc.gov/systems/perlmutter/architecture/)

(These notes are always a work in progress - if something doesn't work either ask [Andrew](mailto:abenson@carnegiescience.edu) for help or, if you figure out a solution, update the notes.)

## Setting environment variables

You'll need to set the following environment variables to allow the various libraries to be found and to set appropriate build options:

```
export PATH=/global/cfs/cdirs/m4943/Galacticus/buildTools/gcc-12/bin:/global/cfs/cdirs/m4943/Galacticus/buildTools/bin:$PATH
export LD_LIBRARY_PATH=/global/cfs/cdirs/m4943/Galacticus/buildTools/lib:/global/cfs/cdirs/m4943/Galacticus/buildTools/lib64:/lib:/lib64:$LD_LIBRARY_PATH
export GALACTICUS_FCFLAGS="-fintrinsic-modules-path /global/cfs/cdirs/m4943/Galacticus/buildTools/finclude -fintrinsic-modules-path /global/cfs/cdirs/m4943/Galacticus/buildTools/lib -fintrinsic-modules-path /global/cfs/cdirs/m4943/Galacticus/buildTools/include -fintrinsic-modules-path /global/cfs/cdirs/m4943/Galacticus/buildTools/include/gfortran -fintrinsic-modules-path /global/cfs/cdirs/m4943/Galacticus/buildTools/lib/gfortran/modules -L/global/cfs/cdirs/m4943/Galacticus/buildTools/lib -L/global/cfs/cdirs/m4943/Galacticus/buildTools/lib64"
export GALACTICUS_CFLAGS="-I/global/cfs/cdirs/m4943/Galacticus/buildTools/include"
export GALACTICUS_CPPFLAGS=-I/global/cfs/cdirs/m4943/Galacticus/buildTools/include"
export PERL5LIB="/global/cfs/cdirs/m4943/Galacticus/buildTools/perl5/lib/perl5${PERL5LIB:+:${PERL5LIB}}"
```

I'd suggest placing these into your `.bashrc` file (or creating a function in there which sets these so you can easily run that function when you need to). Note that if you do this you'll need to either log out and back in, or enter these commands at the command line also for them to take effect right away.

### Note for `gcc-latest` version (2026)

If you are building a version of Galacticus on the [`gfortranFinalization`](https://github.com/galacticusorg/galacticus/tree/gfortranFinalization) branch you will need to adjust these settings, replacing the above with:
```
export PATH=/global/cfs/cdirs/m4943/Galacticus/buildTools_gcc-latest/bin:/global/cfs/cdirs/m4943/Galacticus/buildTools/gcc-12/bin:/global/cfs/cdirs/m4943/Galacticus/buildTools/bin:$PATH
export LD_LIBRARY_PATH=/global/cfs/cdirs/m4943/Galacticus/buildTools_gcc-latest/lib:/global/cfs/cdirs/m4943/Galacticus/buildTools_gcc-latest/lib64:/lib:/lib64:/global/cfs/cdirs/m4943/Galacticus/buildTools/lib:/global/cfs/cdirs/m4943/Galacticus/buildTools/lib64:/lib:/lib64:$LD_LIBRARY_PATH
export GALACTICUS_FCFLAGS="-fintrinsic-modules-path /global/cfs/cdirs/m4943/Galacticus/buildTools_gcc-latest/finclude -fintrinsic-modules-path /global/cfs/cdirs/m4943/Galacticus/buildTools_gcc-latest/lib -fintrinsic-modules-path /global/cfs/cdirs/m4943/Galacticus/buildTools_gcc-latest/include -fintrinsic-modules-path /global/cfs/cdirs/m4943/Galacticus/buildTools_gcc-latest/include/gfortran -fintrinsic-modules-path /global/cfs/cdirs/m4943/Galacticus/buildTools_gcc-latest/lib/gfortran/modules -fintrinsic-modules-path /global/cfs/cdirs/m4943/Galacticus/buildTools/finclude -fintrinsic-modules-path /global/cfs/cdirs/m4943/Galacticus/buildTools/lib -fintrinsic-modules-path /global/cfs/cdirs/m4943/Galacticus/buildTools/include -fintrinsic-modules-path /global/cfs/cdirs/m4943/Galacticus/buildTools/include/gfortran -fintrinsic-modules-path /global/cfs/cdirs/m4943/Galacticus/buildTools/lib/gfortran/modules -L/global/cfs/cdirs/m4943/Galacticus/buildTools/lib -L/global/cfs/cdirs/m4943/Galacticus/buildTools_gcc-latest/lib64 -L/global/cfs/cdirs/m4943/Galacticus/buildTools/lib64"
export GALACTICUS_CFLAGS="-I/global/cfs/cdirs/m4943/Galacticus/buildTools_gcc-latest/include -I/global/cfs/cdirs/m4943/Galacticus/buildTools/include"
export GALACTICUS_CPPFLAGS="-I/global/cfs/cdirs/m4943/Galacticus/buildTools_gcc-latest/include -I/global/cfs/cdirs/m4943/Galacticus/buildTools/include"
export PERL5LIB="/global/cfs/cdirs/m4943/Galacticus/buildTools/perl5/lib/perl5${PERL5LIB:+:${PERL5LIB}}"
```

## Getting Galacticus

I suggest that you place the Galacticus source code and datasets into a directory in your home directory. So, first create and enter that directory:

```
mkdir Galacticus
cd Galacticus
```

You can then retrieve Galacticus and datasets from GitHub:

```
git clone https://github.com/galacticusorg/galacticus.git
git clone https://github.com/galacticusorg/datasets.git
```

You'll need to set environment variables to point to the locations of these:

```
export GALACTICUS_EXEC_PATH=$HOME/Galacticus/galacticus
export GALACTICUS_DATA_PATH=$HOME/Galacticus/datasets
```

You may want to put these `export` commands in your `.bashrc` also so that you don't have to re-enter them every time.

Galacticus generates a bunch of files at run-time which get stored in `$GALACTICUS_DATA_PATH/dynamic`. Since these can become quite large I suggest moving the `dynamic` directory to a scratch disk and creating a link to it. For example:

```
cd $GALACTICUS_DATA_PATH
mkdir -p dynamic /resnick/groups/carnegie_poc/$USER/
mv dynamic /resnick/groups/carnegie_poc/$USER/
ln -sf /resnick/groups/carnegie_poc/$USER/dynamic
```

## Building Galacticus

You should now be able to build Galacticus:

```
cd $GALACTICUS_EXEC_PATH
make -j2 Galacticus.exe
```

The build takes quite a while (~30 minutes). If it succeeds you'll have a `Galacticus.exe` executable file.

It's useful to run a very quick test to make sure it's all working:

```
./Galacticus.exe parameters/quickTest.xml
```

## Building the Library and Python Module

Building the Galacticus library and Python module (so you can use Galacticus in a Jupyter notebook for example) can be done using:
```
make -j2 GALACTICUS_BUILD_OPTION=lib libgalacticus.so
```
See [here](https://github.com/galacticusorg/galacticus/wiki/Python-interface-%28experimental%29) for more details.