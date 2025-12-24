#!/bin/bash

# Start the challenge in the background with socat
socat TCP-LISTEN:1470,reuseaddr,fork EXEC:/home/pwn/chall,su=nobody &

# Wait a moment to ensure it starts
sleep 1

# Wait 15 seconds so you can attach from your host
echo "[*] Waiting 15 seconds for you to manually attach gdbserver..."
sleep 15

# Get the PID of the running chall binary
CHALL_PID=$(pgrep chall)

# Start gdbserver and attach to it
echo "[*] Starting gdbserver on 0.0.0.0:1337, attached to PID $CHALL_PID"
exec gdbserver 0.0.0.0:1337 --attach "$CHALL_PID"
