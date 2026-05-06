# Submitting Jobs on OBS HPC

###### status: `reference` · last reviewed: 05/05.2026

###### tags: `computing` `OBS HPC`

The OBS HPC compute cluster uses the [SLURM](https://en.wikipedia.org/wiki/Slurm_Workload_Manager) queue scheduler to manage jobs.

## `OBS HPC` Configuration

The `OBS HPC` login node is at `obshpc.carnegiescience.edu` - you can connect with your usual Carnegie credentials.

Full documentation for the cluster lives [here](https://carnegiescience.atlassian.net/wiki/spaces/HPC).

### Other Carnegie HPC clusters

You can also access the equivalent clusters at our other divisions (just `ssh` to `eplhpc.carnegiescience.edu` or `bsehpc.carnegiescience.edu`). Your jobs will not have priority on these systems - so if someone else from those divisions submits a job, your job may get killed. But, it can be useful for running jobs that you can easily restart or resubmit if necessary.

### Storage

* `/home/$USER` - your home directory. Use it for source files and other valuable data; check your quota with `quota`.
* `/carnegie/nobackup/users/$USER` - per-user data space. Suitable for larger datasets and run-time outputs (note: not backed up).
* `/carnegie/nobackup/groups/dmtheory/` - shared group storage (e.g. for merger trees). Ask in the [`#dmtheory-help`](https://carnegiescience.slack.com/archives/C065D2V8G3A) Slack channel for access.


## Submitting a Job

To submit a job on `OBS HPC` you should create a "submit script", which is simply a `bash` script with some header information to specify what resources you require. An example is as follows:
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

# Load the Galacticus module
module load galacticus
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
mpirun --n 64 --bind-to none --map-by node ./Galacticus.exe myJobParameters.xml
```
where we switch off OpenMP parallelism by setting `OMP_NUM_THREADS=1` and launch 64 MPI processes.

To submit your job to `OBS HPC` use:
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
               859       obs    myJob  abenson  R 2-00:00:11      1 memex-2015-006
      
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

- [Compiling Galacticus on OBS HPC](compiling-galacticus-on-obs-hpc-OOMa0kUW.md)
- [Submitting Jobs on Caltech HPC](submitting-jobs-on-caltech-hpc-o4QFFb8Q.md)
