# Objetivo
What does asm2(0x4,0x2d) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://jupiter.challenges.picoctf.org/static/ceac75672637589213b952abe32c84b3/test.S)
# Solución
```
Al analizar el código vemos que tenemos un ciclo que se va a repetir 118 veces hasta que la condición sea falsa, en cada iteración vemos que suma 1 a la variable que originalmente tenía 0x2d (45 en decimal) y es el valor que queremos obtener, si sumamos 118 veces al 0x2d obtenemos el valor de la bandera, en este caso, 0xa3
```
# Notas
- 0xa3
# Referencia
