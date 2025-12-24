FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && \
    apt-get install -y socat libstdc++6 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Create challenge directory
WORKDIR /home/ctf

# Copy binary and flag
COPY chall /home/ctf/chall
COPY flag.txt /home/ctf/flag.txt

# Make binary executable and secure the flag
RUN chmod 755 /home/ctf/chall && \
    chmod 440 /home/ctf/flag.txt && \
    chown root:root /home/ctf/flag.txt /home/ctf/chall

# Add non-privileged user
RUN useradd -m ctf

# Make sure everything in /home/ctf is owned by ctf except flag
RUN chown -R ctf:ctf /home/ctf && \
    chown root:root /home/ctf/flag.txt

# Drop privileges to 'ctf' for the challenge binary, but flag.txt stays owned by root and is only readable
USER ctf

# Expose port
EXPOSE 1337

# Launch the challenge with socat
ENTRYPOINT ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:/home/ctf/chall,stderr"]
