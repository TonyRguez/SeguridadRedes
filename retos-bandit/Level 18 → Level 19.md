# Objetivo
The password for the next level is stored in a file **readme** in the homedirectory. Unfortunately, someone has modified **.bashrc** to log you out when you log in with SSH.
# Datos de acceso
bandit18
hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg
# Solución
```
└─$ ssh bandit.labs.overthewire.org -p 2220 -l bandit18 /bin/bash
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: 
whoami
bandit18
ls
creadme
cat readme
awhqfNnAbc1naukrpqDYcF95h7HoMTrC
```
# Notas
- Con /bin/bash al final del comando podemos cambiar el bash en el que entramos
# Referencia