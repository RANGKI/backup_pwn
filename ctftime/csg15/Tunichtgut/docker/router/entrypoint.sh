#!/bin/bash
set -euo pipefail

# NAT packets properly
nft add table inet router
nft add chain inet router nat '{ type nat hook postrouting priority srcnat; policy accept; }'
nft add rule inet router nat masquerade

# Allow users to SSH into this machine.
dropbear -BEFRjkwp 1024
