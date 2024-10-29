#!/bin/sh

set -o errexit
set -o nounset

echo "Starting celery worker..."
watchmedo auto-restart -d ./ -p '*.py' --recursive -- celery -A sport_connect_api.celery worker -l info