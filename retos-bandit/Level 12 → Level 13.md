# Objetivo
The password for the next level is stored in the file **data.txt**, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)
# Datos de acceso
bandit12
JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv
# Solución
```
bandit12@bandit:~$ mkdir /tmp/37183729
bandit12@bandit:~$ cd /tmp/37183729
bandit12@bandit:/tmp/37183729$ cp ~/data.txt .
bandit12@bandit:/tmp/37183729$ ls
data.txt
bandit12@bandit:/tmp/37183729$ xxd -r data.txt > data
bandit12@bandit:/tmp/37183729$ file data
data: gzip compressed data, was "data2.bin", last modified: Thu Oct  5 06:19:20 2023, max compression, from Unix, original size modulo 2^32 573
bandit12@bandit:/tmp/37183729$ ls
data  data.txt
bandit12@bandit:/tmp/37183729$ rm data.txt
bandit12@bandit:/tmp/37183729$ ls
data
bandit12@bandit:/tmp/37183729$ mv data data.gz
bandit12@bandit:/tmp/37183729$ gzip -d data.gz
bandit12@bandit:/tmp/37183729$ file data
data: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/37183729$ ls
data
bandit12@bandit:/tmp/37183729$ mv data data.bz2
bandit12@bandit:/tmp/37183729$ bzip2 -d data.bz2
bandit12@bandit:/tmp/37183729$ file data
data: gzip compressed data, was "data4.bin", last modified: Thu Oct  5 06:19:20 2023, max compression, from Unix, original size modulo 2^32 20480
bandit12@bandit:/tmp/37183729$ mv data data.gz
bandit12@bandit:/tmp/37183729$ gzip -d data.gz
bandit12@bandit:/tmp/37183729$ file data
data: POSIX tar archive (GNU)
bandit12@bandit:/tmp/37183729$ mv data data.tar
bandit12@bandit:/tmp/37183729$ tar xf data.tar
bandit12@bandit:/tmp/37183729$ rm data.tar
bandit12@bandit:/tmp/37183729$ file data5.bin
data5.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/37183729$ mv data5.bin data5.tar
bandit12@bandit:/tmp/37183729$ tar xf data5.tar
bandit12@bandit:/tmp/37183729$ ls
data5.tar  data6.bin
bandit12@bandit:/tmp/37183729$ rm data5.tar
bandit12@bandit:/tmp/37183729$ file data6.bin
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/37183729$ mv data6.bin data6.bz2
bandit12@bandit:/tmp/37183729$ file data6
data6: cannot open `data6' (No such file or directory)
bandit12@bandit:/tmp/37183729$ ls
data6.bz2
bandit12@bandit:/tmp/37183729$ bzip2 -d data6.bin
bzip2: Can't open input file data6.bin: No such file or directory.
bandit12@bandit:/tmp/37183729$ bzip2 -d data6.bz2
bandit12@bandit:/tmp/37183729$ ls
data6
bandit12@bandit:/tmp/37183729$ file data6
data6: POSIX tar archive (GNU)
bandit12@bandit:/tmp/37183729$ mv data6 data6.tar
bandit12@bandit:/tmp/37183729$ tar xf data6.tar
bandit12@bandit:/tmp/37183729$ ls
data6.tar  data8.bin
bandit12@bandit:/tmp/37183729$ rm data6.tar
bandit12@bandit:/tmp/37183729$ file data8.bin
data8.bin: gzip compressed data, was "data9.bin", last modified: Thu Oct  5 06:19:20 2023, max compression, from Unix, original size modulo 2^32 49
bandit12@bandit:/tmp/37183729$ mv data8.bin data8.gz
bandit12@bandit:/tmp/37183729$ gzip -d data8.gz
bandit12@bandit:/tmp/37183729$ ls
data8
bandit12@bandit:/tmp/37183729$ file data8
data8: ASCII text
bandit12@bandit:/tmp/37183729$ cat data8
The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw
bandit12@bandit:/tmp/37183729$ 

```
# Notas
xxd sirve para hacer un vaciado hexadecimal de un archivo
# Referencia