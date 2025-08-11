; execve("/bin/sh", NULL, NULL)
BITS 64
ORG 0x400000

    ; ELF Header
    db 0x7f, "ELF"      ; Magic
    db 2                ; 64-bit
    db 1                ; Little endian
    db 1                ; ELF version
    db 0                ; System V
    db 0                ; ABI version
    times 7 db 0        ; Padding

    dw 2                ; Executable file
    dw 0x3e             ; x86-64
    dd 1                ; ELF version
    dq _start           ; Entry point
    dq phdr - $$        ; Program header offset
    dq 0                ; Section header offset
    dd 0                ; Flags
    dw ehdrsize         ; ELF header size
    dw phdrsize         ; Program header size
    dw 1                ; Number of program headers
    dw 0, 0, 0          ; No section headers

ehdrsize: equ $ - $$

phdr:
    dd 1                ; PT_LOAD
    dd 0
    dq 0
    dq $$               ; Virtual address
    dq filesize         ; File size
    dq filesize         ; Memory size
    dq 0x1000           ; Align

phdrsize: equ $ - phdr

_start:
    xor rsi, rsi        ; argv = NULL
    xor rdx, rdx        ; envp = NULL
    mov rdi, binsh
    mov al, 59          ; execve syscall number
    syscall

binsh:
    db "/bin/sh", 0

filesize: equ $ - $$
