# Objetivo
I've hidden a flag in this file. Can you find it? [Forensics is fun.pptm](https://mercury.picoctf.net/static/2e739f9e0dc9f4c1556ea6b033c3ec8e/Forensics%20is%20fun.pptm)

# Solución
```
picoCTF{D1d_u_kn0w_ppts_r_z1p5}
```
# Notas
- Al usar unzip en el archivo se descomprimen varias carpetas, en la ruta ppt/slideMasters encontramos un archivo llamado "hidden", al hacerle un cat obtenemos una cadena en base64, usamos cyberchef para transformarla y obtenemos la bandera
# Referencia