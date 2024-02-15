# Objetivo
The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once
# Datos de acceso
bandit8
TESKZC0XvTetK0S9xNwm25STk5iWrBvP
# Solución
```
bandit8@bandit:~$ ls
data.txt
bandit8@bandit:~$ sort data.txt | uniq -u
EN632PlfYiZbn3PhVK3XOGSlNInNE00t
bandit8@bandit:~$ 

```
# Notas
- Sort. Ordena lineas en un archivo de texto
- uniq -u. Toma las lineas de la salida de un comando y muestra solo la que no se repite
- uniq -c. Cuenta las veces que se repite una linea
# Referencia
Clase