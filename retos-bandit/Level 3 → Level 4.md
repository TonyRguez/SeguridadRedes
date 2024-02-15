# Objetivo
The password for the next level is stored in a hidden file in the **inhere** directory.
# Datos de acceso
bandit3
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
# Solución
```
bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ cd inhere/
bandit3@bandit:~/inhere$ ls
bandit3@bandit:~/inhere$ ls -la
total 12
drwxr-xr-x 2 root    root    4096 Oct  5 06:19 .
drwxr-xr-x 3 root    root    4096 Oct  5 06:19 ..
-rw-r----- 1 bandit4 bandit3   33 Oct  5 06:19 .hidden
bandit3@bandit:~/inhere$ cat .hidden
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe
```
# Notas
- ls -la. Muestra los archivos de formato largo, incluyendo los ocultos
- Navegar por la ventana de manual de un comando 
	- Flechas, av pag, reg pag
	- /bus. sirve para hacer una búsqueda
	- n para buscar hacia adelante
	- shift + n para buscar hacia atrás
	- q para salir del manual
	- h para recibir ayuda de las teclas a usar estando dentro del manual
# Referencia
Clase
