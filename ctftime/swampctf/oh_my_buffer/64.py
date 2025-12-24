from pwn import *
import time
exe = context.binary = ELF("./chall")
r = process()
r.sendline("2")
r.sendline("90")
# time.sleep(10)
r.sendline("A")
r.recvuntil(b"Sorry, we couldn't find the user: A\n")
print(r.recvline())
# r.interactive()
r.sendline("1")
