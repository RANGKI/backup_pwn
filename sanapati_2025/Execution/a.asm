bits 64

sys_execve equ 59
sys_exit   equ 60

section .data
    child db "/bin/sh", 0

section .text
global _start
_start:
    mov rdi, child     ; filename
    xor rsi, rsi       ; argv = NULL
    xor rdx, rdx       ; envp = NULL
    mov rax, sys_execve
    syscall

    ; exit in case execve fails
    mov rdi, 1         ; exit code
    mov rax, sys_exit
    syscall
