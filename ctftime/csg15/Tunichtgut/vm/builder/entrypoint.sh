#!/bin/bash
set -euo pipefail

if [ ! -d /artifacts/ ]; then
    echo 'artifacts directory not mounted into builder container' >&2
    exit 1
fi
if [ ! -d /builder/ ]; then
    echo 'builder directory not mounted into builder container' >&2
    exit 1
fi
if [ ! -d /docker/ ]; then
    echo 'docker setup not mounted into builder container' >&2
    exit 1
fi
if [ ! -e /var/run/docker.sock ]; then
    echo 'docker socket not mounted into builder container' >&2
    exit 1
fi
if [ ! -e /dev/kvm ]; then
    echo '/dev/kvm not available in builder container' >&2
    exit 1
fi
if [ ! -f /launch.sh ]; then
    echo 'launch.sh script not mounted into builder container' >&2
    exit 1
fi

rm -rf -- /work/
mkdir -p /work/
mkdir /work/docker/

# Grab the base image, if it's not cached
if [ ! -f /artifacts/base-image.qcow2 ] || ! echo '073073594e14f3134b1036dce3a198f592e93e56781bdd33a063aa042810aa82  /artifacts/base-image.qcow2' | sha256sum -c -; then
    wget -O /artifacts/base-image.qcow2 https://cloud.debian.org/images/cloud/bookworm/20250210-2019/debian-12-genericcloud-amd64-20250210-2019.qcow2
fi
rm -f /artifacts/cloud-init.iso /artifacts/tunichtgut.qcow2
cp -a /artifacts/base-image.qcow2 /artifacts/tunichtgut.qcow2

# Build the actual Docker images we want to run in the VM, then save them and the compose file to the ISO
cd /docker/
docker compose build
for image in $(docker compose config --images); do # docker compose images only works for _created_ containers!
    hashed="$(docker image inspect --format='{{.ID}}' "${image}" | sed 's/sha256://')"
    docker image save "${image}" | gzip > "/work/docker/${hashed}.tar.gz"
done
cp -a /docker/compose.yml /work/docker/compose.yml

# Copy over the systemd units (we want to fetch the flag on boot, so relying on restart=unless-stopped is probably the wrong thing to do).
cp -ar /builder/systemd /work/systemd
cp -ar /builder/challenge.sh /work/

# Copy over the rest of the cloud-init setup
cp -a /builder/cloud-init/* /work/

# Build the cloud-init iso image
mkisofs -output /artifacts/cloud-init.iso -volid cidata -graft-points -joliet -joliet-long -rational-rock /work/

# Boot the image once, to run the init code
/launch.sh --disk=/artifacts/tunichtgut.qcow2 --iso=/artifacts/cloud-init.iso --writable
