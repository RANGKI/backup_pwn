FROM ubuntu:22.04@sha256:ed1544e454989078f5dec1bfdabd8c5cc9c48e0705d07b678ab6ae3fb61952d2

ENV user magic_palette
ENV chall_port 54321

RUN apt-get update
RUN apt-get -y install socat adduser

RUN adduser -u 5432 $user

ADD ./deploy/prob /home/$user/prob
ADD ./deploy/run.sh /home/$user/run.sh

RUN chown root:$user /home/$user/

RUN chmod 755 /home/$user/prob
RUN chmod +x /home/$user/run.sh

WORKDIR /home/$user
EXPOSE $chall_port
CMD socat TCP-LISTEN:$chall_port,reuseaddr,fork EXEC:./run.sh,stderr
