#!/bin/bash
chmod +x install_scripts/*.sh
pip install -q ipywidgets
jupyter nbextension enable --py widgetsnbextension
