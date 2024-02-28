# Objetivo
Fix the syntax error in this Python script to print the flag.[Download Python script](https://artifacts.picoctf.net/c/26/fixme1.py)
# Solución
```
tonyrguez-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/26/fixme1.py
--2024-02-28 01:05:28--  https://artifacts.picoctf.net/c/26/fixme1.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.43, 3.160.22.128, 3.160.22.16, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.43|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 837 [application/octet-stream]
Saving to: 'fixme1.py'

fixme1.py                                       100%[=====================================================================================================>]     837  --.-KB/s    in 0s      

2024-02-28 01:05:28 (285 MB/s) - 'fixme1.py' saved [837/837]

tonyrguez-picoctf@webshell:~$ nano /home/tonyrguez-picoctf/fixme1.py
tonyrguez-picoctf@webshell:~$ python fixme1.py 
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_09ee727a}
tonyrguez-picoctf@webshell:~$ ^C
tonyrguez-picoctf@webshell:~$ 
```

# Notas
- Se usa nano para editar el archivo desde la consola

# Referencias