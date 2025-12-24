from pwn import *
from Crypto.Cipher import ARC4

context.arch = 'amd64'

pl = asm(
    shellcraft.open('.secret.enc', 'O_CREAT | O_RDWR', 0o644) +
    '''
    mov r10, rax
    ''' + 
    '''
    push 0x31337
    ''' * 2560 + 
    shellcraft.open('secret.png', 0) +
    shellcraft.read('rax', 'rsp', 0x5000) +
    '''
    mov r11, 0xffffffffffffffff
    enc:
    pop rax
    cmp rax, 0x31337
    je end
    xor rax, r11
    mov r11, rax
    push rax
    ''' + 
    shellcraft.write('r10', 'rsp', 8) +
    '''
    pop r11
    jmp enc
    end: 
    ret
    '''
)

print(list(pl), len(pl))