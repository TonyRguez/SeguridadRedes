# Objetivo
Using netcat (nc) is going to be pretty important. Can you connect to `jupiter.challenges.picoctf.org` at port `25103` to get the flag?
# Solución
```
tonyrguez-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org -p 25103
usage: nc [-46CDdFhklNnrStUuvZz] [-I length] [-i interval] [-M ttl]
          [-m minttl] [-O length] [-P proxy_username] [-p source_port]
          [-q seconds] [-s sourceaddr] [-T keyword] [-V rtable] [-W recvlimit]
          [-w timeout] [-X proxy_protocol] [-x proxy_address[:port]]
          [destination] [port]
tonyrguez-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 25103
You're on your way to becoming the net cat master
picoCTF{nEtCat_Mast3ry_d0c64587}
^C
tonyrguez-picoctf@webshell:~$
```

# Notas
- Se usa nc para conectarse a la dirección y al final se agrega el puerto al que vas a entrar

# Referencias