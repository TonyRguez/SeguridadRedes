# Objetivo
The password for the next level can be retrieved by submitting the password of the current level to **port 30001 on localhost** using SSL encryption.

**Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…**
# Datos de acceso
bandit15
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
# Solución
```
bandit15@bandit:~$ openssl s_client -connect localhost:30001
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = localhost
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = localhost
verify error:num=10:certificate has expired
notAfter=Feb 18 10:54:16 2024 GMT
verify return:1
depth=0 CN = localhost
notAfter=Feb 18 10:54:16 2024 GMT
verify return:1
---
Certificate chain
 0 s:CN = localhost
   i:CN = localhost
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA1
   v:NotBefore: Feb 18 10:53:16 2024 GMT; NotAfter: Feb 18 10:54:16 2024 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDCzCCAfOgAwIBAgIEcjY6OTANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjQwMjE4MTA1MzE2WhcNMjQwMjE4MTA1NDE2WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCz
TX1NLedZhpQfXiWbWWD2BlNYjANpj+TnzUOI9ZbKJnOQJAbFfWZLA6No7XOStgje
+RPIoAHrX42G95VDfWtRms+qCsCTlUaS9291dZJQ3iOjBIE+PvmRcGdUlFJXDYa6
E61L2DKLbb8YSAnSuUPG3K7CtdxJpA5DpCBCmHEA9t5gZ5HGo9Gt9Kay9lhApX78
ocytwwHG15LplXI6LQB3ykhyCAcfljR3azd90T83dz7kLyM7yIMt60k1kemuX6RW
qSvkCvxmckRFoQPjwKZUopGLlhcC58Kb2xlwEGK+9j/ibBRkmEdBkOOeb5pJol7K
Wkd9LdG0nTWrggni7EKbAgMBAAGjZTBjMBQGA1UdEQQNMAuCCWxvY2FsaG9zdDBL
BglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0ZWQgYnkgTmNhdC4g
U2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3DQEBBQUAA4IBAQCA
j53OECoyjZMkHINZj35xk2kKQc9Jj9XjoCE0HlooUWd1ETik/2TkIbdWenozDrgH
10Jqmu/zAEhQkfFALBXCR7Vo0319yvR3rlnC2TdzMeBeUQ/n6ivPsCCL6SF8UTWT
XZJoTEfmp+Ma4zup/mEs23uO/FQ0J3LmSgICtXzPCA09M/ffj2UgTENdTHDltQxl
nQpzF+U40+bg/2PQ83XOTQJbZVbU2FnP/MitSYycxemLJXzbdsIxQhQy0VmTY73E
ZFemHVTbzEzcsCJRak4AyPZ9Zpi2uozHA8r1PqtnDzsN5FBFwuJxCuc+F8QeHh9e
QoyfsotkA6BO0LBqWNvE
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
    Session-ID: DAD7A08A7213B3A9DB81C424DDC208ADC5B02BC289F8E07964F6C06EA5AA1FDF
    Session-ID-ctx: 
    Resumption PSK: DE4CE78DDB2BA3C245BD8A7386F17ACA8A4466589CC66DD239C79B286E9DC8484CDEBBA713D5C753FA7D088633BD7EEA
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - dc 1b 67 7e 6b 49 ec f9-e1 0a 8a 6e cb ac b4 e6   ..g~kI.....n....
    0010 - a3 cc a7 17 50 05 4c 7b-df 33 e7 87 69 f0 be 60   ....P.L{.3..i..`
    0020 - 63 14 cf 77 31 18 62 b2-f4 e2 5e 23 a2 5b 7b 17   c..w1.b...^#.[{.
    0030 - 40 1a fd 29 1f 89 b7 7e-7b 02 d3 54 92 64 de e8   @..)...~{..T.d..
    0040 - 65 f7 07 b5 af ae 9f a7-3d d2 0a 62 de 19 dc 4c   e.......=..b...L
    0050 - 7a 0a 23 b3 f4 ba 74 bb-1d c1 c0 b7 30 23 bb 22   z.#...t.....0#."
    0060 - 11 eb 5a d6 23 3c a0 98-ce bb 66 11 9b 7c aa a7   ..Z.#<....f..|..
    0070 - cd 37 de 3b c5 e3 45 1d-7b 80 59 05 d3 d1 44 90   .7.;..E.{.Y...D.
    0080 - 1c d5 0c 67 a4 35 2f ed-c2 a9 1d 3a 28 b1 8c 78   ...g.5/....:(..x
    0090 - 63 fa 61 9b 67 ea aa d7-e3 eb a2 f0 3e e6 3e d8   c.a.g.......>.>.
    00a0 - 75 6a 71 f9 c1 e8 25 03-8f 42 ec 93 8f c0 76 70   ujq...%..B....vp
    00b0 - 97 dc ca 04 1b 8e 6b bb-98 93 52 28 6d e0 97 7f   ......k...R(m...
    00c0 - e3 a2 60 cc cc a1 63 af-58 02 6b 30 35 58 24 f2   ..`...c.X.k05X$.

    Start Time: 1708370552
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
    Session-ID: 3495A50AC68ED0A74B3A611E560508B71DE7EA3C2F5F05E954890EE7D4F41F51
    Session-ID-ctx: 
    Resumption PSK: E91B5FB051E931613F604FD15C0A1553236982D7B1FEB03CBF7183BB4C94B452B7981CE650CB30EFFC3F24AB95B6D005
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - dc 1b 67 7e 6b 49 ec f9-e1 0a 8a 6e cb ac b4 e6   ..g~kI.....n....
    0010 - 72 ae 9f 16 8e f5 6e 43-39 81 b1 5e e4 73 9b 04   r.....nC9..^.s..
    0020 - 74 72 19 87 b3 95 1a d7-a6 e8 dc d5 a7 36 a4 0d   tr...........6..
    0030 - c6 fd 8f bf 78 0b 32 29-9d ea a7 45 44 bd ba 10   ....x.2)...ED...
    0040 - 01 00 f1 6a 29 05 95 cc-f1 b3 6a f5 c3 71 11 71   ...j).....j..q.q
    0050 - 90 d9 cb 8e 53 1e 20 90-0e 7b 57 7b 3d df 69 68   ....S. ..{W{=.ih
    0060 - 3e eb 89 a0 61 4c 5c 10-24 fc 74 34 80 1f 1c d2   >...aL\.$.t4....
    0070 - 73 29 ad a8 d7 c2 eb 7c-72 a3 d7 90 76 19 4a 8e   s).....|r...v.J.
    0080 - e2 64 0f 50 90 c0 12 ce-4f 7c f9 5b 37 4d b7 38   .d.P....O|.[7M.8
    0090 - 61 ab 93 10 40 a7 e0 b5-77 42 b7 f9 c4 69 49 da   a...@...wB...iI.
    00a0 - 04 ed 9b f7 fa 8e 56 eb-2f f6 87 51 06 39 bb a3   ......V./..Q.9..
    00b0 - e1 db fb 69 61 32 c9 43-0d 2f 87 a7 57 ce a5 8c   ...ia2.C./..W...
    00c0 - 59 93 d8 27 7a 1c 09 eb-d6 ef 2f 30 f3 b0 b5 30   Y..'z...../0...0

    Start Time: 1708370552
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
Correct!
JQttfApK4SeyHwDlI9SXGR50qclOAil1

closed
bandit15@bandit:~$ 

```
# Notas
# Referencia