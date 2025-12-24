from pwn import *
from ctypes import CDLL

context.binary = binary = ELF('./main', checksec=False)
libc = CDLL('/lib/x86_64-linux-gnu/libc.so.6')

# Connect to the remote service
# p = process()
p = remote("20.244.40.210",6000)

cookies = [
    "Chocolate Chip", "Sugar Cookie", "Oatmeal Raisin", "Peanut Butter", "Snickerdoodle", 
    "Shortbread", "Gingerbread", "Macaron", "Macaroon", "Biscotti", "Butter Cookie", 
    "White Chocolate Macadamia Nut", "Double Chocolate Chip", "M&M Cookie", "Lemon Drop Cookie", 
    "Coconut Cookie", "Almond Cookie", "Thumbprint Cookie", "Fortune Cookie", "Black and White Cookie", 
    "Molasses Cookie", "Pumpkin Cookie", "Maple Cookie", "Espresso Cookie", "Red Velvet Cookie", 
    "Funfetti Cookie", "S'mores Cookie", "Rocky Road Cookie", "Caramel Apple Cookie", "Banana Bread Cookie", 
    "Zucchini Cookie", "Matcha Green Tea Cookie", "Chai Spice Cookie", "Lavender Shortbread", "Earl Grey Tea Cookie", 
    "Pistachio Cookie", "Hazelnut Cookie", "Pecan Sandies", "Linzer Cookie", "Spritz Cookie", 
    "Russian Tea Cake", "Anzac Biscuit", "Florentine Cookie", "Stroopwafel", "Alfajores", 
    "Polvorón", "Springerle", "Pfeffernüsse", "Speculoos", "Kolaczki", 
    "Rugelach", "Hamantaschen", "Mandelbrot", "Koulourakia", "Melomakarona", 
    "Kourabiedes", "Pizzelle", "Amaretti", "Cantucci", "Savoiardi (Ladyfingers)", 
    "Madeleine", "Palmier", "Tuile", "Langue de Chat", "Viennese Whirls", 
    "Empire Biscuit", "Jammie Dodger", "Digestive Biscuit", "Hobnob", "Garibaldi Biscuit", 
    "Bourbon Biscuit", "Custard Cream", "Ginger Nut", "Nice Biscuit", "Shortcake", 
    "Jam Thumbprint", "Coconut Macaroon", "Chocolate Crinkle", "Pepparkakor", "Sandbakelse", 
    "Krumkake", "Rosette Cookie", "Pinwheel Cookie", "Checkerboard Cookie", "Rainbow Cookie", 
    "Mexican Wedding Cookie", "Snowball Cookie", "Cranberry Orange Cookie", "Pumpkin Spice Cookie", 
    "Cinnamon Roll Cookie", "Chocolate Hazelnut Cookie", "Salted Caramel Cookie", "Toffee Crunch Cookie", 
    "Brownie Cookie", "Cheesecake Cookie", "Key Lime Cookie", "Blueberry Lemon Cookie", 
    "Raspberry Almond Cookie", "Strawberry Shortcake Cookie", "Neapolitan Cookie"
]

# Seed the random number generator with the current time
seed = libc.time(0x0)
libc.srand(seed)

# Guess the cookies 100 times in a row
for _ in range(100):
    cookie_index = libc.rand() % 100
    correct_cookie = cookies[cookie_index]

    info(f'Guessing: {correct_cookie}')

    p.recvuntil(b'Guess the cookie: ')
    p.sendline(correct_cookie.encode())

    response = p.recvline().decode()
    if 'Wrong' in response:
        break

p.interactive()
