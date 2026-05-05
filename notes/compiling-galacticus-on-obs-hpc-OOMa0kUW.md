# Compiling Galacticus on OBS HPC

###### status: `reference` · last reviewed: TBD

###### tags: `build` `computing` `OBS HPC`

"OBS HPC" is a compute cluster at Carnegie. It has all of the tools and libraries needed to compile and run Galacticus pre-installed and loadable via the `module` command, so building your own copy of Galacticus is generally straightforward.

Some basic information on OBS HPC:
* Login node: `obshpc.carnegiescience.edu` (use your usual Carnegie credentials)
* [Documentation](https://carnegiescience.atlassian.net/wiki/spaces/HPC)

(These notes are always a work in progress - if something doesn't work, ask in the [`#dmtheory-help`](https://carnegiescience.slack.com/archives/C065D2V8G3A) Slack channel or, if you figure out a solution, update the notes.)

## Build environment

### Loading the `galacticus` module

Before attempting to build Galacticus you should run the command:
```
module load galacticus
```
This will load the required compilers and libraries and set your environment variable appropriately to allow you to build Galacticus.

If you use Galacticus extensively I'd suggest placing this command into your `.bashrc` file so that the module is loaded automatically whenever you log in.

### Note for older versions

If you are building a version of Galacticus prior to revision [a6a5c8c](https://github.com/galacticusorg/galacticus/commit/a6a5c8c3a3e96a1a9b9e49e75278790df784f07c) (released on 12/01/2024), you must use the older HDF5 library (v.1.8.20) you should instead do:
```
module load galacticus_hdf5v1.8.20
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

Galacticus generates a bunch of files at run-time which get stored in `$GALACTICUS_DATA_PATH/dynamic`. Since these can become quite large I suggest moving the `dynamic` directory to a data disk and creating a link to it. For example:

```
cd $GALACTICUS_DATA_PATH
mv dynamic /carnegie/nobackup/users/$USER/
ln -sf /carnegie/nobackup/users/$USER/dynamic
```

### Using shared static datasets

Since the `static` folder in the `datasets` repo is the same for everyone, you can opt to make use of a shared `static` datasets folder. (The only reason you would want to *not* do this is if you're making changes to the `static` datasets.)

This can be set up as follows:
```
export GALACTICUS_DATA_PATH=/carnegie/nobackup/users/$USER/Galacticus/datasets
mkdir -p ${GALACTICUS_DATA_PATH}
cd ${GALACTICUS_DATA_PATH}
mkdir static
ln -sf /carnegie/nobackup/appdata/galacticus/datasets/static static
```

The copy of the `datasets` repo at `/carnegie/nobackup/appdata/galacticus/datasets` is automatically updated every night.

## Building Galacticus

You should now be able to build Galacticus. It's recommended to build on a compute node if possible (as you can then use more CPUs and memory so it will go faster). To do this, first get a compute node using:
```
srun --exclusive --mem=0 --pty bash -i
```
This will allocate a node to you and log you in to a terminal on that node. Then you can compile:
```
cd $GALACTICUS_EXEC_PATH
make -j24 Galacticus.exe
```
(Once the build is finished you can leave the compute node using `exit`.)

If no compute nodes are available right away, you can compile on the login node, but use fewer build jobs (otherwise your build will likely be killed automatically):
```
cd $GALACTICUS_EXEC_PATH
make -j4 Galacticus.exe
```

The build takes quite a while (~30 minutes). If it succeeds you'll have a `Galacticus.exe` executable file. It's useful to run a very quick test to make sure it's all working:

```
./Galacticus.exe parameters/quickTest.xml
```

### Using the shared partition

OBS HPC now has a "shared" partition. This is a single node which allows multiple jobs to run simultaneously. This can be useful if, for example, you just want to compile Galacticus but the default queue is very full and you would have to wait hours or days to get a compute node.

To get an interactive job on the shared partition use:
```
srun --cpus-per-task=24 --mem=8G -p shared --pty bash -i
```
This will get you up to 24 CPUs and 8GB of memory. Note that 8GB of memory is the maximum allowed on the shared partition. Also note that `srun` defaults to requesting *1GB per CPU* - so if you don't specify the memory in the `srun` command it may fail if you ask for more than 8 CPUs. 

Once you have this interactive job on the shared node you can compile as normal. Due to the 8GB memory limit sometimes the build will fail - if you use multiple jobs to build (the `-j` option to `make`) then the total memory usage can exceed 8GB. Therefore, you may want to try:
```
make -j24 -k Galacticus.exe
```
which will build with 24 jobs and keep going (`-k`) even if some fail due to excess memory usage. If the build fails due to a job being killed for excess memory usage, just run the same command again - eventually it should succeed! Alternatively, I've found that using just two jobs:
```
make -j2 Galacticus.exe
```
works without any problems.

You can find more details about the shared partition [here](https://carnegiescience.atlassian.net/wiki/spaces/HPC/pages/1107820551/Using+Shared+CPUs+Oversubscribe).

## Building the library and Python module

Building the Galacticus library and Python module (so you can use Galacticus in a Jupyter notebook for example) can be done using:
```
make -j2 GALACTICUS_BUILD_OPTION=lib libgalacticus.so
```
See [here](https://github.com/galacticusorg/galacticus/wiki/Python-interface-%28experimental%29) for more details.

## Group storage

We have shared storage space at `/carnegie/nobackup/groups/dmtheory/` - used to store shared datasets (e.g. merger trees). If you need access, ask in the [`#dmtheory-help`](https://carnegiescience.slack.com/archives/C065D2V8G3A) Slack channel.

## See also

- [Submitting Jobs on OBS HPC](submitting-jobs-on-obs-hpc-aCJxUqdn.md)
- [Compiling Galacticus on Caltech HPC](compiling-galacticus-on-caltech-hpc-jol6HnNq.md)
- [Compiling Galacticus on NERSC](compiling-galacticus-on-nersc-KMvLs5JT.md)
