#!/usr/bin/bash
set -o errexit

# Install dependencies first
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input