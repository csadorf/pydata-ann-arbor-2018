#!/bin/bash

## Based on guidance provided here:
## https://medium.com/learning-machine-learning/present-your-data-science-projects-with-jupyter-slides-75f20735eb0f


jupyter nbconvert --to slides intro.ipynb --reveal-prefix=reveal.js 
mv intro.slides.html index.html
