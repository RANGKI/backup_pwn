# MODE=static, DISK=<disk file>: embed the disk image in the Docker image
# MODE=dynamic: mount the disk image into the Docker image by hand (as /tunichtgut.qcow2)
ARG MODE=static
FROM debian:bookworm-20250203-slim@sha256:40b107342c492725bc7aacbe93a49945445191ae364184a6d24fedb28172f6f7 AS dynamic

ADD --chmod=0755 --checksum=sha256:c125df9762b0c7233459087bb840c0e5dbfc4d9690ee227f1ed8994f4d51d2e0 \
    https://raw.githubusercontent.com/reproducible-containers/repro-sources-list.sh/v0.1.4/repro-sources-list.sh \
    /usr/local/bin/repro-sources-list.sh

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked --mount=type=cache,target=/var/lib/apt,sharing=locked \
    /usr/local/bin/repro-sources-list.sh && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends --yes \
        qemu-system-x86 && \
    rm -f /usr/local/bin/repro-sources-list.sh

FROM dynamic AS static
ARG DISK=artifacts/tunichtgut.qcow2
COPY ${DISK} /tunichtgut.qcow2
FROM ${MODE} AS final

COPY entrypoint.sh launch.sh /
RUN chmod 0500 /entrypoint.sh /launch.sh
ENTRYPOINT ["/entrypoint.sh"]
