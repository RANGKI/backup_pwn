#!/bin/bash
set -euo pipefail

# Install Docker
apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends \
    ca-certificates curl
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sha256sum -c - <<EOF
1500c1f56fa9e26b9b8f42452a553675796ade0807cdce11975eb98170b3a570  /etc/apt/keyrings/docker.asc
EOF

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian $(. /etc/os-release && echo "$VERSION_CODENAME") stable" > /etc/apt/sources.list.d/docker.list
apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends \
    docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Save the compose file and wrapper script
mkdir -p /challenge/
install --mode=0444 /mnt/docker/compose.yml /challenge/
install --mode=0500 /mnt/challenge.sh /challenge/

# Enable Docker
systemctl enable --now docker.service

# Import all the images
for image in /mnt/docker/*.tar.gz; do
    docker image load --input "${image}"
done

# Copy over our systemd units, and enable the services
install --mode=0644 --owner=root --target-directory=/etc/systemd/system/ /mnt/systemd/*
systemctl daemon-reload
for service in /mnt/systemd/*.service; do
    systemctl enable "$(basename "${service}")"
done
