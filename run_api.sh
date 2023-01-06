#!/bin/bash

# Activate the new environment
source fastapi-env/bin/activate

# Run the app
uvicorn main:app &