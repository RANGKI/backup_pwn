import numpy as np
from PIL import Image

class Affine:
    def __init__(self, a, b, m=256):
        self.a = a
        self.b = b
        self.m = m
        self.a_inv = pow(a, -1, m)  # Modular inverse of 'a' under mod 'm'

    def E(self, x):
        return (self.a * x + self.b) % self.m

    def D(self, x):
        return (self.a_inv * (x - self.b)) % self.m

def affine_decrypt(img, a, b, m=256):
    decrypted_img = img.copy()
    height, width = decrypted_img.shape[:2]

    affine = Affine(a, b, m)

    for i in range(height):
        for j in range(width):
            pixel = decrypted_img[i][j]
            r = affine.D(pixel[0])
            g = affine.D(pixel[1])
            b = affine.D(pixel[2])
            decrypted_img[i][j] = [r, g, b]

    return decrypted_img


def matrix_decrypt(encrypted_img, key):
        """
        Matrix-based decryption method
        """
        # Extract the transformation matrix A
        n = key.shape[0] - 1
        A = key[:n, :n]

        # Extract original image dimensions
        l_mod = int(key[-1][0])
        l_rem = key[-1][1]
        w_mod = int(key[-1][2])
        w_rem = key[-1][3]

        # Compute original dimensions
        l = l_mod * 256 + l_rem
        w = w_mod * 256 + w_rem

        # Modulus used in encryption
        Mod = 256

        # Decrypt each color channel
        Dec1 = (np.matmul(A % Mod, encrypted_img[:, :, 0] % Mod)) % Mod
        Dec2 = (np.matmul(A % Mod, encrypted_img[:, :, 1] % Mod)) % Mod
        Dec3 = (np.matmul(A % Mod, encrypted_img[:, :, 2] % Mod)) % Mod

        # Resize and concatenate decrypted channels
        Dec1 = np.resize(Dec1, (Dec1.shape[0], Dec1.shape[1], 1))
        Dec2 = np.resize(Dec2, (Dec2.shape[0], Dec2.shape[1], 1))
        Dec3 = np.resize(Dec3, (Dec3.shape[0], Dec3.shape[1], 1))
        Dec = np.concatenate((Dec1, Dec2, Dec3), axis=2)

        # Crop back to original dimensions
        Dec = Dec[:l, :w]

        return Dec

def save_image(img, filename):
    image = Image.fromarray(img.astype(np.uint8))
    image.save('result/'+filename)



img = Image.open("image_encrypted.png")
img_array = np.array(img)
key = np.load('key.npy')
temp = matrix_decrypt(img_array,key)
for a in range(1,256,2):
        temp=affine_decrypt(temp,a,a+2)
        save_image(temp,str(a)+str(a+2)+'decrpyt.png')