# make_elf.py
with open("elf_payload", "wb") as f:
    f.write(bytes.fromhex(
        "7f454c46020101000000000000000000"  # ELF header
        "02003e00010000007800000000000000"  # Type, Machine, Entry = 0x78
        "40000000000000004000000000000000"  # PH offset, SH offset (unused)
        "00000000000000003800000001000000"  # Flags, EH size, PH num

        # Program header (PT_LOAD)
        "01000000000000000000000000000000"  # Type, offset
        "00000000000000000000000000000000"  # Vaddr, Paddr
        "58000000000000005800000000000000"  # Filesz, Memsz = 0x58
        "0500000000000000"                  # Flags (r+x), align

        # Code (starts at 0x78)
        "4831f6"                            # xor rsi, rsi
        "4831d2"                            # xor rdx, rdx
        "488d3d1a000000"                    # lea rdi, [rip+0x1a] -> "/bin/sh"
        "488d742400"                        # lea rsi, [rsp]
        "b00b"                              # mov al, 0xb (execve syscall)
        "0f05"                              # syscall

        # "/bin/sh\0-s\0"
        "2f62696e2f7368002d7300"            # "/bin/sh\0-s\0"
    ))
