#!/bin/bash

# Upgrade the system
sudo apt update
sudo apt -y upgrade

# Install the necessary packages for python3 installationa and environment
sudo apt install -y build-essential libssl-dev libffi-dev 
sudo apt install -y python3 python3-pip python3-venv python3-dev

# Create a new environment
python3 -m venv fastapi-env

# Activate the new environment
source $(pwd)/fastapi-env/bin/activate

# Install the packages in the new environment
pip install -r requirements.txt