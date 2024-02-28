# Objetivo
Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/13/level2.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/13/level2.flag.txt.enc) in the same directory too.
# Solución
```
tonyrguez-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/13/level2.py
--2024-02-28 02:04:12--  https://artifacts.picoctf.net/c/13/level2.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.92, 3.160.22.16, 3.160.22.43, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.92|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 914 [application/octet-stream]
Saving to: 'level2.py'

level2.py                                       100%[=====================================================================================================>]     914  --.-KB/s    in 0s      

2024-02-28 02:04:12 (45.1 MB/s) - 'level2.py' saved [914/914]

tonyrguez-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/13/level2.flag.txt.enc
--2024-02-28 02:04:24--  https://artifacts.picoctf.net/c/13/level2.flag.txt.enc
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.92, 3.160.22.16, 3.160.22.43, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.92|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 31 [application/octet-stream]
Saving to: 'level2.flag.txt.enc'

level2.flag.txt.enc                             100%[=====================================================================================================>]      31  --.-KB/s    in 0s      

2024-02-28 02:04:25 (1.32 MB/s) - 'level2.flag.txt.enc' saved [31/31]

tonyrguez-picoctf@webshell:~$ ls
README.txt  level2.flag.txt.enc  level2.py
tonyrguez-picoctf@webshell:~$ nano level2.py
tonyrguez-picoctf@webshell:~$ python level2.py
Please enter correct password for flag: Please enter correct password for flag:
That password is incorrect
tonyrguez-picoctf@webshell:~$ python level2.py
Please enter correct password for flag: de76
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_489dea9a}
tonyrguez-picoctf@webshell:~$ 
```

# Notas
- Se usa cyberchef para decodificar los caracteres en hexadecimal que se encuentran adentro del programa de python

# Referencias