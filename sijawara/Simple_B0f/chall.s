	.file	"chall.c"
	.intel_syntax noprefix
	.text
	.globl	flushBuffers
	.type	flushBuffers, @function
flushBuffers:
.LFB6:
	.cfi_startproc
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	mov	edi, 0
	call	fflush@PLT
	nop
	pop	rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE6:
	.size	flushBuffers, .-flushBuffers
	.section	.rodata
.LC0:
	.string	"/bin/cat flag.txt"
	.text
	.globl	flag
	.type	flag, @function
flag:
.LFB7:
	.cfi_startproc
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	lea	rax, .LC0[rip]
	mov	rdi, rax
	call	system@PLT
	mov	eax, 0
	call	flushBuffers
	nop
	pop	rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE7:
	.size	flag, .-flag
	.section	.rodata
.LC1:
	.string	"SMKN7Semarang"
	.text
	.globl	isPasswordCorrect
	.type	isPasswordCorrect, @function
isPasswordCorrect:
.LFB8:
	.cfi_startproc
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	sub	rsp, 16
	mov	QWORD PTR -8[rbp], rdi
	mov	rax, QWORD PTR -8[rbp]
	mov	edx, 13
	lea	rcx, .LC1[rip]
	mov	rsi, rcx
	mov	rdi, rax
	call	strncmp@PLT
	test	eax, eax
	sete	al
	movzx	eax, al
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE8:
	.size	isPasswordCorrect, .-isPasswordCorrect
	.section	.rodata
	.align 8
.LC2:
	.string	"Selamat datang di permainan BINARY EXPLOITATION\n"
	.align 8
.LC3:
	.string	"langkah pertama masukkan password terlebih dahulu:"
.LC4:
	.string	"%s"
	.align 8
.LC5:
	.string	"Maaf password yang anda masukkan salah!"
	.align 8
.LC6:
	.string	"Langkah pertama telah diselesaikan anda berhasil masuk.\nFLAG:"
.LC7:
	.string	"ERROR, INCORRECT PASSWORD!"
	.text
	.globl	authentication
	.type	authentication, @function
authentication:
.LFB9:
	.cfi_startproc
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	sub	rsp, 80
	mov	DWORD PTR -4[rbp], 0
	lea	rax, .LC2[rip]
	mov	rdi, rax
	call	puts@PLT
	lea	rax, .LC3[rip]
	mov	rdi, rax
	call	puts@PLT
	mov	eax, 0
	call	flushBuffers
	lea	rax, -80[rbp]
	mov	rsi, rax
	lea	rax, .LC4[rip]
	mov	rdi, rax
	mov	eax, 0
	call	__isoc99_scanf@PLT
	cmp	DWORD PTR -4[rbp], 0
	jne	.L6
	lea	rax, .LC5[rip]
	mov	rdi, rax
	call	puts@PLT
	mov	eax, 0
	call	flushBuffers
	jmp	.L5
.L6:
	lea	rax, -80[rbp]
	mov	rdi, rax
	call	isPasswordCorrect
	cmp	eax, 1
	jne	.L8
	lea	rax, .LC6[rip]
	mov	rdi, rax
	call	puts@PLT
	mov	eax, 0
	call	flag
	jmp	.L5
.L8:
	lea	rax, .LC7[rip]
	mov	rdi, rax
	call	puts@PLT
	mov	eax, 0
	call	flushBuffers
.L5:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE9:
	.size	authentication, .-authentication
	.globl	main
	.type	main, @function
main:
.LFB10:
	.cfi_startproc
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	mov	rax, QWORD PTR stdin[rip]
	mov	esi, 0
	mov	rdi, rax
	call	setbuf@PLT
	mov	rax, QWORD PTR stdout[rip]
	mov	esi, 0
	mov	rdi, rax
	call	setbuf@PLT
	mov	eax, 0
	call	authentication
	mov	eax, 0
	pop	rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE10:
	.size	main, .-main
	.ident	"GCC: (Debian 12.2.0-14) 12.2.0"
	.section	.note.GNU-stack,"",@progbits
