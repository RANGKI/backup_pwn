#!/usr/bin/env python3

# List of hexadecimal values from %8$p to %12$p (relevant for ASCII decoding)
hex_values = [
    "0x54436f6b656e6f4b",  # %8$p
    "0x6e696b61656c7b46",  # %9$p
    "0x68745f6c6c615f67",  # %10$p
    "0x73676e6968745f65",  # %11$p
    "0x7d"                  # %12$p
]

def hex_to_ascii(hex_str):
    # Remove '0x' prefix and ensure the string is clean
    hex_str = hex_str.replace("0x", "")
    # Pad with zeros if needed (e.g., for %12$p which is shorter)
    hex_str = hex_str.zfill(16) if len(hex_str) > 2 else hex_str.zfill(2)
    # Convert hex string to bytes (big-endian)
    try:
        # Split into pairs of characters (bytes)
        byte_pairs = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]
        # Reverse for little-endian to big-endian
        byte_pairs = byte_pairs[::-1]
        # Convert each byte pair to ASCII if printable
        ascii_str = ""
        for byte in byte_pairs:
            char_code = int(byte, 16)
            # Only include printable ASCII characters (32-126)
            if 32 <= char_code <= 126:
                ascii_str += chr(char_code)
            else:
                ascii_str += f"[0x{byte}]"  # Non-printable placeholder
        return ascii_str
    except ValueError:
        return "[invalid hex]"

# Decode each hex value and concatenate
result = ""
for i, hex_val in enumerate(hex_values, start=8):
    decoded = hex_to_ascii(hex_val)
    print(f"%{i}$p: {hex_val} -> {decoded}")
    # Skip %8$p ("KonekoCT") as it’s not part of the flag
    if i >= 9:
        result += decoded

# Print the final decoded string
print("\nFinal decoded string:", result)
