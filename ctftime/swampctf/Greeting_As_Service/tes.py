from pwn import *
elf = ELF("./coredump_GAAS")
print(hex(elf.plt['printf']))  # Should match 0x401060
print(hex(elf.plt['gets']))    # Should match 0x401070
