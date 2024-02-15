# Objetivo
The password for the next level is stored **somewhere on the server** and has all of the following properties:

- owned by user bandit7
- owned by group bandit6
- 33 bytes in size
# Datos de acceso
bandit6
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU
# Solución
```
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/
cat: /var/lib/dpkg/info/: Is a directory
bandit6@bandit:~$ cd /var/lib/dpkg/info/
bandit6@bandit:/var/lib/dpkg/info$ cat bandit7.password 
z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

```
# Notas
- find
	- -user. Permite especificar el usuario
	- -group. Permite especificar el grupo
- 2>/dev/null. Enviar la salida de error al dispositivo null (que no aparezca en pantalla)
# Referencia
Clase