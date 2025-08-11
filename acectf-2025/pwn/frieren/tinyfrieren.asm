;; tiny.asm: Copyright (C) 1999 Brian Raiter <breadbox@muppetlabs.com>
;; Licensed under the terms of the GNU General Public License, either
;; version 2 or (at your option) any later version.
;;
;; To build:
;;	nasm -f bin -o tiny tiny.asm && chmod +x tiny

BITS 32
  
		org	0x00010000
  
		db	0x7F, "ELF"
		dd	1
		dd	0
		dd	$$
		dw	2
		dw	3
		dd	_start
		dd	_start
		dd	4
_start:		mov	bl, 42			; set ebx to exit code 42
		xor	eax, eax		; set eax to 1 (exit syscall)
		inc	eax
		int	0x80			; and exit
		db	0
		dw	0x34
		dw	0x20
		db	1
  
filesize	equ	$ - $$

;; This is how the file looks when it is read as an (incomplete) ELF
;; header, beginning at offset 0:
;;
;; e_ident:	db	0x7F, "ELF"			; required
;;		db	1				; 1 = ELFCLASS32
;;		db	0				; (garbage)
;;		db	0				; (garbage)
;;		db	0				; (garbage)
;;		db	0x00, 0x00, 0x00, 0x00		; (unused)
;;		db	0x00, 0x00, 0x01, 0x00
;; e_type:	dw	2				; 2 = ET_EXE
;; e_machine:	dw	3				; 3 = EM_386
;; e_version:	dd	0x00010020			; (garbage)
;; e_entry:	dd	0x00010020			; program starts here
;; e_phoff:	dd	4				; phdrs located here
;; e_shoff:	dd	0xB340C031			; (garbage)
;; e_flags:	dd	0x0080CD2A			; (unused)
;; e_ehsize:	dw	0x0080				; (garbage)
;; e_phentsize:	dw	0x20				; phdr entry size
;; e_phnum:	db	1				; one phdr in the table
;; e_shentsize:
;; e_shnum:
;; e_shstrndx:
;;
;; This is how the file looks when it is read as a program header
;; table, beginning at offset 4:
;;
;; p_type:	dd	1				; 1 = PT_LOAD
;; p_offset:	dd	0				; read from top of file
;; p_vaddr:	dd	0x00010000			; load at this address
;; p_paddr:	dd	0x00030002			; (unused)
;; p_filesz:	dd	0x00010020			; too big, but ok
;; p_memsz:	dd	0x00010020			; equal to file size
;; p_flags:	dd	4				; 4 = PF_R
;; p_align:	dd	0xB340C031			; (garbage)
