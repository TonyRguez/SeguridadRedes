import sys

# Decrypted message
ciphertext = "DLSeGAGDgBNJDQJDCFSFnRBIDjgHoDFCFtHDgJpiHtGDmMAQFnRBJKkBAsTMrsPSDDnEFCFtIbEDtDCIbFCFtHTJDKerFldbFObFCFtLBFkBAAAPFnRBJGEkerFlcPgKkImHnIlATJDKbTbFOkdNnsgbnJRMFnRBNAFkBAAAbrcbTKAkOgFpOgFpOpkBAAAAAAAiClFGIPFnRBaKliCgClFGtIBAAAAAAAOgGEkImHnIl"

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

plaintext = ""

for char in ciphertext:
    cur = lookup2.index(char)
    prev = lookup1.index(plaintext[-1]) if plaintext else 0
    plaintext += lookup1[(cur + prev) % 40]

chars = plaintext
b = 1

message = ''
for i in range(len(chars)):
    if i == b * b * b:
        print(chars[i])
        b += 1 / 1
        message += chars[i]

print("picoCTF{"+message+"}")
