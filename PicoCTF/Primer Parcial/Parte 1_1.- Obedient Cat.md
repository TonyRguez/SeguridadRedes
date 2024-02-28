# Objetivo
This file has a flag in plain sight (aka "in-the-clear"). [Download flag](https://mercury.picoctf.net/static/0e428b2db9788d31189329bed089ce98/flag).

# Solución
```
tonyrguez-picoctf@webshell:~$ wget https://mercury.picoctf.net/static/0e428b2db9788d31189329bed089ce98/flag
--2024-02-26 18:20:37--  https://mercury.picoctf.net/static/0e428b2db9788d31189329bed089ce98/flag
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 34 [application/octet-stream]
Saving to: 'flag'

flag                100%[==================>]      34  --.-KB/s    in 0s      

2024-02-26 18:20:37 (16.6 MB/s) - 'flag' saved [34/34]

tonyrguez-picoctf@webshell:~$ cat flag
picoCTF{s4n1ty_v3r1f13d_2fd6ed29}
tonyrguez-picoctf@webshell:~$ 
```

# Notas
- wget te permite descargar un archivo en la consola de la página

# Referencias

