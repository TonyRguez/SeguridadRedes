# Objetivo
We have recovered a [binary](https://jupiter.challenges.picoctf.org/static/7aa5f383ec616fe9d72c2ffe1fabd0d9/rev) and a [text file](https://jupiter.challenges.picoctf.org/static/7aa5f383ec616fe9d72c2ffe1fabd0d9/rev_this). Can you reverse the flag.
# Solución
```
Abrimos el archivo rev en ghidra para ver que originalmente se usó C para codificar la bandera, hacemos el siguiente programa en Python

d = open("rev_this").read()

flag = ""
for j in range(8, 23):
        if j &  1 == 0:
                flag += chr(ord(d[j]) - 5)
        else:
                flag += chr(ord(d[j]) + 2)

print(flag)

el cuál nos regresa el pedazo de la bandera decodificada
```
# Notas
- picoCTF{r3v3rs36ad73964}
# Referencia