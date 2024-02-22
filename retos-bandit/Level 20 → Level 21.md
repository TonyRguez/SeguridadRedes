# Objetivo
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).
# Datos de acceso
bandit20
VxCazJaVykI6W36BkBU0mJTCM8rR95XT
# Solución
```
bandit20@bandit:~$ nc -lnvp 3570 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT &
[1] 3070501
bandit20@bandit:~$ Listening on 0.0.0.0 3570
./suconnect
Usage: ./suconnect <portnumber>
This program will connect to the given port on localhost using TCP. If it receives the correct password from the other side, the next password is transmitted back.
bandit20@bandit:~$ ./suconnect 3570
Connection received on 127.0.0.1 54596
Read: VxCazJaVykI6W36BkBU0mJTCM8rR95XT
Password matches, sending next password
NvEJF7oVjkddltPSrdKEFOllh9V1IBcq
[1]+  Done                    nc -lnvp 3570 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT
bandit20@bandit:~$ 
```
# Notas
- tmux puede hacer que dividas tu consola de comandos
	- ctrl + b % para crear una consola en vertical
	- puedes usar ctrl + b : y escribir setw -g mouse on para activar el mouse
	- ctrl + b flechitas para poder moverte entre terminales sin usar el mouse
# Referencia