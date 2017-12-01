#!/usr/bin/bash
#SBATCH --ntasks 2 --nodes 1 
module load IQ-TREE
iqtree-omp -s VMS1.aa.trim -nt 2

