import pwn

def find_syscall_all_sections(binary_path):
    # Load the binary
    elf = pwn.context.binary = pwn.ELF(binary_path, checksec=False)
    
    # Byte pattern for syscall (0x0f 0x05)
    pattern = b'\x0f\x05'
    
    found = False
    # Iterate through all sections in the ELF file
    for section in elf.sections:
        section_name = section.name
        section_data = section.data()
        section_addr = section.header.sh_addr
        
        # Skip empty sections
        if not section_data:
            continue
        
        # Search for the pattern in the current section
        offset = 0
        while True:
            offset = section_data.find(pattern, offset)
            if offset == -1:  # No more occurrences in this section
                break
            # Calculate the virtual address of the match
            match_addr = section_addr + offset
            print(f"Found 'syscall' in section '{section_name}' at address: 0x{match_addr:x}")
            found = True
            offset += 1  # Move to the next byte to continue searching
    
    if not found:
        print("No 'syscall' pattern found in any section of the binary.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python find_syscall_all_sections.py <binary_path>")
        sys.exit(1)
    find_syscall_all_sections(sys.argv[1])
