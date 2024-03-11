#!/bin/bash

set -o errexit
set -o nounset

worker_ready() {
  (cd ./sport_connect_api && celery -A sport_connect_api.celery inspect ping)
}

until worker_ready; do
  >&2 echo 'Celery workers not available'
  sleep 1
done
>&2 echo 'Celery workers is available'

(cd ./sport_connect_api && celery \
  --broker="${RABBMITMQ_URL}" \
  flower \
  --broker_api="${RABBMITMQ_API}" \
  --debug \
  --persistent=True \
  --db=./flower.db \
  --state_save_interval=10000 \
  purge_offline_workers=10s
)