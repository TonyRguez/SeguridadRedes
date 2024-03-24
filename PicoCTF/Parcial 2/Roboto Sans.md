# Objetivo

The flag is somewhere on this web application not necessarily on the website. Find it.Check [this](http://saturn.picoctf.net:63195/) out.
# Solución
```
picoCTF{Who_D03sN7_L1k5_90B0T5_22ce1f22}
```

# Notas
- Al entrar a la página e ir a ver el archivo **robots.txt** encontramos un texto en base 64, si lo decodificamos en CyberChef la segunda linea nos indica js/myfile.txt, al entrar a ese suburl obtenemos la bandera

# Referencias