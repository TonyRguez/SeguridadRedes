# Objetivo
The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several ‘=’ characters.
# Datos de acceso
bandit9
EN632PlfYiZbn3PhVK3XOGSlNInNE00t
# Solución
```
bandit9@bandit:~$ ls
data.txt
bandit9@bandit:~$ strings data.txt
bandit9@bandit:~$ strings data.txt | grep "=="
```
# Notas
- strings. Extrae las cadenas de un archivo binario
# Referencia
Clases
