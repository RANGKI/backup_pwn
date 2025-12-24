from pwn import *
libc = ELF("./libc.so.6")
print(hex(libc.sym['_IO_2_1_stdin_']))
