# Objetivo
In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](https://mercury.picoctf.net/static/2604f8b51a5cc62d38a3736938f19cef/values)
# Solución
```
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Retos Crypto/Retos Crypto Parte 3]
└─$ cat values    
Decrypt my super sick RSA:
c: 861270243527190895777142537838333832920579264010533029282104230006461420086153423
n: 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e: 65537                                                                                                                                                          
Entramos a factordb para factorizar n y así obtener los valores de p y q, aplicamos las formulas de RSA 

┌──(kalicura㉿rufian)-[~/SeguridadRedes/Retos Crypto/Retos Crypto Parte 3]
└─$ python
Python 3.11.7 (main, Dec  8 2023, 14:22:46) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> p = 1955175890537890492055221842734816092141
>>> q = 670577792467509699665091201633524389157003
>>> p * q
1311097532562595991877980619849724606784164430105441327897358800116889057763413423
>>> n = p * q
>>> e = 65537
>>> c = 861270243527190895777142537838333832920579264010533029282104230006461420086153423
>>> tn = (p-1)*(q-1)
>>> d = pow(e, -1, tn)
>>> m = pow(c, d, n)
>>> hex(m)[2:]
'7069636f4354467b736d6131315f4e5f6e305f67306f645f31333638363637397d'
>>> 
KeyboardInterrupt
>>> bytes.fromhex(hex(m)[2:])
b'picoCTF{sma11_N_n0_g0od_13686679}'
>>> 


```
# Notas
- 
# Referencia