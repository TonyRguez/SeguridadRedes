# Objetivo
Let's decrypt this: [ciphertext](https://jupiter.challenges.picoctf.org/static/ee7e2388b45f521b285334abb5a63771/ciphertext)? Something seems a bit small.
# Solución
```
Sabemos que la fórmula para encriptar es c = m^e mod n, al hacer un cat al documento vemos que e = 3, por lo que c = m ^ 3, y al despejar m = raiz³ de c

Abrimos python y hacemos lo siguiente:

>>> from Crypto.Util.number import long_to_bytes
>>> from gmpy2 import *
>>> 
>>> gmpy2.get.context().precision=2048
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'gmpy2.gmpy2' has no attribute 'get'
>>> gmpy2.get_context().precision=2048
>>> e = 3
>>> c = 2205316413931134031074603746928247799030155221252519872649649212867614751848436763801274360463406171277838056821437115883619169702963504606017565783537203207707757768473109845162808575425972525116337319108047893250549462147185741761825125
>>> 
>>> root. exact = iroot(c, e)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'builtin_function_or_method' object has no attribute 'exact'
>>> root, exact = iroot(c, e)
>>> root
mpz(13016382529449106065894479374027604750406953699090365388202874238148389207291005)
>>> long_to_bytes(root)
b'picoCTF{n33d_a_lArg3r_e_606ce004}'
>>> 

```
# Notas
- picoCTF{n33d_a_lArg3r_e_606ce004}
# Referencia