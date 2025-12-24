from pwn import *
elf = context.binary = ELF("./tic")
p = process()
p.sendline("x")
p.sendline(b"\x36")
p.sendline(b"\x35")
print(p.recv(9999))