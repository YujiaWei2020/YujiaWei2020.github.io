---
# Display name
title: Yujia Wei

# Full name (for SEO)
first_name: Yujia
last_name: Wei

# Is this the primary user of the site?
superuser: true

# Highlight the author in author lists? (true/false)
highlight_name: true

# Role/position/tagline
role: Senior CFD-AI Engineer

# Organizations/Affiliations to display in Biography blox
organizations:
  - name: Severn Trent Water
    url: ''

# Social network links
# Need to use another icon? Simply download the SVG icon to your `assets/media/icons/` folder.
profiles:
  - icon: at-symbol
    url: 'yujia.wei@cranfield.ac.uk'
    label: E-mail Me
  - icon: brands/x
    url: https://twitter.com/GetResearchDev
  - icon: brands/instagram
    url: https://www.instagram.com/
  - icon: brands/github
    url: https://github.com/YujiaWei2020/
  - icon: brands/linkedin
    url: https://www.linkedin.com/in/yujia-wei-47720b231/
  - icon: academicons/google-scholar
    url: https://scholar.google.com/citations?user=Zjb9VTwAAAAJ&hl=en&oi=sra/
  - icon: academicons/orcid
    url: https://orcid.org/0000-0002-5186-6141/

interests:
  - Fluid Structure Interaction
  - Computational Fluid Dynamics
  - Deep Learning

education:
  - area: PhD Fluid Structure Interaction
    institution: University of Strathclyde
    date_start: 2019-10-01
    date_end: 2023-03-31
    summary: |
      Thesis on Fluid-structure interaction models on the hydroelastic analysis of containerships in waves. Presented papers at OMAE19 conference, being published in Marine Structures and Ocean Engineering.
    button:
      text: 'Read Thesis'
      url: 'https://stax.strath.ac.uk/concern/theses/c534fp60d'
  - area: MSC Naval Architecture and Ocean Engineering
    institution: University of Strathclyde
    date_start: 2018-09-01
    date_end: 2019-09-01
    summary: |
      GPA: Distinction
  - area: BEng Naval Architecture and Ocean Engineering
    institution: University of Strathclyde
    date_start: 2017-09-01
    date_end: 2015-09-01
    summary: |
      GPA: Honor
      
work:
  - position: Senior CFD-AI Engineer
    company_name: Severn Trent Water
    company_url: ''
    company_logo: ''
    date_start: 2025-03-01
    date_end: ''
    summary: |2-
      - Designed and built STverse, a modular CFD-AI platform spanning the full simulation-to-deployment stack: geometry ingestion, automated CFD orchestration, data pipeline and validation, surrogate model training, and production inference.
      - Architected a fully automated CFD batch runner with parallel cloud sweeps; failed or non-converged cases are automatically quarantined, with uncertainty quantification to minimise high-fidelity data acquisition costs.
      - Established MLOps workflows for dataset and surrogate-model versioning and production inference monitoring.
      - Geometry optimisation pipelines delivered 24% efficiency gains on contact tanks and 40% on settlement tanks; Qt-based interface enables non-specialists to run full optimisation workflows without CFD expertise.
      - Led the technical design team and mentored graduate engineers on surrogate model design and physics-informed ML research.
      - Stack: Python, PyTorch, OpenFOAM, VTK, PyVista, SLURM, AWS, Qt, MLflow
  - position: Developer – AI4CFD FreeCAD Module
    company_name: Open Source / Independent
    company_url: ''
    company_logo: ''
    date_start: 2025-01-01
    date_end: ''
    summary: |2-
      - Built and maintain "AI4CFD", the first open-source CFD-AI module for the FreeCAD framework, covering geometry preprocessing, batch simulation runners, surrogate AI training, inference, and design optimisation.
      - Implemented point-cloud and graph-based deep learning algorithms preserving mesh connectivity for geometry-invariant training; training pipelines support distributed GPU execution with live monitoring via Weights & Biases.
      - Designed a shared geometry/data interface supporting CFD, FEA, and particle-simulation workflows, with plug-in compatibility across solvers (OpenFOAM, CalculiX, ANSYS FLUENT, DualSPHysics).
      - Applied to pipe-layout optimisation for data-centre cooling (University of Oxford) and underwater airfoil optimisation for a marine design company.
  - position: Research Fellow
    company_name: Cranfield University – Airbus Digital
    company_url: ''
    company_logo: ''
    date_start: 2023-03-01
    date_end: 2025-03-01
    summary: |2-
      - Contributed to multiphase CFD modelling for aircraft landing processes within the Airbus Digital LandOne programme, running simulations on HPC clusters for large parametric sweeps.
      - Developed machine-learning surrogates trained on Airbus experimental datasets to characterise extreme operating conditions across landing gear systems.
      - Deployed digital twin systems coupling surrogate models with live test data for design-space exploration and manufacturing risk reduction.
      - Conducted FEA stress and fatigue analysis across hybrid material configurations, achieving over 30% rigidity improvement.
  - position: Research Assistance
    company_name: University of Strathclyde
    company_url: ''
    company_logo: ''
    date_start: 2020-06-01
    date_end: 2022-12-31
    summary: |
      - Hydrodynamic analysis of offshore platform



# Skills
# Add your own SVG icons to `assets/media/icons/`
skills:
  - name: Skills
    items:
      - name: Computation modelling
        description: ''
        percent: 80
        icon: code-bracket
      - name: Data Science
        description: ''
        percent: 100
        icon: chart-bar
      - name: Python, C++
        description: ''
        percent: 40
        icon: circle-stack
  - name: Hobbies
    color: '#eeac02'
    color_border: '#f0bf23'
    items:
      - name: Hiking
        description: ''
        percent: 60
        icon: person-simple-walk
      - name: Dogs
        description: ''
        percent: 100
        icon: dog
      - name: Workout
        description: ''
        percent: 80
        icon: camera

languages:
  - name: English
  - name: Chinese



# Awards.
#   Add/remove as many awards below as you like.
#   Only `title`, `awarder`, and `date` are required.
#   Begin multi-line `summary` with YAML's `|` or `|2-` multi-line prefix and indent 2 spaces below.
awards:
  - title: Future leader 
    url: https://www.worldlabs.org/opportunity/gfil-future-frontiers-fund-fff-q1-2023
    date: '2023-07-01'
    awarder: Green Future Investments Ltd (GFIL)
    icon: 
    summary: |
      I won future leader funding with £10k from GFIL onto the advanved design of offshore renewable systems.
  # - title: Blockchain Fundamentals
  #   url: https://www.edx.org/professional-certificate/uc-berkeleyx-blockchain-fundamentals
  #   date: '2023-07-01'
  #   awarder: edX
  #   icon: edx
  #   summary: |
  #     Learned:
  #     - Synthesize your own blockchain solutions
  #     - Gain an in-depth understanding of the specific mechanics of Bitcoin
  #     - Understand Bitcoin’s real-life applications and learn how to attack and destroy Bitcoin, Ethereum, smart contracts and Dapps, and alternatives to Bitcoin’s Proof-of-Work consensus algorithm
  # - title: 'Object-Oriented Programming in R'
  #   url: https://www.datacamp.com/courses/object-oriented-programming-with-s3-and-r6-in-r
  #   certificate_url: https://www.datacamp.com
  #   date: '2023-01-21'
  #   awarder: datacamp
  #   icon: datacamp
  #   summary: |
  #     Object-oriented programming (OOP) lets you specify relationships between functions and the objects that they can act on, helping you manage complexity in your code. This is an intermediate level course, providing an introduction to OOP, using the S3 and R6 systems. S3 is a great day-to-day R programming tool that simplifies some of the functions that you write. R6 is especially useful for industry-specific analyses, working with web APIs, and building GUIs.
---

## About Me

Hello, I'm a Senior CFD-AI Engineer at Severn Trent Water, building production-grade physics-informed AI platforms for engineering simulation. My background spans Fluid Structure Interaction, computational fluid dynamics (OpenFOAM), and deep learning, with a PhD from the University of Strathclyde and postdoctoral research at Cranfield University in collaboration with Airbus Digital.

I also develop AI4CFD, the first open-source CFD-AI module for FreeCAD, making physics-informed AI accessible to the broader engineering community. This portfolio showcases my projects, publications, and open-source contributions. Feel free to get in touch!


