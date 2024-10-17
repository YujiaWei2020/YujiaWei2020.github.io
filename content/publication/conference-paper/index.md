---
title: 'A fluid-structure interaction model on the hydroelastic analysis of a container ship using PRECICE'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin
  - Tahsin Tezdogan

# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'

date: '2013-07-01T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2017-01-01T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *American Society of Mechanical Engineers
publication_short: In *OMAE*

abstract: Commercial vessels have recently shown a common trend in increasing their sizes to meet the growing demand for transportation and operations. This trend may however result in more flexible or ‘softer’ hulls. The flexible hull structure reduces the ship natural frequency close to the wave encounter frequency, increasing the probability of resonance or high-frequency vibrations. Meanwhile, the resulting structural deformations from flexible hull could significantly affect the flow field and the hydrodynamic loads cannot be estimated accurately. Hence, it is important to treat a flexible hull and its surrounding flow field as an interacting system to predict a ship’s dynamic behaviour based on the hydroelastic theory. In this study, a novel fluid-structure interactions coupling scheme using the “preCICE” library to communicate with the fluid solver “OpenFOAM” and structure solver “calculiX” was first proposed to study the hydroelastic behavior of a container ship with a forward speed in regular waves. With the advantage of this numerical model, the flexible behaviour of this ship, such as its vertical bending displacement and corresponding bending moment can be quantified, and the “springing” and “whipping” responses can be calculated. It is believed that the present FSI model will exhibit more advantages over the traditional rigid-body methods currently used in the ship seakeeping field.

# Summary. An optional shortened abstract.
summary: First FSI model using preCICE connect OpenFOAM and Calculix for ship hydroelasticity analysis.

tags:
  - FSI

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: ''
url_code: 'https://asmedigitalcollection.asme.org/OMAE/proceedings-abstract/OMAE2022/V007T08A035/1148005'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
  - example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

{{% callout note %}}
Create your slides in Markdown - click the _Slides_ button to check out the example.
{{% /callout %}}

Add the publication's **full text** or **supplementary notes** here. You can use rich formatting such as including [code, math, and images](https://docs.hugoblox.com/content/writing-markdown-latex/).
