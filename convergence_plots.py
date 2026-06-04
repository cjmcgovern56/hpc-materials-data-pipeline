import matplotlib.pyplot as plt

# =========================================================================
# 1. CUTOFF ENERGY CONVERGENCE DATA & PLOT
# =========================================================================

# 3C-SiC Cutoff Test Energies (Ry)
SiC_scf40_tot_energy = -20.49662266
SiC_scf60_tot_energy = -20.53589690
SiC_scf80_tot_energy = -20.53920340
SiC_scf100_tot_energy = -20.53927599

# Diamond Cutoff Test Energies (Ry)
Diamond_scf40_tot_energy = -23.99419620
Diamond_scf60_tot_energy = -24.06810094
Diamond_scf80_tot_energy = -24.07502233
Diamond_scf100_tot_energy = -24.07513963

# Compile into plotting lists
cutoffs = [40, 60, 80, 100]
SiC_energies = [SiC_scf40_tot_energy, SiC_scf60_tot_energy, SiC_scf80_tot_energy, SiC_scf100_tot_energy]
Diamond_energies = [Diamond_scf40_tot_energy, Diamond_scf60_tot_energy, Diamond_scf80_tot_energy, Diamond_scf100_tot_energy]

# Generate Cutoff Plot
fig, ax1 = plt.subplots(figsize=(8, 5))
ax1.set_xlabel('Kinetic Energy Cutoff (Ry)', fontsize=12)
ax1.set_ylabel('3C-SiC Total Energy (Ry)', color='blue', fontsize=12)
ax1.plot(cutoffs, SiC_energies, marker='o', color='blue', label='3C-SiC', linewidth=2)
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Diamond Total Energy (Ry)', color='red', fontsize=12)
ax2.plot(cutoffs, Diamond_energies, marker='s', color='red', label='Diamond', linewidth=2)
ax2.tick_params(axis='y', labelcolor='red')

plt.title('Kinetic Energy Cutoff Convergence Comparison', fontsize=14)
ax1.grid(True, linestyle='--', alpha=0.6)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='center right')

plt.tight_layout()
plt.savefig('03_structures/cutoff_convergence.png', dpi=300)
plt.close()


# =========================================================================
# 2. K-POINT GRID CONVERGENCE DATA & PLOT
# =========================================================================

# 3C-SiC K-Point Test Energies (Ry)
SiC_kpoint_4x_tot_energy = -20.53073473
SiC_kpoint_6x_tot_energy = -20.53920340
SiC_kpoint_8x_tot_energy = -20.53990504

# Diamond K-Point Test Energies (Ry)
Diamond_kpoint_4x_tot_energy = -24.06601902
Diamond_kpoint_6x_tot_energy = -24.07502233
Diamond_kpoint_8x_tot_energy = -24.07564255

# Compile into plotting lists
k_grids = [4, 6, 8]
sic_k_energies = [SiC_kpoint_4x_tot_energy, SiC_kpoint_6x_tot_energy, SiC_kpoint_8x_tot_energy]
diamond_k_energies = [Diamond_kpoint_4x_tot_energy, Diamond_kpoint_6x_tot_energy, Diamond_kpoint_8x_tot_energy]

# Generate K-Point Plot
fig, ax1 = plt.subplots(figsize=(8, 5))
ax1.set_xlabel('K-Point Grid Density (N x N x N)', fontsize=12)
ax1.set_ylabel('3C-SiC Total Energy (Ry)', color='blue', fontsize=12)
ax1.plot(k_grids, sic_k_energies, marker='o', color='blue', label='3C-SiC', linewidth=2)
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Diamond Total Energy (Ry)', color='red', fontsize=12)
ax2.plot(k_grids, diamond_k_energies, marker='s', color='red', label='Diamond', linewidth=2)
ax2.tick_params(axis='y', labelcolor='red')

plt.title('K-Point Grid Convergence Comparison', fontsize=14)
ax1.set_xticks(k_grids)
ax1.grid(True, linestyle='--', alpha=0.6)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='center right')

plt.tight_layout()
plt.savefig('03_structures/kpoint_convergence.png', dpi=300)
plt.close()

print("Convergence plots successfully generated using named parameters and saved to '03_structures/'.")
