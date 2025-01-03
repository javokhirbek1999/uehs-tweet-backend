#!/bin/bash

echo "Starting pre-deployment tasks..."

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Make Migrations
echo "Creating migrations..."
python manage.py makemigrations
python manage.py makemigrations api

# Apply migrations
echo "Applying migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Any additional commands can be added here
echo "Pre-deployment tasks completed."

