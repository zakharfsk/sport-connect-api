#!/bin/sh

set -o errexit
set -o nounset

echo "Collect static..."
python manage.py collectstatic --noinput &&

echo "Load fixtures..."
python manage.py loaddata fixtures/sport.json fixtures/sport_school.json fixtures/sport_standards.json fixtures/avarage_values_standards.json fixtures/weightingfactors.json fixtures/users_and_school.json

echo "Make migrations..."
python manage.py makemigrations &&

echo "Migrate..."
python manage.py migrate --noinput &&

echo "Starting server..."
gunicorn 'sport_connect_api.wsgi' --reload --bind=0.0.0.0:8000
