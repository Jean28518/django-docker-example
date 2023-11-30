#!/bin/sh

# Static files
python manage.py collectstatic --noinput

# Translation
python manage.py compilemessages

# Migrate
python manage.py migrate

# Set Debug to False
sed -i 's/DEBUG = True/DEBUG = False/g' demochecklist/settings.py

# Start server
gunicorn demochecklist.wsgi:application --bind 0.0.0.0:80