#This codes produces the Beer graph for the spectroscopy lab

import numpy as np
import matplotlib.pyplot as plt

# Calcium concentration (ppm)
concentration = np.array([2.00, 4.00, 6.00, 8.03, 9.98, 15.15])

# Absorbance measurements
absorbance = np.array([0.064, 0.117, 0.177, 0.240, 0.302, 0.440])

# Unknown sample
unknown_absorbance = 0.125

# Photon energy (J)
photon_energy = 4.72e-19

# Linear regression
slope, intercept = np.polyfit(concentration, absorbance, 1)

# Calculate R-squared
predicted = slope * concentration + intercept
ss_res = np.sum((absorbance - predicted)**2)
ss_tot = np.sum((absorbance - np.mean(absorbance))**2)
r_squared = 1 - ss_res / ss_tot

# Calculate unknown concentration
unknown_concentration = (unknown_absorbance - intercept) / slope

# Generate regression line
x_line = np.linspace(0, 16, 200)
y_line = slope * x_line + intercept

# Create graph
fig, ax = plt.subplots(figsize=(10, 7))

# Experimental data points
ax.scatter(
    concentration, absorbance,
    color="blue",
    s=80,
    label="Calibration standards",
    zorder=3
)

# Linear regression
ax.plot(
    x_line, y_line,
    color="red",
    linewidth=2,
    label="Linear regression"
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

# Equation and R-squared
equation_text = (
    f"y = {slope:.6f}x + {intercept:.6f}\n"
    f"R² = {r_squared:.5f}"
)

ax.text(
    0.05, 0.95,
    equation_text,
    transform=ax.transAxes,
    fontsize=12,
    verticalalignment="top",
    bbox=dict(facecolor="white", edgecolor="gray")
)

# Photon energy annotation
ax.text(
    0.05, 0.78,
    r"Photon Energy = $4.72 \times 10^{-19}$ J",
    transform=ax.transAxes,
    fontsize=12,
    fontweight="bold",
    bbox=dict(facecolor="lightyellow", edgecolor="orange")
)

# Graph title and axes
ax.set_title(
    "Absorbance vs. Concentration of Ca²⁺",
    fontsize=16,
    fontweight="bold"
)

ax.set_xlabel("Concentration (ppm)", fontsize=13)
ax.set_ylabel("Absorbance", fontsize=13)

# Axis limits
ax.set_xlim(0, 16)
ax.set_ylim(0, 0.50)

# Grid and legend
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(loc="lower right", fontsize=10)

plt.tight_layout()

# Save graph
plt.savefig(
    "Ca2_Absorbance_Calibration.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    "Ca2_Absorbance_Calibration.pdf",
    bbox_inches="tight"
)

# Display graph
plt.show()

# Print calculations
print("CALCIUM CALIBRATION RESULTS")
print("---------------------------")
print(f"Slope: {slope:.6f}")
print(f"Intercept: {intercept:.6f}")
print(f"R-squared: {r_squared:.5f}")
print(f"Unknown absorbance: {unknown_absorbance:.3f}")
print(f"Unknown concentration: {unknown_concentration:.2f} ppm")
print(f"Photon energy: {photon_energy:.2e} J")
