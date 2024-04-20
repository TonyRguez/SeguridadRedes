# Objetivo
We found this weird message being passed around on the servers, we think we have a working decryption scheme.Download the message [here](https://artifacts.picoctf.net/c/128/message.txt).Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)
# Solución
```
Abrimos el archivo y vemos que debemos hacer módulo 37 a cada uno de los números separados por espacio, si el resultado va de 0 a 25 entonces es una letra, si va del 26 al 35 es un número y si es 36 entonces es "_".

Hacemos un programa en python que sea capaz de transformar el resultado en su equivalente en ascii para obtener la bandera

datos = open("message.txt").read().split()
flag = ""
c = ""
for n in datos:
        i = int(n) % 37
        if i >= 0 and i <= 25:
                c= chr(i + 65)
        elif i >= 26 and i <= 35:
                c = chr(i + 22)
        elif i == 36:
                c = "_"

        flag = flag + c
print(flag)

Obtenemos que el resultado del programa es
R0UND_N_R0UND_B6B25531

Agregamos el formato de la bandera y la metemos
```
# Notas
- PicoCTF{R0UND_N_R0UND_B6B25531}
# Referencia