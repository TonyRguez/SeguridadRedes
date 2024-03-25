# Objetivo
Can you find the flag? [shark1.pcapng](https://mercury.picoctf.net/static/81c7862241faf4a48bd64a858392c92b/shark1.pcapng).
# Solución
```
picoCTF{p33kab00_1_s33_u_deadbeef}
```
# Notas
- Descargamos y abrimos el archivo en wireshark, seguimos el stream de TCP, en el stream 5 encontramos una cadena rotada 13 veces, la desencriptamos en cyberchef y obtenemos la bandera
# Referencia