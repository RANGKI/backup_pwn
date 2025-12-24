#!/bin/bash
set -euo pipefail

# Start the VPN (and keep restarting it if it crashes)
while true; do
    tunichtgut || echo 'VPN exited, restarting...'
    sleep 1
done &
sleep 1

# Do some stuff.
while true; do
    if ! ( curl --max-time 5 --silent https://tunichtgut.network/status/ || echo 'Connection to server failed...' >&2; ) | grep -q 'You are connected'; then
        echo -e '\x1b[31mYou are not connected to TUNichtgut\x1b[0m'
    else
        echo -e '\x1b[32mYou are connected to TUNichtgut\x1b[0m'
    fi
    sleep 30
done
