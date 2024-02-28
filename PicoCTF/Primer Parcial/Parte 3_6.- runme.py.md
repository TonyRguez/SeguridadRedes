# Objetivo

Run the `runme.py` script to get the flag. Download the script with your browser or with `wget` in the webshell.[Download runme.py Python script](https://artifacts.picoctf.net/c/34/runme.py)
# Solución
```
tonyrguez-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/34/runme.py
--2024-02-28 02:44:51--  https://artifacts.picoctf.net/c/34/runme.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.16, 3.160.22.43, 3.160.22.128, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.16|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 270 [application/octet-stream]
Saving to: 'runme.py'

runme.py                                        100%[=====================================================================================================>]     270  --.-KB/s    in 0s      

2024-02-28 02:44:51 (98.1 MB/s) - 'runme.py' saved [270/270]

tonyrguez-picoctf@webshell:~$ python runme.py
picoCTF{run_s4n1ty_run}
tonyrguez-picoctf@webshell:~$ 
```

# Notas
- Se usa wget para bajar el archivo y se corre

# Referencias