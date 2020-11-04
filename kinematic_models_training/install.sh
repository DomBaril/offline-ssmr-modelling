#!/bin/bash

if [[ "$OSTYPE" != "darwin"* ]]; then
     source ~/miniconda3/etc/profile.d/conda.sh
fi

ENV_REQUIRED="kinematic_model_training"
ENV=$(conda env list)

if [[ "$ENV" == *"$ENV_REQUIRED"* ]]; then
  echo "Updating the environment"
  if [ "$CONDA_DEFAULT_ENV" != "$ENV_REQUIRED" ]; then
    conda activate $ENV_REQUIRED
  fi
  conda env update -q --file environment.yml --prune
else
  echo "Creating the environment"
  conda env create -f environment.yml
  conda activate powertrain_dynamics
fi

# Extensions for Jupyterlab
jupyter labextension install @jupyter-widgets/jupyterlab-manager

# Table of content
jupyter labextension install @jupyterlab/toc

# Interactive plot
jupyter labextension install jupyter-matplotlib

# Highlight typos when typing markdown
jupyter labextension install @ijmbarr/jupyterlab_spellchecker

# 3D plotting library
#jupyter labextension install k3d

# 3D plotting library
#jupyter labextension install ipyvolume
#jupyter labextension install jupyter-threejs

# nbgrader
# nbgrader 0.6 only work with notebooks, not lab yet...

jupyter nbextension enable --py widgetsnbextension

jupyter lab clean
jupyter lab build
