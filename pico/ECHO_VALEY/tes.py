from pwn import *
exe = context.binary = ELF("./valley")
r = process()
r.shutdown('send')
r.interactive()
