# Objetivo
There's something in the [building](https://jupiter.challenges.picoctf.org/static/011955b303f293d60c8116e6a4c5c84f/buildings.png). Can you retrieve the flag?
# Solución
```
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ sudo gem install zsteg
Fetching iostruct-0.0.5.gem
Fetching zpng-0.4.5.gem
Fetching zsteg-0.2.13.gem
Successfully installed zpng-0.4.5
Successfully installed iostruct-0.0.5
Successfully installed zsteg-0.2.13
Parsing documentation for zpng-0.4.5
Installing ri documentation for zpng-0.4.5
Parsing documentation for iostruct-0.0.5
Installing ri documentation for iostruct-0.0.5
Parsing documentation for zsteg-0.2.13
Installing ri documentation for zsteg-0.2.13
Done installing documentation for zpng, iostruct, zsteg after 0 seconds
3 gems installed
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ zsteg -a buildings.png| grep picoCTF
b1,rgb,lsb,xy       .. text: "picoCTF{h1d1ng_1n_th3_b1t5}"


```
# Notas
- Al usar zsteg en el archivo, el programa utiliza todas las técnicas de esteganografía que sabe para decifrar el archivo, usamos grep para que filtre picoCTF y así obtener la bandera.
# Referencia