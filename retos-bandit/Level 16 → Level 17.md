# Objetivo
The credentials for the next level can be retrieved by submitting the password of the current level to **a port on localhost in the range 31000 to 32000**. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.
# Datos de acceso
bandit16
JQttfApK4SeyHwDlI9SXGR50qclOAil1
# Solución
```
bandit16@bandit:~$ nmap 127.0.0.1
Starting Nmap 7.80 ( https://nmap.org ) at 2024-02-21 18:09 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00015s latency).
Not shown: 994 closed ports
PORT      STATE SERVICE
22/tcp    open  ssh
1111/tcp  open  lmsocialserver
1840/tcp  open  netopia-vo2
4321/tcp  open  rwhois
8000/tcp  open  http-alt
30000/tcp open  ndmps

Nmap done: 1 IP address (1 host up) scanned in 0.07 seconds
bandit16@bandit:~$ nmap 127.0.0.1 -p 31000-32000
Starting Nmap 7.80 ( https://nmap.org ) at 2024-02-21 18:10 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00010s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.05 seconds
bandit16@bandit:~$ which nmap
/usr/bin/nmap
bandit16@bandit:~$ which nc
/usr/bin/nc
bandit16@bandit:~$ nc -vz localhost 31000-32000 2>&1 | grep succ
Connection to localhost (127.0.0.1) 31046 port [tcp/*] succeeded!
Connection to localhost (127.0.0.1) 31518 port [tcp/*] succeeded!
Connection to localhost (127.0.0.1) 31691 port [tcp/*] succeeded!
Connection to localhost (127.0.0.1) 31790 port [tcp/*] succeeded!
Connection to localhost (127.0.0.1) 31960 port [tcp/*] succeeded!
bandit16@bandit:~$ openssl s_client -connect localhost:31190
80DBF0F7FF7F0000:error:8000006F:system library:BIO_connect:Connection refused:../crypto/bio/bio_sock2.c:125:calling connect()
80DBF0F7FF7F0000:error:10000067:BIO routines:BIO_connect:connect error:../crypto/bio/bio_sock2.c:127:
connect:errno=111
bandit16@bandit:~$ openssl s_client -connect localhost:31790
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = localhost
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = localhost
verify error:num=10:certificate has expired
notAfter=Feb 20 17:51:06 2024 GMT
verify return:1
depth=0 CN = localhost
notAfter=Feb 20 17:51:06 2024 GMT
verify return:1
---
Certificate chain
 0 s:CN = localhost
   i:CN = localhost
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA1
   v:NotBefore: Feb 20 17:50:06 2024 GMT; NotAfter: Feb 20 17:51:06 2024 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDCzCCAfOgAwIBAgIEQ9wEgDANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjQwMjIwMTc1MDA2WhcNMjQwMjIwMTc1MTA2WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDA
gdd50zQdwKnADuCYAoUSFvGreD2Mr/e6QZK+31XsKXCd/+cGHdmkqerggVlwno8T
3lmAaRw+Pk/nNdn3xJEGGq5guV2YhAnT+IQgP6+76ii/4gUCQxnaTtmslJDSfv7i
km+qYsFRL1YdtOo5od2etkLdorXGqGcIrB6ilCgKgQ2Q7FqMjh7n37HPk8yaWCwX
M/JZ7jkXw4mf2Un9UILgo/oJfR0JhMq6cDkHztG0E6j5ruknDeeOMGimH9pmzaa9
xdJe1GTtk+v03FIng0IfHi0HVPUCN8dl9rKLzn/LKZ3UftyffIErE7nDCLaGpVBK
DQzkq5gMPShGa1RT7nkFAgMBAAGjZTBjMBQGA1UdEQQNMAuCCWxvY2FsaG9zdDBL
BglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0ZWQgYnkgTmNhdC4g
U2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3DQEBBQUAA4IBAQBh
XmVUELbEPhoHaMrhwHyd24bRzYiiOemi75OA6QywOLh7moC8MGKvtI0mHhhA+lfB
eEvOOPwL5om4culG+KnC24fdWzwX/PPtkYKocNSrIQINrVhTwBbGwnC+WCSYizZS
43Zav+szrJ6H66qO4x4wXU9p1qC24dIpY5dfBsy4m8P/XzUtg68YJng1EIuGM6DF
CnMWXUB0cfUgBsbWPMrQlJd5sHifKeglK3kBCXn3zb9T881YbLNAwMK2a5SnPdh8
eTg1e7pdNYwPvHcxYPySGyQCkLpLHduWUxVNrUfsVHrxI6rrHynZ5vv4+ulAmhAc
YoU33/wx/D1oycw1GLHh
-----END CERTIFICATE-----
subject=CN = localhost
issuer=CN = localhost
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1339 bytes and written 373 bytes
Verification error: certificate has expired
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 2048 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 10 (certificate has expired)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: E7AB112141B25B71BD57E7ABF316158992118399DB575850F4A5A1E081E83766
    Session-ID-ctx: 
    Resumption PSK: 02AE0D45DFCE53A5DDF5372EE9EB65EACCED09B572F322568F22442C0084BFA180978B6D0B606ED81E34477ED7E6B0EA
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 92 ed 0d d5 75 f9 0c 95-ed 08 73 73 af f3 6c c3   ....u.....ss..l.
    0010 - 89 d3 a2 5b e1 dd bc 4e-a7 c6 31 b5 a7 d5 67 85   ...[...N..1...g.
    0020 - e0 1e 94 52 69 d5 0a fe-ff 80 a4 d7 e4 03 3c 53   ...Ri.........<S
    0030 - 68 fd 0e 56 e7 13 c9 09-b9 bc 56 07 73 ae 8f 30   h..V......V.s..0
    0040 - 5c 3d db 3c 3d 31 9b cf-42 98 e3 16 e8 b9 53 cb   \=.<=1..B.....S.
    0050 - 09 fb d2 94 08 15 c2 6f-8f 85 57 af a3 51 5d e1   .......o..W..Q].
    0060 - 52 aa 3a e3 09 c5 b2 2f-1b a8 43 bb a4 db 4d 61   R.:..../..C...Ma
    0070 - 54 08 81 ab 7e f1 66 fa-6f c9 4f b5 a2 8a e0 72   T...~.f.o.O....r
    0080 - ab cc 53 b7 70 10 2f 57-ec c9 66 ba bf d8 fd ba   ..S.p./W..f.....
    0090 - 25 bc 46 da 28 d2 11 56-8f e6 81 fb 8d 05 0c a2   %.F.(..V........
    00a0 - 6e 74 7f 4b 7c 76 ae 9e-d5 8d fb a4 0d bf 1e 3f   nt.K|v.........?
    00b0 - e6 3a f3 6d dc 81 a1 1a-f3 78 af a7 64 c8 56 1e   .:.m.....x..d.V.
    00c0 - f7 9d fb 27 b3 54 7d 9a-21 e4 d2 a2 8a 31 ce d2   ...'.T}.!....1..

    Start Time: 1708539497
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 79E552DC35FC45A6B6B73567697B51C4AA9A41B1865FED4DDCD34E7B054E8F99
    Session-ID-ctx: 
    Resumption PSK: 173B2266DB1F528C716687C36C6D974BBDC97D5C0181374EA2557D383E5BB9040684F489CA2ADC08F07E3C196676A764
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 92 ed 0d d5 75 f9 0c 95-ed 08 73 73 af f3 6c c3   ....u.....ss..l.
    0010 - 35 f2 d1 94 cd 03 e3 88-e4 8e 8d 27 26 d7 29 5e   5..........'&.)^
    0020 - 44 c4 e3 46 30 b0 ed f7-b4 e0 2e 22 f9 c1 e1 c4   D..F0......"....
    0030 - 54 7c 41 03 d9 fd c4 c9-68 54 67 2b ee a9 df 8b   T|A.....hTg+....
    0040 - 5e e9 ef 31 51 5f 44 58-48 61 20 5d c2 c4 be 39   ^..1Q_DXHa ]...9
    0050 - 8f 92 77 3f cb 2d 88 ff-46 da a0 cd 50 0f 22 f5   ..w?.-..F...P.".
    0060 - 51 aa e8 06 9a 7b a5 48-a2 61 b6 36 76 96 31 d1   Q....{.H.a.6v.1.
    0070 - 44 fa 38 56 f5 2b b4 7e-d4 b3 98 82 e3 2c 2b b6   D.8V.+.~.....,+.
    0080 - 71 3e a0 9e a3 ed 34 9d-6f 85 e2 97 de 1e d4 43   q>....4.o......C
    0090 - 0a aa 00 05 2f 49 20 8c-6e 08 3a 67 04 18 a3 95   ..../I .n.:g....
    00a0 - ad d5 de fe 70 87 bc 5c-6b c7 45 eb 8c 9a 5c f4   ....p..\k.E...\.
    00b0 - 12 24 cb 21 5a 21 d8 fe-ac 15 2f 95 9d b2 7a e0   .$.!Z!..../...z.
    00c0 - 8e 36 7b 88 81 16 08 b2-e4 74 b8 a6 7e 36 36 ff   .6{......t..~66.

    Start Time: 1708539497
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
JQttfApK4SeyHwDlI9SXGR50qclOAil1
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

closed

┌──(kalicura㉿rufian)-[~/Desktop/SeguridadRedes]
└─$ chmod 600 lallavenuda
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~/Desktop/SeguridadRedes]
└─$ ls -la lallavenuda
-rw------- 1 kalicura kalicura 1675 Feb 21 12:20 lallavenuda

┌──(kalicura㉿rufian)-[~/Desktop/SeguridadRedes]
└─$ ssh -i lallavenuda bandit17@bandit.labs.overthewire.org -p 2220

bandit17@bandit:~$ cat /etc/bandit_pass/bandit17
VwOSWtCA7lRKkTfbr2IDh6awj9RNZM5e

```
# Notas
- 2>&1 sirve para mandar los mensajes de error a la salida estandar para filtrar los mensajes de la consola
- nmap nos sirve para ver qué puertos están abiertos, de manera predeterminada escanea los primeros 30000 puertos pero podemos dar un rango en específico que queramos
# Referencia