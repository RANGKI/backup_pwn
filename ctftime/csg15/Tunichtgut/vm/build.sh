#!/bin/bash
# Note to infrastructure people: This does not use d2vm, since we actually _need_ Docker inside the VM.
set -euo pipefail
cd "$(dirname "$(realpath "${BASH_SOURCE[0]}")")"
trap 'docker compose --file compose.builder.yml down' EXIT
docker compose --file compose.builder.yml up --build --force-recreate
