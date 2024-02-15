# Objetivo
The password for the next level is stored in a file called **-** located in the home directory
# Datos de acceso
bandit1
NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL
# Solución
```
bandit1@bandit:~$ cat ./-
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
bandit1@bandit:~$ pwd
/home/bandit1
bandit1@bandit:~$ cat /home/bandit1/-
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
bandit1@bandit:~$ 
```
# Notas

- Ctrl + A. Manda el cursor al inicio de la linea de comando
- Ctrl + E. Manda el cursor al final de la linea de comandos
- Ctrl + C. Interrumpir comando
- pwd sirve para ver la ruta actual
- Si un nombre de archivo inicia con guión, se debe poner ./ para referirse a ese archivo
# Referencia
Clase