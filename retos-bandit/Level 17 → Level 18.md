# Objetivo
There are 2 files in the homedirectory: **passwords.old and passwords.new**. The password for the next level is in **passwords.new** and is the only line that has been changed between **passwords.old and passwords.new**

**NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19**
# Datos de acceso
bandit17
VwOSWtCA7lRKkTfbr2IDh6awj9RNZM5e
# Solución
```
bandit17@bandit:~$ cat /etc/bandit_pass/bandit17
VwOSWtCA7lRKkTfbr2IDh6awj9RNZM5e
bandit17@bandit:~$ ^C
bandit17@bandit:~$ wc -l passwords.old
100 passwords.old
bandit17@bandit:~$ wc -l passwords.new
100 passwords.new
bandit17@bandit:~$ diff passwords.old passwords.new
42c42
< p6ggwdNHncnmCNxuAt0KtKVq185ZU7AW
---
> hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg
```
# Notas
- diff nos sirve para ver los caracteres diferentes entre dos archivos
# Referencia