#This codes produces the Beer graph for the spectroscopy lab


import numpy as np
import matplotlib.pyplot as plt

# Concentration of Ca2+ (ppm)
concentration = np.array([2.00, 4.00, 6.00, 8.03, 9.98, 15.15])

# Absorbance values
absorbance = np.array([0.064, 0.117, 0.177, 0.240, 0.302, 0.440])

# Unknown sample absorbance
unknown_absorbance = 0.125

# Energy of photon (J)
photon_energy = 4.72e-19

# Linear regression
slope, intercept = np.polyfit(concentration, absorbance, 1)

# Predicted absorbance
predicted_absorbance = slope * concentration + intercept

# Calculate R-squared
ss_res = np.sum((absorbance - predicted_absorbance)**2)
ss_tot = np.sum((absorbance - np.mean(absorbance))**2)
r_squared = 1 - ss_res / ss_tot

# Calculate unknown concentration
unknown_concentration = (
    unknown_absorbance - intercept
) / slope

# Generate regression line
concentration_line = np.linspace(0, 16, 200)
absorbance_line = slope * concentration_line + intercept

# Create graph
fig, ax = plt.subplots(figsize=(11, 7))

# Experimental data
ax.scatter(
    concentration,
    absorbance,
    color="blue",
    s=80,
    label="Calibration Standards",
    zorder=3
)

# Linear regression line
ax.plot(
    concentration_line,
    absorbance_line,
    color="red",
    linewidth=2,
    label="Linear Regression"
)

# Unknown sample
ax.scatter(
    unknown_concentration,
    unknown_absorbance,
    color="green",
    marker="*",
    s=220,
    label=f"Unknown = {unknown_concentration:.2f} ppm",
    zorder=4
)

# Regression equation using concentration and absorbance
equation = (
    f"Absorbance = {slope:.6f}(Concentration) "
    f"+ {intercept:.6f}\n"
    f"R² = {r_squared:.5f}"
)

# Display equation
ax.text(
    0.05, 0.95,
    equation,
    transform=ax.transAxes,
    fontsize=12,
    verticalalignment="top",
    bbox=dict(facecolor="white", edgecolor="gray")
)

# Display photon energy
ax.text(
    0.05, 0.80,
    r"Photon Energy = $4.72 \times 10^{-19}$ J",
    transform=ax.transAxes,
    fontsize=12,
    bbox=dict(facecolor="lightyellow", edgecolor="orange")
)

# Title and axis labels
ax.set_title(
    "Absorbance vs. Concentration of Ca²⁺",
    fontsize=16,
    fontweight="bold"
)

ax.set_xlabel("Concentration of Ca²⁺ (ppm)", fontsize=13)
ax.set_ylabel("Absorbance", fontsize=13)

# Axis limits
ax.set_xlim(0, 16)
ax.set_ylim(0, 0.50)

# Grid and legend
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(loc="lower right")

plt.tight_layout()

# Save graph
plt.savefig("Ca2_Calibration_Graph.png", dpi=300)
plt.savefig("Ca2_Calibration_Graph.pdf")

# Display graph
plt.show()

# Print results
print("CALCIUM CALIBRATION RESULTS")
print("---------------------------")
print(
    f"Absorbance = {slope:.6f}(Concentration) "
    f"+ {intercept:.6f}"
)
print(f"R² = {r_squared:.5f}")
print(f"Unknown concentration = {unknown_concentration:.2f} ppm")
print(f"Photon energy = {photon_energy:.2e} J")
