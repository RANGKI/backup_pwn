#!/bin/bash
set -euo pipefail

compose=(/usr/bin/docker compose --file /challenge/compose.yml --project-directory /challenge/)
export COMPOSE_MENU=0
export DOCKER_CLI_HINTS=false

function start_challenge {
    flag_source="${FLAG_SOURCE:-/dev/vdb}"
    if [ ! -e "${flag_source}" ]; then
        echo "Flag source ${flag_source} does not exist, starting with placeholder flag" >&2
    elif [ ! -f "${flag_source}" ] && [ ! -b "${flag_source}" ]; then
        echo "Flag source ${flag_source} is not a file or block device, starting with placeholder flag" >&2
    else
        if [ -b "${flag_source}" ]; then
            size="$(blockdev --getsize64 "${flag_source}")"
        elif [ -f "${flag_source}" ]; then
            size="$(stat --format='%s' "${flag_source}")"
        else
            size=0
        fi
        if [ "${size}" -le 0 ]; then
            echo "Flag source ${flag_source} is empty, starting with placeholder flag" >&2
        elif [ "${size}" -gt 40960 ]; then
            echo "Flag source ${flag_source} is way too large (${size} bytes), starting with placeholder flag" >&2
        else
            export FLAG="$(tr -dc '[:print:]' < "${flag_source}")"
        fi
    fi

    "${compose[@]}" up # No --detach - we need this to stick around for systemd to not go insane...
}
function stop_challenge {
    "${compose[@]}" down
}

case "$1" in
    start) start_challenge;;
    stop) stop_challenge;;
    *) echo "Unknown command: $1" >&2; exit 1;;
esac
