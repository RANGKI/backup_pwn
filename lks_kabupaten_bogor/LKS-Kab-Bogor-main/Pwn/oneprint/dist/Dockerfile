FROM ubuntu:24.04

COPY flag.txt /flag.txt
COPY chall /chall

RUN apt-get update && apt-get install -y socat

EXPOSE 1337

CMD ["socat", "-T60", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:/chall,stderr"]