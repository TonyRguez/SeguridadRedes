# Objetivo
We have several pages hidden. Can you find the one with the flag?The website is running [here](http://saturn.picoctf.net:62050/).

# Solución
```
picoCTF{succ3ss_@h3n1c@10n_51b260fe}
```

# Notas
- Al entrar en la página e inspeccionarla, vemos que en los recursos encontramos un suburl llamado **secret**, al agregarlo y ver nuevamente los recursos encontramos que hay otro suburl llamado **hidden**, al entrar en el link vemos que nuevamente hay un suburl llamado **superhidden**, al entrar inspeccionamos la página y obtenemos la bandera.

# Referencias