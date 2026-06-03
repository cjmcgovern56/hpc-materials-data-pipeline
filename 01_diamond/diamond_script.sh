#!/bin/bash -l
  
#SBATCH --job-name=Diamond_relax

#SBATCH --partition=ckpt
#SBATCH --account=stf-ckpt

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4


#SBATCH --time=01:00:00

#SBATCH --export=all

module load chem/qe/6.8

mpirun -n 4 pw.x < ./diamond_vc-relax.in > ./diamond_vs-relax.out

