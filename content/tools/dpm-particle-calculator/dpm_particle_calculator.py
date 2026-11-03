"""DPM particle calculator.

Estimates particle and parcel counts for ANSYS Fluent Discrete Phase Model
(DPM) injections that use a Rosin-Rammler diameter distribution.

For each injection (one per particle density), the injected mass is split
across `n_diameters` discrete diameters spanning d_min to d_max (as Fluent
does), and converted to a number of real particles and of parcels.
"""

import math

import numpy as np

# ---------------------------------------------------------------------------
# Inputs
# ---------------------------------------------------------------------------

# injection time window in s
injection_start = 120
injection_end = 125

# injected mass flow rate in kg/s (per injection)
injection_mass_per_second = 0.0006

# particle diameters in m (1 um = 1e-6 m)
d_min = 1e-5
d_mean = 4e-5
d_max = 6e-5

# particle density in kg/m^3, one per injection
densities = {"particle_1": 1010, "particle_2": 1400, "particle_3": 1600}

# Rosin-Rammler spread parameter
spread = 3.5

# number of discrete diameters (Fluent "Number of Diameters")
n_diameters = 3

# number of real particles represented by each parcel
particles_per_parcel = 1000


# ---------------------------------------------------------------------------
# Calculation
# ---------------------------------------------------------------------------

def particle_mass(d, rho):
    """Mass of a spherical particle of diameter d and density rho."""
    return rho * math.pi / 6 * d**3


def rosin_rammler_fractions(d_min, d_mean, d_max, spread, n_diameters):
    """Discrete diameters and their mass fractions.

    The mass fraction of particles larger than d is
    Y_d = exp(-(d / d_mean) ** spread), truncated to [d_min, d_max].
    Each discrete diameter takes the mass fraction of the interval around it.
    """
    d_bins = np.linspace(d_min, d_max, n_diameters)
    d_edges = np.concatenate([[d_min], 0.5 * (d_bins[:-1] + d_bins[1:]), [d_max]])
    y_d = np.exp(-(d_edges / d_mean) ** spread)
    mass_frac = -np.diff(y_d)
    mass_frac /= mass_frac.sum()
    return d_bins, mass_frac


def main():
    injection_duration = injection_end - injection_start
    total_mass = injection_mass_per_second * injection_duration
    d_bins, mass_frac = rosin_rammler_fractions(d_min, d_mean, d_max, spread, n_diameters)

    print(f"Injection duration:     {injection_duration} s")
    print(f"Mass flow rate:         {injection_mass_per_second} kg/s per injection")
    print(f"Total mass injected:    {total_mass:.4e} kg per injection",
          f"({total_mass * 1e3:.4e} g)")
    print(f"Particles per parcel:   {particles_per_parcel}")
    print(f"Number of diameters:    {n_diameters}")
    for d, f in zip(d_bins, mass_frac):
        print(f"  d = {d * 1e6:.2f} um, mass fraction = {f:.4f}")

    n_total = 0
    for name, rho in densities.items():
        # total number of real particles injected
        n_rr = np.sum(total_mass * mass_frac / particle_mass(d_bins, rho))
        # number of parcels
        n_parcel = n_rr / particles_per_parcel
        n_total += n_rr

        print(f"\n--- {name} (rho = {rho} kg/m^3) ---")
        print(f"Total particle count:   {n_rr:.4e}")
        print(f"Particle flow rate:     {n_rr / injection_duration:.4e} /s")
        print(f"Total parcel count:     {n_parcel:.4e}")
        print(f"Parcel flow rate:       {n_parcel / injection_duration:.4e} /s")

    n_parcel_total = n_total / particles_per_parcel
    print("\n--- All injections ---")
    print(f"Total mass injected:    {total_mass * len(densities):.4e} kg")
    print(f"Total particle count:   {n_total:.4e}")
    print(f"Particle flow rate:     {n_total / injection_duration:.4e} /s")
    print(f"Total parcel count:     {n_parcel_total:.4e}"
          f" (at {particles_per_parcel} particles per parcel)")
    print(f"Parcel flow rate:       {n_parcel_total / injection_duration:.4e} /s")


if __name__ == "__main__":
    main()
