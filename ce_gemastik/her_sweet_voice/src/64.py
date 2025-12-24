from pwn import *

exe = context.binary = ELF("./chall")
r = process()
offset = 0
rop = ROP(exe)
