# Objetivo
Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings) without running it?

# Solución
```
tonyrguez-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings
--2024-02-28 01:15:24--  https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 776032 (758K) [application/octet-stream]
Saving to: 'strings'

strings                                         100%[=====================================================================================================>] 757.84K  1.82MB/s    in 0.4s    

2024-02-28 01:15:25 (1.82 MB/s) - 'strings' saved [776032/776032]

tonyrguez-picoctf@webshell:~$ strings strings | grep pico
picoCTF{5tRIng5_1T_d66c7bb7}
tonyrguez-picoctf@webshell:~$ 
```

# Notas
-  Se usa strings para ver el contenido del archivo y se usa grep para filtrar y encontrar la cadena

# Referencias