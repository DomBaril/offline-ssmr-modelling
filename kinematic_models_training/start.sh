#!/bin/bash

if [[ "$OSTYPE" != "darwin"* ]]; then
     source ~/miniconda3/etc/profile.d/conda.sh
fi

ENV_REQUIRED="kinematic_model_training"

if [ "$CONDA_DEFAULT_ENV" != "$ENV_REQUIRED" ]; then
  conda activate $ENV_REQUIRED
fi

export JUPYTER_CONFIG_DIR="./config/"
jupyter lab
