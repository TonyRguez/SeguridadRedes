# Objetivo

Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/f95b1ee9f29d631d99073e34703a2826/warm) has extraordinarily helpful information...
# Solución
```
tonyrguez-picoctf@webshell:~$ wget https://mercury.picoctf.net/static/f95b1ee9f29d631d99073e34703a2826/warm
--2024-02-26 18:28:45--  https://mercury.picoctf.net/static/f95b1ee9f29d631d99073e34703a2826/warm
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 10936 (11K) [application/octet-stream]
Saving to: 'warm.1'

warm.1              100%[==================>]  10.68K  --.-KB/s    in 0s      

2024-02-26 18:28:45 (276 MB/s) - 'warm.1' saved [10936/10936]

tonyrguez-picoctf@webshell:~$ chmod +x warm
tonyrguez-picoctf@webshell:~$ ./warm
Hello user! Pass me a -h to learn what I can do!
tonyrguez-picoctf@webshell:~$ ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_f0668f62}
tonyrguez-picoctf@webshell:~$ 
```

# Notas
- chmod +x. Se usa para asignar permisos de ejecución de un archivo

# Referencias