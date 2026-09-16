# This code produces the bar graph for the measurement lab
# This code produces bar graph for the measurement obtained with graduate cylinder
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Experimental data
# -----------------------------
measurements = np.arange(1, 6)

volume_ml = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
mass_g = np.array([9.89, 20.1, 30.2, 40.2, 50.0])

# -----------------------------
# Calculate density
# Density = mass / volume
# -----------------------------
density_g_ml = mass_g / volume_ml

# Calculate average density
average_density = np.mean(density_g_ml)

# Calculate sample standard deviation
standard_deviation = np.std(density_g_ml, ddof=1)

# True density of water at 22.0 °C
true_density = 0.99777  # g/mL

# -----------------------------
# Create bar graph
# -----------------------------
plt.figure(figsize=(10, 6))

plt.bar(
    measurements,
    density_g_ml,
    yerr=np.full(len(density_g_ml), standard_deviation),
    capsize=5,
    edgecolor="black",
    label="Measured density"
)

# Average density line
plt.axhline(
    average_density,
    linestyle="--",
    linewidth=2,
    label=f"Average density = {average_density:.4f} g/mL"
)

# True density line
plt.axhline(
    true_density,
    linestyle=":",
    linewidth=2,
    label=f"True density at 22.0 °C = {true_density:.5f} g/mL"
)

# -----------------------------
# Add density values above bars
# -----------------------------
for x, y in zip(measurements, density_g_ml):
    plt.text(
        x,
        y + 0.001,
        f"{y:.4f}",
        ha="center",
        va="bottom"
    )

# -----------------------------
# Graph formatting
# -----------------------------
plt.title(
    "Density of Water at 22.0 °C Measured with a Graduated Cylinder"
)

plt.xlabel("Measurement")
plt.ylabel("Density (g/mL)")

plt.xticks(measurements)

# Zoom the y-axis so the differences are easier to see
plt.ylim(0.97, 1.03)

plt.grid(axis="y", alpha=0.25)

plt.legend()

plt.tight_layout()

# Display graph
plt.show()

# -----------------------------
# Print results in PyCharm
# -----------------------------
print("Density for each measurement:")

for i, density in zip(measurements, density_g_ml):
    print(f"Measurement {i}: {density:.4f} g/mL")

print(f"\nAverage density: {average_density:.4f} g/mL")
print(f"Standard deviation: {standard_deviation:.4f} g/mL")
print(f"True density at 22.0 °C: {true_density:.5f} g/mL")

# This code produces bar graph for the measurement obtained with volumetric pipette
import numpy as np
import matplotlib.pyplot as plt

# Experimental data
measurements = np.arange(1, 6)
volume_ml = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
mass_g = np.array([9.93, 19.9, 29.8, 39.8, 49.7])

# Calculate density for each measurement
# Density = mass / volume
density_g_ml = mass_g / volume_ml

# Calculate average density
average_density = np.mean(density_g_ml)

# Calculate sample standard deviation
standard_deviation = np.std(density_g_ml, ddof=1)

# True density of water at 20.0 °C
true_density = 0.9982  # g/mL

# Create bar graph
fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(
    measurements,
    density_g_ml,
    yerr=np.full(len(density_g_ml), standard_deviation),
    capsize=5,
    edgecolor="black",
    label="Measured density"
)

# Average density line
ax.axhline(
    average_density,
    linestyle="--",
    linewidth=2,
    label=f"Average density = {average_density:.4f} g/mL"
)

# True density line
ax.axhline(
    true_density,
    linestyle=":",
    linewidth=2,
    label=f"True density at 20.0 °C = {true_density:.4f} g/mL"
)

# Add density values above each bar
for x, y in zip(measurements, density_g_ml):
    ax.text(
        x,
        y + 0.0008,
        f"{y:.4f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

# Labels and title
ax.set_title(
    "Density of Water at 20.0 °C Measured with a Volumetric Pipette"
)
ax.set_xlabel("Measurement")
ax.set_ylabel("Density (g/mL)")

ax.set_xticks(measurements)

# Adjust y-axis to make differences visible
ax.set_ylim(0.985, 1.005)

ax.grid(axis="y", alpha=0.25)
ax.legend()

plt.tight_layout()
plt.show()

# Print results
print("Density for each measurement:")

for i, density in zip(measurements, density_g_ml):
    print(f"Measurement {i}: {density:.4f} g/mL")

print(f"\nAverage density: {average_density:.4f} g/mL")
print(f"Sample standard deviation: {standard_deviation:.4f} g/mL")
print(f"True density at 20.0 °C: {true_density:.4f} g/mL")

#This code produce the bar graph of the mesaurement for the density of penny
import numpy as np
import matplotlib.pyplot as plt

# Experimental data
measurements = np.arange(1, 5)
volume_cm3 = np.array([0.25, 0.25, 0.25, 0.25])
mass_g = np.array([2.5, 2.5, 2.5, 2.5])

# Calculate density
# Density = mass / volume
density_g_cm3 = mass_g / volume_cm3

# Calculate average density
average_density = np.mean(density_g_cm3)

# Calculate sample standard deviation
standard_deviation = np.std(density_g_cm3, ddof=1)

# True density of a post-1982 U.S. penny
true_density = 7.18  # g/cm^3

# Create bar graph
fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(
    measurements,
    density_g_cm3,
    yerr=np.full(len(density_g_cm3), standard_deviation),
    capsize=5,
    edgecolor="black",
    label="Measured density"
)

# Average density line
ax.axhline(
    average_density,
    linestyle="--",
    linewidth=2,
    label=f"Average density = {average_density:.2f} g/cm³"
)

# True density line
ax.axhline(
    true_density,
    linestyle=":",
    linewidth=2,
    label=f"True density = {true_density:.2f} g/cm³"
)

# Add density values above bars
for x, y in zip(measurements, density_g_cm3):
    ax.text(
        x,
        y + 0.08,
        f"{y:.2f}",
        ha="center",
        va="bottom",
        fontsize=10
    )

# Labels and title
ax.set_title("Density of Penny")
ax.set_xlabel("Measurement")
ax.set_ylabel("Density (g/cm³)")
ax.set_xticks(measurements)

# Set y-axis limits
ax.set_ylim(6.0, 10.8)

ax.grid(axis="y", alpha=0.25)
ax.legend()

plt.tight_layout()
plt.show()

# Print results
print("Density for each measurement:")

for i, density in zip(measurements, density_g_cm3):
    print(f"Measurement {i}: {density:.2f} g/cm³")

print(f"\nAverage density: {average_density:.2f} g/cm³")
print(f"Standard deviation: {standard_deviation:.3f} g/cm³")
print(f"True density: {true_density:.2f} g/cm³")