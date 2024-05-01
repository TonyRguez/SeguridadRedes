# Objetivo
Can you get the flag?Download this [binary](https://artifacts.picoctf.net/c/85/gdbme).Here's the test drive instructions:

- `$ chmod +x gdbme`
- `$ gdb gdbme`
- `(gdb) layout asm`
- `(gdb) break *(main+99)`
- `(gdb) run`
- `(gdb) jump *(main+104)`
# Solución
```
Al usar los comandos anteriores le damos permisos al archivo, después lo abrimos con gdb, el comando layout sirve para ver el programa en una ventana arriba, ponemos un break en la linea 99 para que no se ejecute el sleep, después usamos run y jump para saltarnos a la linea 104 la cuál nos arroja la bandera

```
# Notas
- picoCTF{d3bugg3r_dr1v3_197c378a}
# Referencia
