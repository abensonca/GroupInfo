# Submitting Jobs on NERSC

###### status: `reference` · last reviewed: 2026-05-05

###### tags: `computing` `NERSC`

The Perlmutter compute cluster at NERSC uses the [SLURM](https://en.wikipedia.org/wiki/Slurm_Workload_Manager) queue scheduler to manage jobs.

## `NERSC` Configuration

The Perlmutter login node is at `perlmutter.nersc.gov` - connect with your NERSC credentials and an MFA token.

Full documentation lives at [https://docs.nersc.gov/](https://docs.nersc.gov/), with [Perlmutter-specific information here](https://docs.nersc.gov/systems/perlmutter/) and a [running jobs overview here](https://docs.nersc.gov/jobs/).

Jobs at NERSC are charged against a project allocation. Our group's allocation is `m4943`, which you must specify in every submission via `#SBATCH -A m4943` (or `--account=m4943`). Perlmutter has both CPU and GPU compute nodes, so you also need to specify the architecture using `#SBATCH -C cpu` (or `-C gpu`).

The defaults below (CPUs per node, queue names, etc.) may change - verify against [NERSC's current documentation](https://docs.nersc.gov/jobs/) before relying on them.

### Storage

* `/global/homes/<initial>/<user>` (`$HOME`) - your home directory; small quota, recommended for source code and configuration files.
* `/pscratch/sd/<initial>/<user>` (`$SCRATCH`) - large per-user scratch space. Files unaccessed for an extended period are purged - see the [NERSC file-system documentation](https://docs.nersc.gov/filesystems/).
* `/global/cfs/cdirs/m4943/` - Community File System project space for our allocation. Use this for shared inputs, datasets, and long-lived outputs.

## Submitting a Job

To submit a job on Perlmutter you should create a "submit script", which is simply a `bash` script with some header information to specify what resources you require. An example is as follows:
```
#!/bin/bash
#SBATCH --time=1:00:00       # walltime
#SBATCH -A m4943             # project allocation
#SBATCH -C cpu               # Perlmutter CPU node
#SBATCH -q regular           # QoS / queue
#SBATCH --ntasks=1           # number of tasks (i.e. number of Galacticus.exe that will run)
#SBATCH --cpus-per-task=128  # number of CPUs to assign to each task
#SBATCH --nodes=1            # number of nodes
#SBATCH -J "myJobName"       # job name
#SBATCH --mail-user=you@example.com   # email address
#SBATCH --error=myLogFile.log
#SBATCH --output=myLogFile.log

# Notify at the beginning, end of job and on failure.
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL

# Set up the Galacticus build environment - see "Compiling Galacticus on NERSC".
# (e.g. source a script that exports PATH, LD_LIBRARY_PATH, GALACTICUS_FCFLAGS, etc.)

# Change directory to the location from which this job was submitted
cd $SLURM_SUBMIT_DIR
# Disable core-dumps (not useful unless you know what you're doing with them)
ulimit -c 0
export GFORTRAN_ERROR_DUMPCORE=NO
# Ensure there are no CPU time limits imposed.
ulimit -t unlimited
# Tell OpenMP to use all available CPUs on this node.
export OMP_NUM_THREADS=128
# Run Galacticus.
./Galacticus.exe myJobParameters.xml
```

The most important header lines are:
```
#SBATCH -A m4943
#SBATCH -C cpu
#SBATCH --ntasks=1
#SBATCH --nodes=1
```
which specify the allocation, the architecture, and that we want a single task on a single node.

If you have `Galacticus` compiled for MPI parallelism you can run it across multiple nodes. An example, using 4 nodes, would look like this:
```
#!/bin/bash
#SBATCH --time=1:00:00
#SBATCH -A m4943
#SBATCH -C cpu
#SBATCH -q regular
#SBATCH --ntasks=512   # number of MPI processes (4 nodes * 128 CPUs)
#SBATCH --cpus-per-task=1
#SBATCH --nodes=4
#SBATCH -J "myJobName"
#SBATCH --mail-user=you@example.com

#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL

cd $SLURM_SUBMIT_DIR
ulimit -c 0
export GFORTRAN_ERROR_DUMPCORE=NO
ulimit -t unlimited
export OMP_NUM_THREADS=1
srun -n 512 ./Galacticus.exe myJobParameters.xml
```
where we switch off OpenMP parallelism by setting `OMP_NUM_THREADS=1` and launch 512 MPI processes. Note that on Perlmutter the recommended way to launch MPI processes is `srun`, not `mpirun`.

To submit your job use:
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
             JOBID       PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
            1234567    regular_milan  myJob  abenson  R 0-00:10:11      1 nid001234
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

You can request an interactive session on a compute node using:
```
salloc -N 1 -C cpu -q interactive -A m4943 -t 1:00:00
```
This requests a single CPU node on the `interactive` QoS for one hour. When you're finished, just `exit`.

### Tasks, Nodes, CPUs

In the above, we have the following `SBATCH` commands which control how resources are allocated to your job:
* `--nodes`
* `--ntasks`
* `--cpus-per-task`

How you use these will depend on whether you're running Galacticus using OpenMP parallelism (the default), MPI parallelism (which you activate by compiling with the `GALACTICUS_BUILD_OPTION=MPI` option), or a hybrid of both.

### OpenMP parallelism

OpenMP parallelism doesn't allow you to run over multiple nodes, so we will always set `--nodes=1` in this case. Furthermore, OpenMP parallelism only ever runs a single copy of `Galacticus.exe`, so we always set `--ntasks=1`.

OpenMP parallelism _does_ allow that single `Galacticus.exe` to use multiple CPUs. So, set `--cpus-per-task=N` where `N` is whatever number of CPUs you want Galacticus to use - and include a corresponding:
```
export OMP_NUM_THREADS=N
```
in your submit script so that Galacticus knows how many CPUs it has available to it.

### MPI parallelism

MPI parallelism allows Galacticus to run across multiple nodes. There will be multiple `Galacticus.exe` processes running in this case. Suppose we want to run Galacticus using 4 nodes, and to make use of 128 CPUs on each node (for a total of 512 CPUs). We would set the options:
```
--nodes=4
--ntasks=512
--cpus-per-task=1
```
where we've selected 4 nodes, 512 tasks (i.e. 512 copies of `Galacticus.exe` running in total - these will be distributed over the 4 nodes), and assigned a single CPU to each `Galacticus.exe`. Then also include:
```
export OMP_NUM_THREADS=1
```
in your submit script (this limits OpenMP parallelism to a single thread - i.e. no parallelism), and launch Galacticus using:
```
srun -n 512 ./Galacticus.exe myJobParameters.xml
```

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
srun -n $((Nnode*Nmpi)) -c Nopenmp --cpu-bind=cores ./Galacticus.exe myJobParameters.xml
```
The `-c Nopenmp --cpu-bind=cores` options tell `srun` to allocate `Nopenmp` cores per task and pin threads sensibly across them, which lets the OpenMP threads in each `Galacticus.exe` actually use distinct CPUs.

## See also

- [Compiling Galacticus on NERSC](https://hackmd.io/_KMvLs5JTT6dTPA1VQDrrg)
- [Submitting Jobs on Caltech HPC](https://hackmd.io/o4QFFb8QTkCeet8muc6vsQ)
- [Submitting Jobs on OBS HPC](https://hackmd.io/aCJxUqdnShSAjVcX_vUwpg)
