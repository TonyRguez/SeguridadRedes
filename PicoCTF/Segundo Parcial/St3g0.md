# Objetivo
Download this image and find the flag.

- [Download image](https://artifacts.picoctf.net/c/217/pico.flag.png)
# Solución
```
┌──(kalicura㉿rufian)-[~/SeguridadRedes/PicoCTF/Segundo Parcial]
└─$ zsteg -a pico.flag.png | grep 'pico'
b1,rgb,lsb,xy       .. text: "picoCTF{7h3r3_15_n0_5p00n_a9a181eb}$t3g0"
```
# Notas
- Usamos el comando zsteg para decodificar la imagen, al usar -a le decimos que intente con todos los métodos conocidos y usamos grep pico para filtrar y encontrar la bandera.
# Referencia