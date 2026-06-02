!/bin/bash -l
#SBATCH --job-name=diamond_relax
#SBATCH --partition=ckpt
#SBATCH --account=stf-ckpt
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --time=01:00:00     
#SBATCH --mem=20G      
#SBATCH --export=all

module load chem/qe/6.8

# Clean up any old living files before starting
rm -rf diamond.save

# Run with explicit input flag and error redirection
mpirun -n 16 pw.x -in diamond.relax.in > diamond.relax.out 2>&1
