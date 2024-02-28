# Objetivo

There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 21135`, but it doesn't speak English...
# Solución
```
tonyrguez-picoctf@webshell:~$ nc mercury.picoctf.net 21135
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
97 
102 
100 
53 
102 
100 
97 
52 
125 
10 
picoCTF{g00d_k1tty!_n1c3_k1tty!_afd5fda4}
```

# Notas
- Se usó cyberchef con el decodificador de "to charcode" en base 10 para decifrar el mensaje

# Referencias
- https://gchq.github.io/CyberChef/#recipe=From_Charcode('Space',10)&input=MTEyIA0KMTA1IA0KOTkgDQoxMTEgDQo2NyANCjg0IA0KNzAgDQoxMjMgDQoxMDMgDQo0OCANCjQ4IA0KMTAwIA0KOTUgDQoxMDcgDQo0OSANCjExNiANCjExNiANCjEyMSANCjMzIA0KOTUgDQoxMTAgDQo0OSANCjk5IA0KNTEgDQo5NSANCjEwNyANCjQ5IA0KMTE2IA0KMTE2IA0KMTIxIA0KMzMgDQo5NSANCjk3IA0KMTAyIA0KMTAwIA0KNTMgDQoxMDIgDQoxMDAgDQo5NyANCjUyIA0KMTI1IA0KMTA