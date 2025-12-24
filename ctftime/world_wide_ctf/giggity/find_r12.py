import pwn
from capstone import *

def find_r12_syscall_ret(binary_path):
    # Set architecture and initialize context
    pwn.context.arch = 'amd64'
    elf = pwn.context.binary = pwn.ELF(binary_path, checksec=False)
    
    # Get the .text section
    text_section = elf.get_section_by_name('.text')
    if not text_section:
        print("No .text section found in the binary!")
        return
    
    # Read the bytes and base address of the .text section
    text_data = text_section.data()
    text_addr = text_section.header.sh_addr
    
    # Initialize capstone disassembler
    md = Cs(CS_ARCH_X86, CS_MODE_64)
    md.detail = True  # Enable detailed disassembly
    
    found = False
    # Disassemble the .text section
    instructions = list(md.disasm(text_data, text_addr))
    
    # Iterate through instructions
    for i in range(len(instructions) - 2):  # -2 to ensure room for syscall and ret
        instr = instructions[i]
        
        # Check if the current instruction references r12
        if 'r12' in instr.op_str or 'r12' in instr.reg_name(instr.reg_read(0)) or 'r12' in instr.reg_name(instr.reg_write(0)):
            # Look ahead for syscall (0x0f 0x05) and ret (0xc3)
            j = i + 1
            syscall_found = False
            while j < len(instructions) and j < i + 5:  # Look ahead up to 5 instructions
                next_instr = instructions[j]
                if next_instr.mnemonic == 'syscall':
                    syscall_found = True
                    break
                j += 1
            
            # If syscall was found, check for ret
            if syscall_found and j < len(instructions) - 1:
                for k in range(j + 1, min(j + 3, len(instructions))):  # Look for ret within 2 instructions
                    if instructions[k].mnemonic == 'ret':
                        # Pattern found: r12-related instruction, followed by syscall, then ret
                        print(f"Pattern found at address 0x{instr.address:x}:")
                        print(f"  {instr.address:#x}: {instr.mnemonic} {instr.op_str} (uses r12)")
                        print(f"  {instructions[j].address:#x}: syscall")
                        print(f"  {instructions[k].address:#x}: ret")
                        found = True
                        break
    
    if not found:
        print("No pattern found: instruction using r12 followed by syscall and ret.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python find_r12_syscall_ret.py <binary_path>")
        sys.exit(1)
    find_r12_syscall_ret(sys.argv[1])
