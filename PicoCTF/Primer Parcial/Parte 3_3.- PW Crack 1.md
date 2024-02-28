# Objetivo
Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/11/level1.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/11/level1.flag.txt.enc) in the same directory too.

# Solución
```
tonyrguez-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/11/level1.py
--2024-02-28 01:55:13--  https://artifacts.picoctf.net/c/11/level1.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.128, 3.160.22.43, 3.160.22.92, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.128|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 876 [application/octet-stream]
Saving to: 'level1.py'

level1.py                                       100%[=====================================================================================================>]     876  --.-KB/s    in 0s      

2024-02-28 01:55:13 (280 MB/s) - 'level1.py' saved [876/876]

tonyrguez-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/11/level1.flag.txt.enc
--2024-02-28 01:55:20--  https://artifacts.picoctf.net/c/11/level1.flag.txt.enc
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.16, 3.160.22.128, 3.160.22.92, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.16|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 30 [application/octet-stream]
Saving to: 'level1.flag.txt.enc'

level1.flag.txt.enc                             100%[=====================================================================================================>]      30  --.-KB/s    in 0s      

2024-02-28 01:55:20 (1.31 MB/s) - 'level1.flag.txt.enc' saved [30/30]

tonyrguez-picoctf@webshell:~$ nano level1.py
tonyrguez-picoctf@webshell:~$ nano level1.flag.txt.enc
tonyrguez-picoctf@webshell:~$ nano level1.py
tonyrguez-picoctf@webshell:~$ python level1.py
Please enter correct password for flag: 1e1a
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_fa343060}
tonyrguez-picoctf@webshell:~$ 
```

# Notas
- Se usa nano para abrir level1 y ver la contraseña

# Referencias