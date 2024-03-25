# Objetivo
Now you DON’T see me.This [report](https://artifacts.picoctf.net/c/84/Financial_Report_for_ABC_Labs.pdf) has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?

# Solución
```
┌──(kalicura㉿rufian)-[~/SeguridadRedes/PicoCTF/Segundo Parcial]
└─$ pdftotext Financial_Report_for_ABC_Labs.pdf         
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/PicoCTF/Segundo Parcial]
└─$ ls
'Enhance!.md'                       'Lookey Here.md'           'Wireshark doo dooo do doo....md'   drawing.flag.svg         shark1.pcapng
 Financial_Report_for_ABC_Labs.pdf  'Packets Primer.md'         anthem.flag.txt                    information.md
 Financial_Report_for_ABC_Labs.txt  'Redaction Gone Wrong.md'   cat.jpg                            network-dump.flag.pcap
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/PicoCTF/Segundo Parcial]
└─$ cat Financial_Report_for_ABC_Labs.txt | grep 'pico'
picoCTF{C4n_Y0u_S33_m3_fully}
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/PicoCTF/Segundo Parcial]
└─$ 
```
# Notas
- Descargamos el archivo y usamos pdftotext para convertir el pdf a texto, después usamos cat para ver el contenido y usamos grep para encontrar la bandera.
# Referencia