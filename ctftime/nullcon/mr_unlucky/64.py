import time
from ctypes import CDLL
from pwn import *

# Load the C standard library for rand() and srand()
libc = CDLL('libc.so.6')

# List of Dota 2 heroes in the exact order from the server
heroes = [
    "Anti-Mage", "Axe", "Bane", "Bloodseeker", "Crystal Maiden",
    "Drow Ranger", "Earthshaker", "Juggernaut", "Mirana", "Morphling",
    "Phantom Assassin", "Pudge", "Shadow Fiend", "Sniper", "Storm Spirit",
    "Sven", "Tiny", "Vengeful Spirit", "Windranger", "Zeus"
]

def try_seed(seed):
    try:
        # Connect to the server
        p = remote('52.59.124.14', 5201)
        # Seed the PRNG with the current candidate
        libc.srand(seed)
        # Wait for the first input prompt
        p.recvuntil('Guess the Dota 2 hero (case sensitive!!!): ')
        
        for i in range(50):
            # Generate the next hero using the same PRNG sequence as the server
            hero = heroes[libc.rand() % 20]
            # Send the hero name
            p.sendline(hero)
            # Wait for the success message
            p.recvuntil('was right! moving on to the next guess...\n')
            # If not the last iteration, wait for the next prompt
            if i != 49:
                p.recvuntil('Guess the Dota 2 hero (case sensitive!!!): ')
        
        # After all correct guesses, receive the flag
        flag = p.recvline()
        print(flag.decode())
        p.close()
        return True
    except:
        p.close()
        return False

# Get the current time and test nearby seeds to account for possible delay
current_time = int(time.time())
for delta in range(-2, 3):
    seed = current_time + delta
    print(f"Attempting seed: {seed}")
    if try_seed(seed):
        print("Flag captured successfully!")
        break
    