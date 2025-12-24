#!/bin/bash
set -euo pipefail

echo "${FLAG:-The server will have the real flag instead of this (and somehow, it was not passed into Docker)}" > /flag
chmod 0400 /flag

/launch.sh --disk=/tunichtgut.qcow2 --flag=/flag
