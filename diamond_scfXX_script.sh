!/bin/bash -l
#SBATCH --job-name=Diamond_scfXX_relax !XX to range for quantaties of: 40, 60, 80, 100
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
mpirun -n 16 pw.x -in diamond_scfXX.relax.in > diamond_scfXX.relax.out 2>&1
