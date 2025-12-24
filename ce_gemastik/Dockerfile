FROM pwn.red/jail

COPY --from=ubuntu / /srv

COPY /src/chall /srv/app/run
COPY /src/flag /srv/app/flag

# randomize with flag-sha256sum
RUN mv /srv/app/flag /srv/app/flag-$(cat /srv/app/flag | sha256sum | cut -d' ' -f1).txt

ENV JAIL_MEM=5M JAIL_TIME=120 JAIL_PORT=1337