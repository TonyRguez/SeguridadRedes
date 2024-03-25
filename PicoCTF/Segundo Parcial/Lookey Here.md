# Objetivo
Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it.Download the data [here](https://artifacts.picoctf.net/c/126/anthem.flag.txt).
# Solución
```
┌──(kalicura㉿rufian)-[~/SeguridadRedes/PicoCTF/Segundo Parcial]
└─$ cat anthem.flag.txt | grep 'pico'
      we think that the men of picoCTF{gr3p_15_@w3s0m3_2116b979}
```
# Notas
- Descargamos el archivo y usamos cat para ver el contenido, usamos grep para filtrar la palabra pico y encontramos la bandera
# Referencia