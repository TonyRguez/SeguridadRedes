# Objetivo
Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/e5825f58ef798fdd1af3f6013592a971/cat.jpg)
# Solución
```
┌──(kalicura㉿rufian)-[~/SeguridadRedes/PicoCTF/Segundo Parcial]
└─$ exiftool cat.jpg          
ExifTool Version Number         : 12.70
File Name                       : cat.jpg
Directory                       : .
File Size                       : 878 kB
File Modification Date/Time     : 2021:03:15 13:24:46-05:00
File Access Date/Time           : 2024:03:24 18:20:51-05:00
File Inode Change Date/Time     : 2024:03:24 18:20:50-05:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1

picoCTF{the_m3tadata_1s_modified}
```
# Notas
- Al descargar la imagen y ver sus metadatos, vemos que en la licencia encontramos una cadena en base 64, al meterla a cyberchef obtenemos la cadena
# Referencia