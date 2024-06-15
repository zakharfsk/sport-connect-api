#!/bin/sh

set -o errexit
set -o nounset

echo "Collect static..."
python manage.py collectstatic --noinput &&

echo "Migrate..."
python manage.py migrate --noinput &&

echo "Starting server..."
gunicorn 'sport_connect_api.wsgi' --reload --bind=0.0.0.0:8000
