# Compiling Galacticus on Caltech HPC

###### status: `reference` · last reviewed: TBD

###### tags: `build` `computing` `Caltech HPC`

Caltech HPC is one of the primary resources on which we run Galacticus. It has all of the tools and libraries needed to compile and run Galacticus pre-installed, so building your own copy of Galacticus is generally straightforward.

Some basic information on Caltech HPC:
* [Login](https://www.hpc.caltech.edu/documentation/faq/how-do-i-login-cluster)
* [Resources](https://www.hpc.caltech.edu/resources)

(These notes are always a work in progress - if something doesn't work either ask [Andrew](mailto:abenson@carnegiescience.edu) for help or, if you figure out a solution, update the notes.)

## Build environment

You'll need to set the following environment variables to allow the various libraries to be found and to set appropriate build options:

```
export PATH=/home/abenson/perl5/bin:/home/abenson/Tools/bin:$PATH
export LD_LIBRARY_PATH=/home/abenson/Tools/lib:/home/abenson/Tools/lib64:$LD_LIBRARY_PATH
export GALACTICUS_FCFLAGS="-fintrinsic-modules-path /home/abenson/Tools/finclude -fintrinsic-modules-path /home/abenson/Tools/include -fintrinsic-modules-path /home/abenson/Tools/include/gfortran -fintrinsic-modules-path /home/abenson/Tools/lib/gfortran/modules -L/home/abenson/Tools/lib -L/home/abenson/Tools/lib64"
export GALACTICUS_CFLAGS="-I/home/abenson/Tools/include"
export GALACTICUS_CPPFLAGS="-I/home/abenson/Tools/include -I/home/abenson/Tools/include/libqhullcpp"
export PERL5LIB=/home/abenson/perl5/lib/perl5
```

I'd suggest placing these into your `.bashrc` file (or creating a function in there which sets these so you can easily run that function when you need to). Note that if you do this you'll need to either log out and back in, or enter these commands at the command line also for them to take effect right away.

### Note for older versions

If you are building a version of Galacticus prior to revision [a6a5c8c](https://github.com/galacticusorg/galacticus/commit/a6a5c8c3a3e96a1a9b9e49e75278790df784f07c) (released on 12/01/2024), you must use the older HDF5 library (v1.8.20). To do so, replace the above settings with:
```
export PATH=/home/abenson/perl5/bin:/home/abenson/Tools/bin:$PATH
export LD_LIBRARY_PATH=/home/abenson/Tools_HDF51.8.20/lib:/home/abenson/Tools_HDF5/lib64:/home/abenson/Tools/lib:/home/abenson/Tools/lib64:$LD_LIBRARY_PATH
export GALACTICUS_FCFLAGS="-I/home/abenson/Tools_HDF51.8.20/include -fintrinsic-modules-path /home/abenson/Tools_HDF51.8.20/include -fintrinsic-modules-path /home/abenson/Tools/finclude -fintrinsic-modules-path /home/abenson/Tools/include -fintrinsic-modules-path /home/abenson/Tools/include/gfortran -fintrinsic-modules-path /home/abenson/Tools/lib/gfortran/modules -L/home/abenson/Tools_HDF51.8.20/lib -L/home/abenson/Tools_HDF51.8.20/lib64 -L/home/abenson/Tools/lib -L/home/abenson/Tools/lib64"
export GALACTICUS_CFLAGS="-I/home/abenson/Tools_HDF51.8.20/include -I/home/abenson/Tools/include"
export GALACTICUS_CPPFLAGS="-I/home/abenson/Tools_HDF51.8.20/include -I/home/abenson/Tools/include -I/home/abenson/Tools/include/libqhullcpp"
export PERL5LIB=/home/abenson/perl5/lib/perl5
```

### Note for `gcc-latest` version (2026)

If you are building a version of Galacticus on the [`gfortranFinalization`](https://github.com/galacticusorg/galacticus/tree/gfortranFinalization) branch you will need to adjust these settings, replacing the above with:
```
export PATH=/home/abenson/perl5/bin:/home/abenson/Tools_gcc-latest/bin:/home/abenson/Tools/bin:$PATH
export LD_LIBRARY_PATH=/home/abenson/Tools_gcc-latest/lib:/home/abenson/Tools_gcc-latest/lib64:/home/abenson/Tools/lib:/home/abenson/Tools/lib64:$LD_LIBRARY_PATH
export GALACTICUS_FCFLAGS="-fintrinsic-modules-path /home/abenson/Tools_gcc-latest/finclude -fintrinsic-modules-path /home/abenson/Tools_gcc-latest/include -fintrinsic-modules-path /home/abenson/Tools_gcc-latest/include/gfortran -fintrinsic-modules-path /home/abenson/Tools_gcc-latest/lib/gfortran/modules -fintrinsic-modules-path /home/abenson/Tools/finclude -fintrinsic-modules-path /home/abenson/Tools/include -fintrinsic-modules-path /home/abenson/Tools/include/gfortran -fintrinsic-modules-path /home/abenson/Tools/lib/gfortran/modules -L/home/abenson/Tools/lib -L/home/abenson/Tools/lib64 -L/home/abenson/Tools_gcc-latest/lib -L/home/abenson/Tools/lib64"
export GALACTICUS_CFLAGS="-I/home/abenson/Tools_gcc-latest/include -I/home/abenson/Tools/include"
export GALACTICUS_CPPFLAGS="-I/home/abenson/Tools_gcc-latest/include -I/home/abenson/Tools/include -I/home/abenson/Tools/include/libqhullcpp"
export PERL5LIB=/home/abenson/perl5/lib/perl5
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

Caltech limits the amount of memory you can use on the login node - sometimes compilation will fail due to an `out of memory` error. If this happens, get a compute node interactively and compile there:
```
srun --pty -t 1:20:00 -n 1 -N 1 --cpus-per-task=16 /bin/bash -l
```
will get you 16 cores on a compute node - you can then compile on there with the usual `make -j16 Galacticus.exe`.

It's useful to run a very quick test to make sure it's all working:

```
./Galacticus.exe parameters/quickTest.xml
```

## Building the library and Python module

Building the Galacticus library and Python module (so you can use Galacticus in a Jupyter notebook for example) can be done using:
```
make -j2 GALACTICUS_BUILD_OPTION=lib libgalacticus.so
```
See [here](https://github.com/galacticusorg/galacticus/wiki/Python-interface-%28experimental%29) for more details.

## See also

- [Submitting Jobs on Caltech HPC](submitting-jobs-on-caltech-hpc-o4QFFb8Q.md)
- [Compiling Galacticus on OBS HPC](compiling-galacticus-on-obs-hpc-OOMa0kUW.md)
- [Compiling Galacticus on NERSC](compiling-galacticus-on-nersc-KMvLs5JT.md)