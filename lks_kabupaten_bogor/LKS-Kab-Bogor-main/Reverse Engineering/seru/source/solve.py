from pwn import xor
from libnum import s2n, n2s

data = open('.secret.enc', 'rb').read()
print(len(data))
res = b''
key = 0xffffffffffffffff
for i in range(0, len(data), 8):
    tmp = s2n(data[i:i+8])
    res += n2s(tmp ^ key).rjust(8, b'\x00')
    key = tmp

with open('flag.png', 'wb') as f:
    f.write(res)