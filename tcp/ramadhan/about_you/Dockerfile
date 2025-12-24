FROM ubuntu:jammy

EXPOSE 1337 1470

RUN apt update && apt install -y socat gdbserver

RUN mkdir /home/pwn
COPY flag.txt /home/pwn/flag.txt
COPY chall /home/pwn/chall
COPY start.sh /home/pwn/start.sh
WORKDIR /home/pwn

RUN chmod -R 755 /home/pwn
RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /usr/bin/env /bin/dash /bin/bash /bin/sh /bin/cat /usr/bin/id /bin/ls /usr/bin/pgrep /usr/bin/gdbserver

CMD ["bash", "/home/pwn/start.sh"]
