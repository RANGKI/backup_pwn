from pwn import *

context.arch = 'amd64'
context.os = 'linux'

elf = ELF.from_assembly(
    '''
        mov rdi, 0;
        mov rsi, rsp;
        sub rsi, 8;
        mov rdx, 300;
        syscall;
        ret;
        
        pop rax;
        ret;
        pop rdi;
        ret;
        pop rsi;
        ret;
        pop rdx;
        ret;
    '''
)
elf.save('vuln')