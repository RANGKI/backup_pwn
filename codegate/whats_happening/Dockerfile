FROM ubuntu:24.04@sha256:3afff29dffbc200d202546dc6c4f614edc3b109691e7ab4aa23d02b42ba86790

ENV user=whatshappening
ENV chall_port=33333

RUN apt-get update
RUN apt-get -y install socat adduser

RUN adduser -u 3333 $user

ADD ./deploy/prob /home/$user/prob

RUN chown root:$user /home/$user/
RUN chmod 755 /home/$user/prob

WORKDIR /home/$user
EXPOSE $chall_port
CMD socat TCP-LISTEN:$chall_port,reuseaddr,fork EXEC:"su -c './prob' $user",stderr
