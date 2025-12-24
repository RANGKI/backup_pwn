FROM debian:bookworm-20250203-slim@sha256:40b107342c492725bc7aacbe93a49945445191ae364184a6d24fedb28172f6f7

ADD --chmod=0755 --checksum=sha256:c125df9762b0c7233459087bb840c0e5dbfc4d9690ee227f1ed8994f4d51d2e0 \
    https://raw.githubusercontent.com/reproducible-containers/repro-sources-list.sh/v0.1.4/repro-sources-list.sh \
    /usr/local/bin/repro-sources-list.sh

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked --mount=type=cache,target=/var/lib/apt,sharing=locked \
    /usr/local/bin/repro-sources-list.sh && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends --yes \
        ca-certificates curl libcap2-bin iproute2 libssl3 && \
    rm -f /usr/local/bin/repro-sources-list.sh

RUN useradd -m -s /bin/bash ctf && \
    passwd -d ctf

COPY tunichtgut /usr/bin/tunichtgut
COPY entrypoint.sh /entrypoint.sh
COPY user-entrypoint.sh /user-entrypoint.sh

# /bin/ip: needed to inherit capabilities, https://stackoverflow.com/a/72037905
# SAFETY: This doesn't really matter since tunichtgut already has these capabilities for /dev/tun-related things
RUN chmod 555 /usr/bin/tunichtgut /entrypoint.sh /user-entrypoint.sh && \
    setcap 'cap_net_admin=eip' /usr/bin/tunichtgut && \
    setcap 'cap_net_admin=ei' /bin/ip

ENTRYPOINT ["/entrypoint.sh"]
