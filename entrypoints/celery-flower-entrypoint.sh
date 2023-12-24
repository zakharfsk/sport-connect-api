#!/bin/sh

echo "Starting celery Flower..."

celery -A sport_connect_api.celery flower --port=5555 --persisten=True