#!/bin/sh

# Wait for postgres to be ready
python manage.py wait_for_db

# Apply database migrations
python manage.py migrate

# Create superuser if it doesn't exist
python manage.py createsuperuser --noinput || true

# Start server
python manage.py runserver 0.0.0.0:8000
