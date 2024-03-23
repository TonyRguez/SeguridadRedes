# Objetivo
We found this [file](https://mercury.picoctf.net/static/7b2d7c26630e977197022d0af09e3aeb/tunn3l_v1s10n). Recover the flag.
# Solución
```
picoCTF{qu1t3_a_v13w_2020}

```
# Notas
- Al usar xxd nos damos cuenta de que es un archivo bmp creado en windows pero tiene varios datos erroneos, estos se corrigen usando hexeditor, al momento de poder abrir la imagen nos damos cuenta de que aún no está la bandera, al editar nuevamente con hexeditor para aumentar la altura de la imagen podemos encontrar la bandera.
# Referencia