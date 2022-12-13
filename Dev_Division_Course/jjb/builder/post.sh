#!/usr/bin/env bash
docker network remove ${NETWORK_NAME}
docker compose down || true
