# Objetivo
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/picopico.key). Recover the flag.

# Solución
```
picoCTF{nongshim.shrimp.crackers}


```
# Notas
- Abrimos la captura de paquetes en wireshark, en edición > preferencias > protocolos > tls agregamos la llave que descargamos para poder desencriptar el tráfico, una vez desencriptado  buscamos la palabra picoCTF para encontrar la bandera en uno de los paquetes.
# Referencia