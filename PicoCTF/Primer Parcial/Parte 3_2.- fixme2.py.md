# Objetivo
Fix the syntax error in the Python script to print the flag.[Download Python script](https://artifacts.picoctf.net/c/5/fixme2.py)

# Solución
```
tonyrguez-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/5/fixme2.py
--2024-02-28 01:22:10--  https://artifacts.picoctf.net/c/5/fixme2.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.128, 3.160.22.92, 3.160.22.16, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.128|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1029 (1.0K) [application/octet-stream]
Saving to: 'fixme2.py'

fixme2.py                                       100%[=====================================================================================================>]   1.00K  --.-KB/s    in 0s      

2024-02-28 01:22:10 (405 MB/s) - 'fixme2.py' saved [1029/1029]

tonyrguez-picoctf@webshell:~$ nano /home/tonyrguez-picoctf/fixme2.py
tonyrguez-picoctf@webshell:~$ python fixme2.py
  File "/home/tonyrguez-picoctf/fixme2.py", line 22
    if flag = "":
       ^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
tonyrguez-picoctf@webshell:~$ nano /home/tonyrguez-picoctf/fixme2.py
tonyrguez-picoctf@webshell:~$ python fixme2.py
That is correct! Here's your flag: 
tonyrguez-picoctf@webshell:~$ nano /home/tonyrguez-picoctf/fixme2.py
tonyrguez-picoctf@webshell:~$ python fixme2.py
That is correct! Here's your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_4863e11b}
tonyrguez-picoctf@webshell:~$ 
```

# Notas
- Se usó nano para editar el archivo de python

# Referencias