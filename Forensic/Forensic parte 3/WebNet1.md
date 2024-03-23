# Objetivo
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/picopico.key). Recover the flag.

# Solución
```
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic/Forensic parte 3]
└─$ strings vulture.jpg -n15
picoCTF{honey.roasted.peanuts}
 )/'%'/9339GDG]]}
 )/'%'/9339GDG]]}
%&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
&'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic/Forensic parte 3]
└─$ 

```
# Notas
- Abrimos la captura de paquetes en wireshark, en edición > preferencias > protocolos > tls agregamos la llave que descargamos para poder desencriptar el tráfico, una vez desencriptado notamos que en el paquete 47 hay una imagen que podemos descargar, al descargarla y haciendo uso del comando strings podemos encontrar la bandera.
# Referencia