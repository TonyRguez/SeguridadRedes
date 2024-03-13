# Objetivo
Find the flag in this [picture](https://jupiter.challenges.picoctf.org/static/89b371a46702a31aa9931a2a2b12f8bf/pico_img.png).
# Solución
```
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ wget https://jupiter.challenges.picoctf.org/static/89b371a46702a31aa9931a2a2b12f8bf/pico_img.png
--2024-03-13 00:59:40--  https://jupiter.challenges.picoctf.org/static/89b371a46702a31aa9931a2a2b12f8bf/pico_img.png
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 108795 (106K) [application/octet-stream]
Saving to: ‘pico_img.png’

pico_img.png                              100%[===================================================================================>] 106.25K  --.-KB/s    in 0.1s    

2024-03-13 00:59:40 (786 KB/s) - ‘pico_img.png’ saved [108795/108795]

                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ exiftool pico_img.png 
ExifTool Version Number         : 12.70
File Name                       : pico_img.png
Directory                       : .
File Size                       : 109 kB
File Modification Date/Time     : 2020:10:26 13:38:23-05:00
File Access Date/Time           : 2024:03:13 00:59:40-05:00
File Inode Change Date/Time     : 2024:03:13 00:59:40-05:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 600
Image Height                    : 600
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Software                        : Adobe ImageReady
XMP Toolkit                     : Adobe XMP Core 5.3-c011 66.145661, 2012/02/06-14:56:27
Creator Tool                    : Adobe Photoshop CS6 (Windows)
Instance ID                     : xmp.iid:A5566E73B2B811E8BC7F9A4303DF1F9B
Document ID                     : xmp.did:A5566E74B2B811E8BC7F9A4303DF1F9B
Derived From Instance ID        : xmp.iid:A5566E71B2B811E8BC7F9A4303DF1F9B
Derived From Document ID        : xmp.did:A5566E72B2B811E8BC7F9A4303DF1F9B
Warning                         : [minor] Text/EXIF chunk(s) found after PNG IDAT (may be ignored by some readers)
Artist                          : picoCTF{s0_m3ta_eb36bf44}
Image Size                      : 600x600
Megapixels                      : 0.360
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ exiftool pico_img.png -Artist
Artist                          : picoCTF{s0_m3ta_eb36bf44}
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ 

```
# Notas
- Al usar exiftool en el archivo descargado encontramos los metadatos del mismo, en el nombre del artista encontramos la bandera
# Referencia
