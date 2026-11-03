---
title: DPM Particle Calculator
summary: Estimate particle and parcel counts for Fluent DPM injections with a Rosin-Rammler size distribution.
date: 2026-11-03
type: docs
math: true
tags:
  - CFD
  - DPM
  - Fluent
---

This calculator estimates how many particles and parcels an ANSYS Fluent Discrete Phase Model (DPM) injection produces. It's useful for checking particle counts and parcel settings before you run a simulation.

## Calculator

Change any input and the results update instantly. Diameters are entered in µm.

{{< dpm-calculator >}}

## Method

The total mass injected by each injection is the mass flow rate multiplied by the injection duration:

{{< math >}}
$$m_{\text{total}} = \dot{m}\,(t_{\text{end}} - t_{\text{start}})$$
{{< /math >}}

The diameter distribution follows Rosin-Rammler, where the mass fraction of particles larger than {{< math >}}$d${{< /math >}} is

{{< math >}}
$$Y_d = \exp\left[-\left(\frac{d}{\bar{d}}\right)^{n}\right]$$
{{< /math >}}

with mean diameter {{< math >}}$\bar{d}${{< /math >}} and spread parameter {{< math >}}$n${{< /math >}}. As in Fluent, the range {{< math >}}$[d_{\min}, d_{\max}]${{< /math >}} is split into evenly spaced discrete diameters {{< math >}}$d_i${{< /math >}}. Each one takes the mass fraction {{< math >}}$f_i${{< /math >}} of the interval around it, normalised so the fractions sum to 1.

The number of real particles of density {{< math >}}$\rho${{< /math >}} is

{{< math >}}
$$N = \sum_i \frac{f_i\, m_{\text{total}}}{\rho\, \pi d_i^3 / 6}$$
{{< /math >}}

and the number of parcels is {{< math >}}$N${{< /math >}} divided by the number of particles per parcel. Flow rates are these totals divided by the injection duration.

## Python script

The same calculation as a standalone script: [download dpm_particle_calculator.py](dpm_particle_calculator.py). It needs NumPy.

{{< resource-code file="dpm_particle_calculator.py" lang="python" summary="Show source" >}}
