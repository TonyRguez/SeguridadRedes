# Objetivo
Download the packet capture file and use packet analysis software to find the flag.

- [Download packet capture](https://artifacts.picoctf.net/c/196/network-dump.flag.pcap)
# Solución
```
picoCTF{p4ck37_5h4rk_01b0a0d6}
```
# Notas
- Descargamos el archivo, lo abrimos con wireshark y seguimos el stream de TCP, en el stream 0 encontramos la bandera
# Referencia