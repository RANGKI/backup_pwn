FROM ubuntu:latest

RUN dpkg --add-architecture i386

RUN apt update -y

RUN apt install libc6:i386 libncurses5:i386 libstdc++6:i386 socat -y

WORKDIR /app

COPY ./src/* .

EXPOSE 5000

RUN chmod 4655 chall

RUN chown root:root flag.txt

RUN chmod 600 flag.txt

CMD socat TCP4-LISTEN:5000,reuseaddr,fork EXEC:./chall
