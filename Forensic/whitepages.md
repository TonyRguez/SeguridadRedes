# Objetivo

# Datos de acceso
# Solución
```
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ wget https://jupiter.challenges.picoctf.org/static/fa4a277cfa846e07a5981d8a19288a2e/whitepages.txt
--2024-03-13 13:27:22--  https://jupiter.challenges.picoctf.org/static/fa4a277cfa846e07a5981d8a19288a2e/whitepages.txt
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2982 (2.9K) [application/octet-stream]
Saving to: ‘whitepages.txt’

whitepages.txt                            100%[===================================================================================>]   2.91K  --.-KB/s    in 0s      

2024-03-13 13:27:22 (56.9 MB/s) - ‘whitepages.txt’ saved [2982/2982]

                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ ls la                                                                                             
ls: cannot access 'la': No such file or directory
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ ls -la            
total 14120
drwxr-xr-x 2 kalicura kalicura     4096 Mar 13 13:27  .
drwxr-xr-x 8 kalicura kalicura     4096 Mar 13 13:09  ..
-rw-r--r-- 1 kalicura kalicura     7018 Mar 12 23:55 'Glory of the Garden.md'
-rw-r--r-- 1 kalicura kalicura     3524 Mar 13 01:13 'So meta.md'
-rw-r--r-- 1 kalicura kalicura   625219 Oct 26  2020  buildings.png
-rw-r--r-- 1 kalicura kalicura   239455 Oct 26  2020  capture.pcap
-rw-r--r-- 1 kalicura kalicura    44514 Mar 13 00:22  extensions.md
-rw-r--r-- 1 kalicura kalicura     9984 Oct 26  2020  flag.png
-rw-r--r-- 1 kalicura kalicura  2295192 Oct 26  2020  garden.jpg
-rw-r--r-- 1 kalicura kalicura    18767 Mar 13 13:25  image.jpg
-rw-r--r-- 1 kalicura kalicura       69 Mar 13 13:10  m00nwalk.md
-rw-r--r-- 1 kalicura kalicura 11066998 Oct 26  2020  message.wav
-rw-r--r-- 1 kalicura kalicura   108795 Oct 26  2020  pico_img.png
-rw-r--r-- 1 kalicura kalicura      458 Mar 13 00:47 'shark on wire 1.md'
-rw-r--r-- 1 kalicura kalicura     1343 Mar 13 01:30 'what lies within.md'
-rw-r--r-- 1 kalicura kalicura     2982 Oct 26  2020  whitepages.txt
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ file whitepages.txt 
whitepages.txt: Unicode text, UTF-8 text, with very long lines (1376), with no line terminators
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$                                   
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ sudo apt install ascii            
[sudo] password for kalicura: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  ascii
0 upgraded, 1 newly installed, 0 to remove and 1219 not upgraded.
Need to get 18.5 kB of archives.
After this operation, 81.9 kB of additional disk space will be used.
Get:1 http://kali.download/kali kali-rolling/main amd64 ascii amd64 3.18-5 [18.5 kB]
Fetched 18.5 kB in 0s (55.0 kB/s)
Selecting previously unselected package ascii.
(Reading database ... 666414 files and directories currently installed.)
Preparing to unpack .../ascii_3.18-5_amd64.deb ...
Unpacking ascii (3.18-5) ...
Setting up ascii (3.18-5) ...
Processing triggers for man-db (2.12.0-3) ...
Processing triggers for kali-menu (2023.4.6) ...
Scanning processes...                                                                                                                                                 
Scanning processor microcode...                                                                                                                                       
Scanning linux images...                                                                                                                                              

Running kernel seems to be up-to-date.

The processor microcode seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ ascii              
Usage: ascii [-adxohv] [-t] [char-alias...]
   -t = one-line output  -a = vertical format
   -d = Decimal table  -o = octal table  -x = hex table  -b binary table
   -h = This help screen -v = version information
Prints all aliases of an ASCII character. Args may be chars, C \-escapes,
English names, ^-escapes, ASCII mnemonics, or numerics in decimal/octal/hex.

Dec Hex    Dec Hex    Dec Hex  Dec Hex  Dec Hex  Dec Hex   Dec Hex   Dec Hex  
  0 00 NUL  16 10 DLE  32 20    48 30 0  64 40 @  80 50 P   96 60 `  112 70 p
  1 01 SOH  17 11 DC1  33 21 !  49 31 1  65 41 A  81 51 Q   97 61 a  113 71 q
  2 02 STX  18 12 DC2  34 22 "  50 32 2  66 42 B  82 52 R   98 62 b  114 72 r
  3 03 ETX  19 13 DC3  35 23 #  51 33 3  67 43 C  83 53 S   99 63 c  115 73 s
  4 04 EOT  20 14 DC4  36 24 $  52 34 4  68 44 D  84 54 T  100 64 d  116 74 t
  5 05 ENQ  21 15 NAK  37 25 %  53 35 5  69 45 E  85 55 U  101 65 e  117 75 u
  6 06 ACK  22 16 SYN  38 26 &  54 36 6  70 46 F  86 56 V  102 66 f  118 76 v
  7 07 BEL  23 17 ETB  39 27 '  55 37 7  71 47 G  87 57 W  103 67 g  119 77 w
  8 08 BS   24 18 CAN  40 28 (  56 38 8  72 48 H  88 58 X  104 68 h  120 78 x
  9 09 HT   25 19 EM   41 29 )  57 39 9  73 49 I  89 59 Y  105 69 i  121 79 y
 10 0A LF   26 1A SUB  42 2A *  58 3A :  74 4A J  90 5A Z  106 6A j  122 7A z
 11 0B VT   27 1B ESC  43 2B +  59 3B ;  75 4B K  91 5B [  107 6B k  123 7B {
 12 0C FF   28 1C FS   44 2C ,  60 3C <  76 4C L  92 5C \  108 6C l  124 7C |
 13 0D CR   29 1D GS   45 2D -  61 3D =  77 4D M  93 5D ]  109 6D m  125 7D }
 14 0E SO   30 1E RS   46 2E .  62 3E >  78 4E N  94 5E ^  110 6E n  126 7E ~
 15 0F SI   31 1F US   47 2F /  63 3F ?  79 4F O  95 5F _  111 6F o  127 7F DEL
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ xxd -l 1000 whitepages.txt 
00000000: e280 83e2 8083 e280 83e2 8083 20e2 8083  ............ ...
00000010: 20e2 8083 e280 83e2 8083 e280 83e2 8083   ...............
00000020: 20e2 8083 e280 8320 e280 83e2 8083 e280   ...... ........
00000030: 83e2 8083 20e2 8083 e280 8320 e280 8320  .... ...... ... 
00000040: 2020 e280 83e2 8083 e280 83e2 8083 e280    ..............
00000050: 8320 20e2 8083 20e2 8083 e280 8320 e280  .  ... ...... ..
00000060: 8320 20e2 8083 e280 83e2 8083 2020 e280  .  .........  ..
00000070: 8320 20e2 8083 2020 2020 e280 8320 e280  .  ...    ... ..
00000080: 83e2 8083 e280 83e2 8083 2020 e280 8320  ..........  ... 
00000090: e280 8320 e280 8320 e280 83e2 8083 e280  ... ... ........
000000a0: 8320 e280 83e2 8083 e280 8320 20e2 8083  . .........  ...
000000b0: e280 83e2 8083 e280 83e2 8083 20e2 8083  ............ ...
000000c0: 20e2 8083 e280 83e2 8083 e280 83e2 8083   ...............
000000d0: 20e2 8083 20e2 8083 e280 83e2 8083 e280   ... ...........
000000e0: 83e2 8083 20e2 8083 e280 8320 e280 83e2  .... ...... ....
000000f0: 8083 e280 83e2 8083 20e2 8083 e280 8320  ........ ...... 
00000100: e280 8320 e280 8320 e280 83e2 8083 2020  ... ... ......  
00000110: e280 8320 e280 83e2 8083 e280 8320 e280  ... ......... ..
00000120: 8320 e280 8320 e280 83e2 8083 e280 8320  . ... ......... 
00000130: e280 8320 e280 83e2 8083 20e2 8083 e280  ... ...... .....
00000140: 83e2 8083 e280 83e2 8083 e280 8320 e280  ............. ..
00000150: 8320 e280 83e2 8083 e280 83e2 8083 e280  . ..............
00000160: 8320 e280 8320 e280 8320 e280 8320 e280  . ... ... ... ..
00000170: 8320 e280 83e2 8083 e280 83e2 8083 20e2  . ............ .
00000180: 8083 e280 8320 e280 83e2 8083 2020 e280  ..... ......  ..
00000190: 83e2 8083 e280 8320 e280 83e2 8083 20e2  ....... ...... .
000001a0: 8083 e280 8320 e280 8320 e280 83e2 8083  ..... ... ......
000001b0: e280 83e2 8083 2020 e280 83e2 8083 20e2  ......  ...... .
000001c0: 8083 e280 83e2 8083 e280 83e2 8083 e280  ................
000001d0: 8320 e280 8320 e280 83e2 8083 20e2 8083  . ... ...... ...
000001e0: e280 8320 e280 83e2 8083 e280 8320 e280  ... ......... ..
000001f0: 8320 e280 8320 e280 83e2 8083 e280 83e2  . ... ..........
00000200: 8083 2020 e280 8320 e280 83e2 8083 2020  ..  ... ......  
00000210: 2020 e280 8320 e280 8320 e280 83e2 8083    ... ... ......
00000220: 20e2 8083 e280 8320 e280 83e2 8083 e280   ...... ........
00000230: 8320 e280 83e2 8083 e280 8320 e280 8320  . ......... ... 
00000240: e280 83e2 8083 2020 e280 83e2 8083 20e2  ......  ...... .
00000250: 8083 e280 83e2 8083 e280 83e2 8083 e280  ................
00000260: 83e2 8083 20e2 8083 e280 8320 20e2 8083  .... ......  ...
00000270: e280 83e2 8083 20e2 8083 e280 83e2 8083  ...... .........
00000280: e280 83e2 8083 e280 8320 e280 83e2 8083  ......... ......
00000290: e280 83e2 8083 20e2 8083 e280 8320 e280  ...... ...... ..
000002a0: 83e2 8083 e280 83e2 8083 e280 8320 e280  ............. ..
000002b0: 8320 e280 83e2 8083 e280 83e2 8083 2020  . ............  
000002c0: e280 8320 e280 83e2 8083 20e2 8083 2020  ... ...... ...  
000002d0: e280 8320 e280 83e2 8083 e280 8320 2020  ... .........   
000002e0: e280 8320 e280 8320 e280 83e2 8083 20e2  ... ... ...... .
000002f0: 8083 e280 8320 e280 83e2 8083 2020 2020  ..... ......    
00000300: e280 8320 e280 8320 e280 8320 e280 8320  ... ... ... ... 
00000310: e280 8320 e280 83e2 8083 2020 20e2 8083  ... ......   ...
00000320: e280 8320 e280 83e2 8083 e280 8320 e280  ... ......... ..
00000330: 83e2 8083 e280 83e2 8083 20e2 8083 e280  .......... .....
00000340: 83e2 8083 e280 83e2 8083 e280 8320 e280  ............. ..
00000350: 8320 e280 83e2 8083 20e2 8083 e280 8320  . ...... ...... 
00000360: e280 83e2 8083 e280 8320 e280 8320 e280  ......... ... ..
00000370: 8320 e280 8320 e280 83e2 8083 e280 83e2  . ... ..........
00000380: 8083 e280 8320 e280 83e2 8083 2020 2020  ..... ......    
00000390: e280 8320 e280 8320 e280 83e2 8083 20e2  ... ... ...... .
000003a0: 8083 e280 8320 e280 8320 e280 8320 e280  ..... ... ... ..
000003b0: 83e2 8083 e280 83e2 8083 e280 83e2 8083  ................
000003c0: 20e2 8083 20e2 8083 e280 83e2 8083 e280   ... ...........
000003d0: 83e2 8083 20e2 8083 e280 8320 e280 83e2  .... ...... ....
000003e0: 8083 e280 83e2 8083                      ........
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ xxd -l 100 -g 1  whitepages.txt
00000000: e2 80 83 e2 80 83 e2 80 83 e2 80 83 20 e2 80 83  ............ ...
00000010: 20 e2 80 83 e2 80 83 e2 80 83 e2 80 83 e2 80 83   ...............
00000020: 20 e2 80 83 e2 80 83 20 e2 80 83 e2 80 83 e2 80   ...... ........
00000030: 83 e2 80 83 20 e2 80 83 e2 80 83 20 e2 80 83 20  .... ...... ... 
00000040: 20 20 e2 80 83 e2 80 83 e2 80 83 e2 80 83 e2 80    ..............
00000050: 83 20 20 e2 80 83 20 e2 80 83 e2 80 83 20 e2 80  .  ... ...... ..
00000060: 83 20 20 e2                                      .  .
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$ sed 's/\xe2\x80\x83/0/g' whitepages.txt | sed 's/\x20/1/g'               
00001010000010010000100101110000011010010110001101101111010000110101010001000110000010100000101000001001000010010101001101000101010001010010000001010000010101010100001001001100010010010100001100100000010100100100010101000011010011110101001001000100010100110010000000100110001000000100001001000001010000110100101101000111010100100100111101010101010011100100010000100000010100100100010101010000010011110101001001010100000010100000100100001001001101010011000000110000001100000010000001000110011011110111001001100010011001010111001100100000010000010111011001100101001011000010000001010000011010010111010001110100011100110110001001110101011100100110011101101000001011000010000001010000010000010010000000110001001101010011001000110001001100110000101000001001000010010111000001101001011000110110111101000011010101000100011001111011011011100110111101110100010111110110000101101100011011000101111101110011011100000110000101100011011001010111001101011111011000010111001001100101010111110110001101110010011001010110000101110100011001010110010001011111011001010111000101110101011000010110110001011111001100110110010100110010001101000011001000110011001100000011100000110001011001000110011000111001011000010110010001100001011000100011001001100001001110010110010000111001001101100110000101100110011001000110000100110100011000110110011001100001011001000011011001111101000010100000100100001001                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/SeguridadRedes/Forensic]
└─$


--METEMOS EN CYBERCHEF--


		picoCTF

		SEE PUBLIC RECORDS & BACKGROUND REPORT
		5000 Forbes Ave, Pittsburgh, PA 15213
		picoCTF{not_all_spaces_are_created_equal_3e2423081df9adab2a9d96afda4cfad6}
		
```
# Notas
- Al abrir el programa en hexeditor nos damos cuenta de que el archivo consiste de espacios en blanco, los primeros representados como e28083 y los otros como 20, usamos un comando para cambiar los primeros por 0 y los otros por 1, metemos el resultado en cyberchef de binario y nos da la contraseña
- picoCTF{not_all_spaces_are_created_equal_3e2423081df9adab2a9d96afda4cfad6}
# Referencia