#!/usr/bin/env bash

while [[ "$status" != *"healthy"* ]]
do
    status=$(curl -u "${STORAGE_USER}:${STORAGE_PASSWORD}" \
      http://"${STORAGE_HOST}":8091/pools/default 2>/dev/null \
      | sed 's/.*status\"://g' \
      | sed 's/,.*//')
    sleep 2
done
