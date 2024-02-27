# Objetivo
There is a git repository at `ssh://bandit30-git@localhost/home/bandit30-git/repo` via the port `2220`. The password for the user `bandit30-git` is the same as for the user `bandit30`.

Clone the repository and find the password for the next level.
# Datos de acceso
bandit30
xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS
# Solución
```
bandit30@bandit:~$ mkdir /tmp/b30
bandit30@bandit:~$ cd /tmp/b30
bandit30@bandit:/tmp/b30$ git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo 
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit30/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit30/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit30-git@localhost's password: 
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.
bandit30@bandit:/tmp/b30$ cd repo
bandit30@bandit:/tmp/b30/repo$ ls
README.md
bandit30@bandit:/tmp/b30/repo$ cat README.md 
just an epmty file... muahaha
bandit30@bandit:/tmp/b30/repo$ git log
commit d39631d73f786269b895ae9a7b14760cbf40a99f (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Oct 5 06:19:45 2023 +0000

    initial commit of README.md
bandit30@bandit:/tmp/b30/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
bandit30@bandit:/tmp/b30/repo$ bit tag
Command 'bit' not found, did you mean:
  command 'btt' from deb blktrace (1.2.0-5)
  command 'bip' from deb bip (0.9.3-1)
  command 'git' from deb git (1:2.34.1-1ubuntu1.10)
  command 'bti' from deb bti (034-6)
  command 'vit' from deb vit (2.1.0-2)
  command 'wit' from deb wit (3.01a-4)
  command 'bst' from deb buildstream (1.6.1-1)
Try: apt install <deb name>
bandit30@bandit:/tmp/b30/repo$ git tag
secret
bandit30@bandit:/tmp/b30/repo$ git show secret
OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt
bandit30@bandit:/tmp/b30/repo$ 

```
# Notas
# Referencia