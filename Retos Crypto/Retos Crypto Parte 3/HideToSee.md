# Objetivo
How about some hide and seek heh?Look at this image [here](https://artifacts.picoctf.net/c/236/atbash.jpg).
# Solución
```
Descargamos la imagen y con la ayuda de la herramienta steghide extraemos la información de la imagen sin ninguna contraaseña, obtenemos krxlXGU{zgyzhs_xizxp_zx751vx6}, en CyberChef vemos que está codificado con el algoritmo AtBash, al decodificarlo obtenemos la bandera
picoCTF{atbash_crack_ac751ec6}

```
# Notas
- picoCTF{atbash_crack_ac751ec6}
# Referencia