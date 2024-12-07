#!/usr/bin/bash
set -o errexit

# Install dependencies first
pip install -r requirements.txt

# Change to the project directory
cd searchProject

# Collect static files
python manage.py collectstatic --no-input