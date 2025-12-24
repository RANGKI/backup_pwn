#!/bin/bash
set -euo pipefail

# Save the flag in a sane place
if [ -e /flag ]; then
    mv "/flag" "/flag-$(tr -dc 'a-zA-Z0-9' < /dev/urandom | head -c 16)"
fi

# Route via the router
ip route del default
ip -6 route del default
ip route add default via "${ROUTER_IPV4}" dev eth0
ip -6 route add default via "${ROUTER_IPV6}" dev eth0 metric 1024 pref medium

# Exclude DNS from the VPN (paid feature)
echo "nameserver ${DNS}" > /etc/resolv.conf
case "${DNS}" in
    *.*) ip route add "${DNS}" via "${ROUTER_IPV4}" dev eth0;;
    *:*) ip -6 route add "${DNS}" via "${ROUTER_IPV6}" dev eth0;;
esac

# Run the rest as a normal user
# See https://stackoverflow.com/a/72037905 and the Dockerfile for why this is capsh instead of su.
capsh --inh=cap_net_admin --user=ctf -- '/user-entrypoint.sh'
