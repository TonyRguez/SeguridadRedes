# Objetivo
Find the flag being held on this server to get ahead of the competition [http://mercury.picoctf.net:34561/](http://mercury.picoctf.net:34561/)
# Solución
```
┌──(kalicura㉿rufian)-[~]
└─$ curl -I head http://mercury.picoctf.net:34561/index.php 
curl: (6) Could not resolve host: head
HTTP/1.1 200 OK
flag: picoCTF{r3j3ct_th3_du4l1ty_8f878508}
Content-type: text/html; charset=UTF-8

```
# Notas
-  Al entrar en la página nos damos cuenta de que los dos botones utilizan métodos post y get, al pasarle un método head en la consola de comandos, se puede obtener la bandera
# Referencia