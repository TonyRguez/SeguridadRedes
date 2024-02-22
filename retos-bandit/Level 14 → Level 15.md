# Objetivo
The password for the next level can be retrieved by submitting the password of the current level to **port 30000 on localhost**.
# Datos de acceso
bandit14
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
# Solución
```
bandit14@bandit:~$ nc localhost 30000
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
Correct!
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt

bandit14@bandit:~$ nmap localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2024-02-19 19:07 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00015s latency).
Not shown: 993 closed ports
PORT      STATE    SERVICE
22/tcp    open     ssh
1111/tcp  open     lmsocialserver
1840/tcp  open     netopia-vo2
4321/tcp  open     rwhois
5120/tcp  filtered barracuda-bbs
8000/tcp  open     http-alt
30000/tcp open     ndmps

Nmap done: 1 IP address (1 host up) scanned in 1.28 seconds
bandit14@bandit:~$ echo "fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq" | nc localhost 30000
Correct!
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt

bandit14@bandit:~$ nc localhost 30000 <<< fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
Correct!
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt

bandit14@bandit:~$ 

```
# Notas
- Al usar el comando nc y los caracteres "<<<" significa que vamos a mandar al puerto lo que está después de los caracteres
# Referencia