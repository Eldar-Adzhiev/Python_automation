#!/usr/bin/env bash
mkdir -p tmp

docker network create ${NETWORK_NAME}
docker compose up --abort-on-container-exit