# Objetivo

I just recently learnt about the SRA public key cryptosystem... or wait, was it supposed to be RSA? Hmmm, I should probably check...Connect to the program on our server: `nc saturn.picoctf.net 60874`Download the program: [chal.py](https://artifacts.picoctf.net/c/297/chal.py)

# Solución
```
from Crypto.Util.number import isPrime, long_to_bytes
from string import ascii_letters, digits
from itertools import combinations
from sympy import divisors
from math import log2

anger = 15529048211176481540924151200919205436976136617346100704918981908396120352748
envy = 86045178503491600186231432954033839924923073631196251394263398533463402607573
sloth = 65537

ds = divisors(envy * sloth - 1)
primes = [x + 1 for x in ds if isPrime(x + 1)]
correct_size_primes = [x for x in primes if log2(x) // 1 == 127]

valid_plaintexts = []
charset = ascii_letters + digits
for p, q in combinations(correct_size_primes, 2):
    try:
        s = long_to_bytes(pow(anger, envy, p * q)).decode("ascii")
        if all([c in charset for c in s]):
            valid_plaintexts.append(s)
    except Exception:
        continue

print(valid_plaintexts)


Usamos el programa anterior en python para obtener el texto plano, el resultado lo ponemos en la consola con el servidor conectado y nos da la bandera

┌──(kalicura㉿rufian)-[~/SeguridadRedes/PicoCTF/Tercer Parcial/Tercer Parcial pt 1]
└─$ nc saturn.picoctf.net 62357
anger = 15529048211176481540924151200919205436976136617346100704918981908396120352748
envy = 86045178503491600186231432954033839924923073631196251394263398533463402607573
vainglory?
> R6klbdO5sCW3wc1V
R6klbdO5sCW3wc1V
Conquered!
picoCTF{7h053_51n5_4r3_n0_m0r3_38268294}

```
# Notas
- picoCTF{7h053_51n5_4r3_n0_m0r3_38268294}
# Referencia
- https://stackotter.dev/blog/picoctf-2023-sra-writeup#what-do-we-need