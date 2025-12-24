FROM debian:bookworm-20250203-slim@sha256:40b107342c492725bc7aacbe93a49945445191ae364184a6d24fedb28172f6f7 AS ynetd-builder

ADD --chmod=0755 --checksum=sha256:c125df9762b0c7233459087bb840c0e5dbfc4d9690ee227f1ed8994f4d51d2e0 \
    https://raw.githubusercontent.com/reproducible-containers/repro-sources-list.sh/v0.1.4/repro-sources-list.sh \
    /usr/local/bin/repro-sources-list.sh

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked --mount=type=cache,target=/var/lib/apt,sharing=locked \
    /usr/local/bin/repro-sources-list.sh && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends --yes \
        musl-dev \
        musl-tools \
        make \
        xz-utils && \
    rm -f /usr/local/bin/repro-sources-list.sh

WORKDIR /work

ADD --chmod=0666 --checksum=sha256:4300f2fbc3996bc389d3c03a74662bfff3106ac1930942c5bd27580c7ba5053d \
    https://yx7.cc/code/ynetd/ynetd-0.1.2.tar.xz \
    /work/ynetd-0.1.2.tar.xz

RUN tar -xJf ynetd-0.1.2.tar.xz && cd ynetd-0.1.2 && CC="musl-gcc" CFLAGS="-static" make

FROM debian:bookworm-20250203-slim@sha256:40b107342c492725bc7aacbe93a49945445191ae364184a6d24fedb28172f6f7 AS challenge-builder

ADD --chmod=0755 --checksum=sha256:c125df9762b0c7233459087bb840c0e5dbfc4d9690ee227f1ed8994f4d51d2e0 \
    https://raw.githubusercontent.com/reproducible-containers/repro-sources-list.sh/v0.1.4/repro-sources-list.sh \
    /usr/local/bin/repro-sources-list.sh

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked --mount=type=cache,target=/var/lib/apt,sharing=locked \
    /usr/local/bin/repro-sources-list.sh && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends --yes \
        gcc libc-dev && \
    rm -f /usr/local/bin/repro-sources-list.sh

WORKDIR /work

COPY ./intro-rop.c /work/intro-rop.c

RUN gcc ./intro-rop.c -o ./intro-rop

RUN echo "e8004a854d4ad3ef7818f88632db90a31518445803d28fc7757d882ae162de1c  ./intro-rop" | sha256sum -c


FROM debian:bookworm-20250203-slim@sha256:40b107342c492725bc7aacbe93a49945445191ae364184a6d24fedb28172f6f7 AS runner

COPY --from=ynetd-builder /work/ynetd-0.1.2/ynetd /ynetd

COPY --from=challenge-builder /work/intro-rop /intro-rop
COPY ./flag /flag

EXPOSE 1024

CMD ["/ynetd", "-se", "y", "-p", "1024", "/intro-rop"]