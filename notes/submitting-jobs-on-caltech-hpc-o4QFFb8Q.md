# Submitting Jobs on Caltech HPC

###### status: `reference` · last reviewed: TBD

###### tags: `computing` `Caltech HPC`

The Caltech HPC compute clusters uses the [SLURM](https://en.wikipedia.org/wiki/Slurm_Workload_Manager) queue scheduler to manage jobs.

## `Caltech HPC` Configuration

Full information can be found [here](https://www.hpc.caltech.edu/documentation).

`Caltech HPC` consists of multiple login nodes (where you start when you `ssh` to `Caltech HPC`) and a large number of compute nodes. You should avoid running substantial calculations (i.e. anything that uses more than ~1 minute of CPU time, or uses multiple cores) on the login node. The compute nodes are intended for serious computation.

Compute nodes are heterogeneous - they have different numbers of cores and memory as described [here](https://www.hpc.caltech.edu/resources).

### Storage

Your home directory, `/home/$USER`, has a quota of 50GB. As such, it's recommended that you use your home space for source files and other valuable data. 

Additionally, there is group space available at `/resnick/groups/carnegie_poc/${USER}`. 

There is also scratch space at `/resnick/scratch`. It is recommended that you create a directory named with your user name on the scratch disk:
```
mkdir -p /resnick/scratch/$USER
```
and store temporary data there. Note that files untouched for 14 days are automatically removed from `/resnick/scratch` - more information can be found [here](https://www.hpc.caltech.edu/documentation/storage).

## Submitting a Job

To submit a job to `Caltech HPC` you should create a "submit script", which is simply a `bash` script with some header information to specify what resources you require. An example is as follows:
```
#!/bin/bash
#SBATCH --time=1:00:00   # walltime
#SBATCH --ntasks=1   # number of tasks (i.e. number of Galacticus.exe that will run)
#SBATCH --cpus-per-task=16 # number of CPUs to assign to each task
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=2G   # memory per CPU core
#SBATCH -J "myJobName"   # job name
#SBATCH --mail-user=abenson@carnegiescience.edu   # email address
#SBATCH --error=myLogFile.log # Send output to a log file
#SBATCH --output=myLogFile.log

# Notify at the beginning, end of job and on failure.
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL

# Change directory to the location from which this job was submitted
cd $SLURM_SUBMIT_DIR
# Disable core-dumps (not useful unless you know what you're doing with them)
ulimit -c 0
export GFORTRAN_ERROR_DUMPCORE=NO
# Ensure there are no CPU time limits imposed.
ulimit -t unlimited
# Tell OpenMP to use all available CPUs on this node.
export OMP_NUM_THREADS=16
# Run Galacticus.
./Galacticus.exe myJobParameters.xml
```

The most important header lines are:
```
#SBATCH --ntasks=16   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
```
which specifies what resources we want for this job. In this case we request 1 compute node, and 16 tasks (cores) on it.

If you have `Galacticus` compiled for MPI parallelism you can run it across multiple nodes. An example, using 4 nodes, would look like this:
```
#!/bin/bash
#SBATCH --time=1:00:00   # walltime
#SBATCH --ntasks=64   # number of tasks (i.e. number of Galacticus.exe that will run)
#SBATCH --cpus-per-task=1 # number of CPUs to assign to each task
#SBATCH --nodes=4   # number of nodes
#SBATCH --mem-per-cpu=2G   # memory per CPU core
#SBATCH -J "myJobName"   # job name
#SBATCH --mail-user=abenson@carnegiescience.edu   # email address

# Notify at the beginning, end of job and on failure.
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL

# Change directory to the location from which this job was submitted
cd $SLURM_SUBMIT_DIR
# Disable core-dumps (not useful unless you know what you're doing with them)
ulimit -c 0
export GFORTRAN_ERROR_DUMPCORE=NO
# Ensure there are no CPU time limits imposed.
ulimit -t unlimited
# Tell OpenMP to use all available CPUs on this node.
export OMP_NUM_THREADS=1
# Run Galacticus.
mpirun --n 64 --bind-to none --map-by node --mca pml ob1 --mca btl ^openib ./Galacticus.exe myJobParameters.xml
```
where we switch off OpenMP parallelism by setting `OMP_NUM_THREADS=1` and launch 64 MPI processes.

To submit your job to `Caltech HPC` use:
```
$ sbatch mySubmitScript.sh
```

This will place the job into the queue, and it will automatically start running as soon as resources are available.

You can monitor the status of jobs using:
```
squeue -u $USER
```
which produces output like:
```
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON) 
          19782601       any    myJob  abenson  R 2-00:00:11      1 hpc-80-33 
      
```
This shows your job number and name, the time it has been running for, and its state (the `ST` column). States are:
* `COMPLETED` - `CD`: The job has completed successfully.
* `COMPLETING` - `CG`: The job is finishing but some processes are still active.
* `FAILED` - `F`: The job terminated with a non-zero exit code and failed to execute.
* `PENDING` - `PD`: The job is waiting for resource allocation. It will eventually run.
* `PREEMPTED` - `PR`: The job was terminated because of preemption by another job.
* `RUNNING` - `R`: The job currently is allocated to a node and is running.
* `SUSPENDED` - `S`: A running job has been stopped with its cores released to other jobs.
* `STOPPED` - `ST`: A running job has been stopped with its cores retained.

### Note for very large numbers of MPI processes

If you run very large numbers of MPI processes (256 or more seems to be the trigger point) you may get errors of the form:
```
ORTE has lost communication with a remote daemon.
```

If this happens, try adding:
```
--mca routed binomial
```
to the `mpirun` command.

### Interactive Sessions

You can request an interactive session on a compute node (i.e. pull up a command line interface on a compute node so that you can work on there directly) using:
```
srun --pty -n 1 --wait=0 --time=1:00:00 /bin/bash
```
This requests a single task (core), will log you in to a node and move to the same directory as you were in on the login node.

When you're finished, just `exit` and you'll be back on the login node (and your interactive session job will terminate).

### Tasks, Nodes, CPUs

In the above, we have the following `SBATCH` commands which control how resources are allocated to your job:
* `--nodes`
* `--ntasks`
* `--cpus-per-task`

How you use these will depend on whether you're running Galacticus using OpenMP parallelism (the default), MPI parallelism (which you activate by compiling with the `GALACTICUS_BUILD_OPTION=MPI` option), or a hybrid of both.

### OpenMP parallelism

OpenMP parallelism doesn't allow you run run over multiple nodes, so we will always set `--nodes=1` in this case. Furthermore, OpenMP paralleism only ever runs a single copy of `Galacticus.exe`, so we always set `--ntasks=1`.

OpenMP parallelism _does_ allow that single `Galacticus.exe` to use multiple CPUs. So, set `--cpus-per-task=N` where `N` is whatever number of CPUs you want Galacticus to use - and include a corresponding:
```
export OMP_NUM_THREADS=N
```
in your submit script so that Galacticus knows how many CPUs it has available to it.

### MPI parallelism

MPI parallelism allows Galacticus to run across multiple nodes. There will be multiple `Galacticus.exe` processes running in this case. Suppose we want to run Galacticus using 4 nodes, and to make use of 16 CPUs on each node (for a total of 64 CPUs). We would set the options:
```
--nodes=4
--ntasks=64
--cpus-per-task=1
```
where we've selected 4 nodes, 64 tasks (i.e. 64 copies of `Galacticus.exe` running in total - these will be distributed over the 4 nodes), and assigned a single CPU to each `Galacticus.exe`. Then also include:
```
export OMP_NUM_THREADS=1
```
in your submit script (this limits OpenMP parallelism to a single thread - i.e. no parallelism), and launch Galacticus using:
```
mpirun --n 64 --bind-to none --map-by node ./Galacticus.exe myJobParameters.xml
```
The `--map-by node` ensures that the 64 `Galacticus.exe` processes get distributed across our 4 nodes.

### Hybrid OpenMP/MPI parallelism

You can use MPI and OpenMP parallelism simultaneously. To do this, first decide how many nodes you want to use, call this `Nnode`. Then decide how many CPUs you want to use on each node, call this `Ncpu`. Next decide how many MPI processes you want to run _on each node_ - this must be an integer factor of `Ncpu` - call this `Nmpi`. Then, to use all available CPUs we need each `Galacticus.exe` to use `Nopenmp=Ncpu/Nmpi` CPUs. 

Having determined all of these, use the `SBATCH` options:
```
--nodes=Nnode
--ntasks=Nnode*Nmpi
--cpus-per-task=Nopenmp
```
and launch Galacticus using:
```
export OMP_NUM_THREADS=Nopenmp
mpirun --n Nnode*Nmpi --bind-to none --map-by node ./Galacticus.exe myJobParameters.xml
```
This is where the `--bind-to none` is important. Without it, MPI restricts all OpenMP parallel threads to run on the same CPU - which defeats the purpose of using OpenMP. With this option, OpenMP threads have access to all avalable CPUs.

## See also

- [Compiling Galacticus on Caltech HPC](https://hackmd.io/jol6HnNqT7KVaAMwzhXoHg)
- [Submitting Jobs on OBS HPC](https://hackmd.io/aCJxUqdnShSAjVcX_vUwpg)
