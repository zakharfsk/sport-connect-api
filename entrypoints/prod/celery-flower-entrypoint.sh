#!/bin/bash

set -o errexit
set -o nounset

worker_ready() {
    celery -A sport_connect_api.celery inspect ping
}

until worker_ready; do
  >&2 echo 'Celery workers not available'
  sleep 1
done
>&2 echo 'Celery workers is available'

celery -A sport_connect_api.celery  \
    --broker="${REDIS_URL}0" \
    flower