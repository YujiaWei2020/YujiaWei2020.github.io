---
title: AI4CFD Module in FreeCAD
featured: true
date: 2026-06-22
tags:
  - AI
  - CFD
  - FreeCAD
  - DeepLearning

image:
  caption: ''
  focal_point: Center
  # Only used as the card/list thumbnail; the single page shows the repo details below instead.
  preview_only: true

url_code: 'https://github.com/YujiaWei2020/AI4CFD-freecad'
---
This project delivers the world's first open-source physical AI software embedded directly within FreeCAD. Designed to be user-friendly, it's built to support any CFD project.

<!--more-->

## Roadmap

![CFD-AI Module in FreeCAD roadmap](featured.png)

## Features

- **Physics-informed AI** — surrogate model trained on CFD results for fast hydrodynamic prediction
- **Automated design space search** — explores geometric parameters to find optimal configurations
- **FreeCAD integration** — runs entirely within the FreeCAD environment, no external solver setup required

## Requirements

- [FreeCAD](https://www.freecad.org/) 1.00+
- Python 3.12+

## Installation

```bash
git clone https://github.com/YujiaWei2020/AI4CFD-freecad.git
```

On Windows:

1. Go to the `freecad_addon` folder
2. Double-click `install.bat`
3. The installer automatically searches for your Python environment (3.12.x); if not found, install Python manually
4. All requirements are then installed automatically

## Usage

1. Open **FreeCAD**
2. Find the AI4CFD module under your addon manager
3. Set your working directory
4. Add design parameters and run CFD batches

## Airfoil Design Exploration

![Airfoil design space exploration](airfoils.gif)

## Manifold CFD Example

![Manifold CFD mesh in FreeCAD](profile.png)

## Design Space Exploration

{{< video src="design space exploration.mp4" controls="yes" >}}
