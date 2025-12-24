FROM ubuntu:24.04

# install packages
RUN apt-get update && \
    DEBAIN_FRONTEND=noninteractive apt-get install -qy xinetd build-essential

# new user: ctf
RUN useradd -m ctf

# copy files and compile binary
COPY src /home/ctf
COPY flag.txt /home/ctf/flag.txt

RUN gcc /home/ctf/chall.c -o /home/ctf/chall -fno-stack-protector -z execstack -no-pie

# set permission
RUN chown -R root:root /home/ctf
RUN chmod -R 755 /home/ctf
RUN chmod 444 /home/ctf/flag.txt

# startup.sh
COPY ./startup.sh /home/startup.sh
RUN chmod 700 /home/startup.sh

# xinetd
COPY ./xinetd /etc/xinetd.d/chal
RUN chmod 700 /etc/xinetd.d/chal

CMD ["/home/startup.sh"]

EXPOSE 9999
