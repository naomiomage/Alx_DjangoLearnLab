#!/usr/bin/env bash
# Exit on error
set -o errexit

# Upgrade pip and install build tools
pip install --upgrade pip setuptools wheel build setuptools-scm

# Install dependencies
pip install -r requirements.txt

# Run Django collectstatic (skip if not needed)
python manage.py collectstatic --noinput
