#!/usr/bin/bash
#SBATCH --ntasks 4 --nodes 1
module load RAxML
raxmlHPC-PTHREADS-SSE3 -m PROTGAMMAAUTO -T 4 -s VMS1.aa.trim -n VMS1_Run1 -p 123 -x 123 -f a -N autoMRE
