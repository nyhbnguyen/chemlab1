#This codes produces the Beer graph for the spectroscopy lab

import numpy as np
import matplotlib.pyplot as plt

# Experimental data
concentration = np.array([2.00, 4.00, 6.00, 8.03, 9.98, 15.15])
absorbance = np.array([0.064, 0.117, 0.177, 0.240, 0.302, 0.440])

# Unknown sample absorbance
unknown_absorbance = 0.125

# Linear regression
slope, intercept = np.polyfit(concentration, absorbance, 1)

# Predicted absorbance values
predicted = slope * concentration + intercept

# Calculate R-squared
ss_res = np.sum((absorbance - predicted)**2)
ss_tot = np.sum((absorbance - np.mean(absorbance))**2)
r_squared = 1 - (ss_res / ss_tot)

# Calculate unknown concentration
unknown_concentration = (unknown_absorbance - intercept) / slope

# Create regression line
x_line = np.linspace(0, 16, 200)
y_line = slope * x_line + intercept

# Plot
plt.figure(figsize=(9, 6))

# Experimental data points
plt.scatter(
    concentration, absorbance,
    color="blue", s=70,
    label="Calibration standards",
    zorder=3
)

# Linear regression line
plt.plot(
    x_line, y_line,
    color="red", linewidth=2,
    label="Linear regression"
)

# Unknown sample
plt.scatter(
    unknown_concentration, unknown_absorbance,
    color="green", marker="*", s=180,
    label=f"Unknown = {unknown_concentration:.2f} ppm",
    zorder=4
)

# Equation and R-squared
equation = (
    f"y = {slope:.6f}x + {intercept:.6f}\n"
    f"R² = {r_squared:.5f}"
)

plt.text(
    0.05, 0.95, equation,
    transform=plt.gca().transAxes,
    fontsize=12,
    verticalalignment="top",
    bbox=dict(facecolor="white", edgecolor="gray", alpha=0.9)
)

# Graph formatting
plt.title("Absorbance vs. Concentration of Ca²⁺", fontsize=15)
plt.xlabel("Concentration (ppm)", fontsize=12)
plt.ylabel("Absorbance", fontsize=12)

plt.xlim(0, 16)
plt.ylim(0, 0.50)

plt.grid(True, linestyle="--", alpha=0.4)
plt.legend(loc="lower right")
plt.tight_layout()

# Save graph
plt.savefig("Ca2_calibration_curve.png", dpi=300, bbox_inches="tight")
plt.savefig("Ca2_calibration_curve.pdf", bbox_inches="tight")

plt.show()

# Print results
print(f"Slope: {slope:.6f}")
print(f"Intercept: {intercept:.6f}")
print(f"R-squared: {r_squared:.5f}")
print(f"Unknown concentration: {unknown_concentration:.2f} ppm")
