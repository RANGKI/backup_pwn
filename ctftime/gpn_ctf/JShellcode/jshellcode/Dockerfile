# docker build -t jshellcode .
# docker run --rm -it -p 1337:1337 jshellcode
# ncat localhost 1337
FROM openjdk:22-bullseye

RUN apt-get update && apt-get -qq -y --no-install-recommends install \
    curl \
    unzip \
    zip \
    socat \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY executor.jar .
COPY watcher.jar .

COPY encrypted /flag
COPY --chmod=600 password /password

RUN useradd -u 2000 user

CMD ["socat", "-v", "tcp-listen:1337,reuseaddr,fork", "EXEC:'java -jar --enable-native-access=ALL-UNNAMED /watcher.jar /executor.jar'"]
