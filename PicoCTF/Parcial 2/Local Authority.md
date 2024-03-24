# Objetivo

Can you get the flag?Go to this [website](http://saturn.picoctf.net:49386/) and see what you can discover.
# Solución
```
  

function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
  else
  {
    return false;
  }
}
```

# Notas
-  picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb}
- Al inspeccionar el código de la página vemos que en secure.js está la función que verifica el usuario y contraseña, al poner el mismo usuario y contraseña obtenemos la contraseña.

# Referencias