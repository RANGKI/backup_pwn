Dump of assembler code for function gadget_0:
   0x000055555555527a <+0>:     pop    rax
   0x000055555555527b <+1>:     ret
End of assembler dump.
pwndbg> disass gadget_1
Dump of assembler code for function gadget_1:
   0x000055555555527c <+0>:     add    rbx,r9
   0x000055555555527f <+3>:     ret
End of assembler dump.
pwndbg> disass gadget_2
Dump of assembler code for function gadget_2:
   0x0000555555555280 <+0>:     mov    rcx,QWORD PTR [rbx]
   0x0000555555555283 <+3>:     ret
End of assembler dump.
pwndbg> disass gadget_3
Dump of assembler code for function gadget_3:
   0x0000555555555284 <+0>:     mov    rax,r8
   0x0000555555555287 <+3>:     mov    rbx,r9
   0x000055555555528a <+6>:     mov    rcx,r10
   0x000055555555528d <+9>:     ret
End of assembler dump.
pwndbg> disass gadget_4
Dump of assembler code for function gadget_4:
   0x000055555555528e <+0>:     xor    rcx,rdi
   0x0000555555555291 <+3>:     xor    rbx,rdi
   0x0000555555555294 <+6>:     ret
End of assembler dump.
pwndbg> disass gadget_5
Dump of assembler code for function gadget_5:
   0x0000555555555295 <+0>:     push   rax
   0x0000555555555296 <+1>:     ret
End of assembler dump.
pwndbg> disass gadget_6
Dump of assembler code for function gadget_6:
   0x0000555555555297 <+0>:     xor    rax,rax
   0x000055555555529a <+3>:     xor    rsi,rsi
   0x000055555555529d <+6>:     ret
End of assembler dump.
pwndbg> disass gadget_7
Dump of assembler code for function gadget_7:
   0x000055555555529e <+0>:     sub    rax,0x8
   0x00005555555552a2 <+4>:     idiv   rdi
   0x00005555555552a5 <+7>:     ret
End of assembler dump.
pwndbg> disass gadget_8
Dump of assembler code for function gadget_8:
   0x00005555555552a6 <+0>:     add    rdi,r8
   0x00005555555552a9 <+3>:     ret
End of assembler dump.
pwndbg> disass gadget_9
Dump of assembler code for function gadget_9:
   0x00005555555552aa <+0>:     nop
   0x00005555555552ab <+1>:     ret
End of assembler dump.
pwndbg> disass gadget_10
Dump of assembler code for function gadget_10:
   0x00005555555552ac <+0>:     imul   rbx,rax
   0x00005555555552b0 <+4>:     ret
End of assembler dump.
pwndbg> disass gadget_11
Dump of assembler code for function gadget_11:
   0x00005555555552b1 <+0>:     xor    r9,r8
   0x00005555555552b4 <+3>:     xor    r8,r9
   0x00005555555552b7 <+6>:     xor    r9,r8
   0x00005555555552ba <+9>:     ret
End of assembler dump.
pwndbg> disass gadget_12
Dump of assembler code for function gadget_12:
   0x00005555555552bb <+0>:     mov    rcx,rsi
   0x00005555555552be <+3>:     add    rcx,r10
   0x00005555555552c1 <+6>:     ret
End of assembler dump.
pwndbg> disass gadget_13
Dump of assembler code for function gadget_13:
   0x00005555555552c2 <+0>:     xor    rdi,rcx
   0x00005555555552c5 <+3>:     xor    rsi,rcx
   0x00005555555552c8 <+6>:     ret
End of assembler dump.
pwndbg> disass gadget_14
Dump of assembler code for function gadget_14:
   0x00005555555552c9 <+0>:     pop    rbx
   0x00005555555552ca <+1>:     push   rdi
   0x00005555555552cb <+2>:     push   rbx
   0x00005555555552cc <+3>:     ret
End of assembler dump.
pwndbg> disass gadget_15
Dump of assembler code for function gadget_15:
   0x00005555555552cd <+0>:     pop    rbp
   0x00005555555552ce <+1>:     pop    rsi
   0x00005555555552cf <+2>:     ret
End of assembler dump.

bin_sh =  ► 0x555555555550 <print_stuff+102>    sub    rbx, rax                        RBX => 0x1287c3 (0x7ffff7f5ae43 - 0x7ffff7e32680)
system =   0x55555555557b <print_stuff+145>    sub    rbx, rax                        RBX => 0xfffffffffffd3250 (0x7ffff7e058d0 - 0x7ffff7e32680)
