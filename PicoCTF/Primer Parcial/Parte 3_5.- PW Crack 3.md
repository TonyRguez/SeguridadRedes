# Objetivo
Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/17/level3.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/17/level3.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/17/level3.hash.bin) in the same directory too.There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

# Solución
```
tonyrguez-picoctf@webshell:~$ bvi level3.hash.bin

bvi version 1.4.0 Copyright (C) 1996-2014 by Gerhard Buergmann
tonyrguez-picoctf@webshell:~$ python level3.py
Please enter correct password for flag: 87ad
That password is incorrect
tonyrguez-picoctf@webshell:~$ 87ab
-bash: 87ab: command not found
tonyrguez-picoctf@webshell:~$ python level3.py
Please enter correct password for flag: 87ab
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_cd6ed2eb}
tonyrguez-picoctf@webshell:~$ 
```

# Notas
- Se usó https://crackstation.net/ para decifrar el hash del archivo level3.hash.bin, el resultado se pasó al programa de python y se extrajo la flag.

# Referencias