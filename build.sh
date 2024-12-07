#!/usr/bin/bash
# build.sh
set -o errexit  # exit on error

pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input
