# Stage 1: Prepare challenge environment using Python
FROM python@sha256:f2fdaec50160418e0c2867ba3e254755edd067171725886d5d303fd7057bbf81 AS app

RUN mkdir -p /challenge
WORKDIR /challenge

COPY chall .
COPY flag.txt .
COPY wrapper.py .

# Stage 2: Final jail stage with static gdbserver
FROM pwn.red/jail

# Copy static gdbserver
COPY ./gdbserver /usr/bin/gdbserver
RUN chmod +x /usr/bin/gdbserver

# Copy challenge files from app stage
COPY --from=app / /srv

# Add run script
RUN mkdir -p /srv/app
COPY --chmod=555 ./run /srv/app/run

# Jail configuration
ENV JAIL_PIDS=10 JAIL_MEM=15M JAIL_TIME=120 JAIL_PORT=5000
