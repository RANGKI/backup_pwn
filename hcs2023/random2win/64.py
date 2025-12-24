from pwn import *
elf = context.binary = ELF("./chall")
from ctypes import CDLL
p = process()
libc = CDLL("/lib/x86_64-linux-gnu/libc.so.6")
random = libc.rand() % 640
p.sendline(str(random))
print(p.recvall().strip().decode())