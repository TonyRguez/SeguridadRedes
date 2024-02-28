# Objetivo
Run the Python script `code.py` in the same directory as `codebook.txt`.

# Solución
```
tonyrguez-picoctf@webshell:~$ ls
README.txt
tonyrguez-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/1/code.py
--2024-02-28 00:30:19--  https://artifacts.picoctf.net/c/1/code.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.92, 3.160.22.16, 3.160.22.43, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.92|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1278 (1.2K) [application/octet-stream]
Saving to: 'code.py'

code.py                                         100%[=====================================================================================================>]   1.25K  --.-KB/s    in 0s      

2024-02-28 00:30:19 (391 MB/s) - 'code.py' saved [1278/1278]

tonyrguez-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/1/codebook.txt
--2024-02-28 00:30:31--  https://artifacts.picoctf.net/c/1/codebook.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.92, 3.160.22.16, 3.160.22.43, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.92|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 27 [application/octet-stream]
Saving to: 'codebook.txt'

codebook.txt                                    100%[=====================================================================================================>]      27  --.-KB/s    in 0s      

2024-02-28 00:30:31 (547 KB/s) - 'codebook.txt' saved [27/27]

tonyrguez-picoctf@webshell:~$ ls -la
total 36
drwxr-xr-x 3 tonyrguez-picoctf tonyrguez-picoctf  161 Feb 28 00:30 .
drwxr-xr-x 3 root              root                31 Feb 26 18:18 ..
-rw------- 1 tonyrguez-picoctf tonyrguez-picoctf  512 Feb 26 19:12 .bash_history
-rw-r--r-- 1 tonyrguez-picoctf tonyrguez-picoctf  220 Feb 26 18:18 .bash_logout
-rw-r--r-- 1 tonyrguez-picoctf tonyrguez-picoctf 3771 Feb 26 18:18 .bashrc
-rw-r--r-- 1 tonyrguez-picoctf tonyrguez-picoctf  807 Feb 26 18:18 .profile
drwx------ 2 tonyrguez-picoctf tonyrguez-picoctf   48 Feb 26 19:07 .ssh
-rw-rw-r-- 1 tonyrguez-picoctf tonyrguez-picoctf  167 Feb 26 18:20 .wget-hsts
-rw-r--r-- 1 root              root              4443 Feb 28 00:29 README.txt
-rw-rw-r-- 1 tonyrguez-picoctf tonyrguez-picoctf 1278 Mar 16  2023 code.py
-rw-rw-r-- 1 tonyrguez-picoctf tonyrguez-picoctf   27 Mar 16  2023 codebook.txt
tonyrguez-picoctf@webshell:~$ code.py
-bash: code.py: command not found
tonyrguez-picoctf@webshell:~$ python code.py
picoCTF{c0d3b00k_455157_d9aa2df2}
tonyrguez-picoctf@webshell:~$ 
```

# Notas
- Se corre el programa code.py con el comando python

# Referencias