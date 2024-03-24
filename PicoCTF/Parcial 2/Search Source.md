# Objetivo

The developer of this website mistakenly left an important artifact in the website source, can you find it?The website is [here](http://saturn.picoctf.net:59405/)
# Solución
```
┌──(kalicura㉿rufian)-[~]

└─$ httrack http://saturn.picoctf.net:59405/

There is an index.html in the directory  but no cache

There is an index.html in the directory, but no cache

A site may have been mirrored here, and erased..

Be sure parameters are ok

  

Press <Y><Enter> to confirm, <N><Enter> to abort

  

Mirror launched on Sun, 24 Mar 2024 16:17:04 by HTTrack Website Copier/3.49-4+libhtsjava.so.2 [XR&CO'2014]

mirroring http://saturn.picoctf.net:59405/ with the wizard help..

Done.: saturn.picoctf.net:59405/images/fevicon.png (153 bytes) - 404

Thanks for using HTTrack!

  
  

┌──(kalicura㉿rufian)-[~]

└─$ cd saturn.picoctf.net_59405

  

┌──(kalicura㉿rufian)-[~/saturn.picoctf.net_59405]

└─$ grep -R pico

css/style.css:/** banner_main picoCTF{1nsp3ti0n_0f_w3bpag3s_8de925a7} **/

index.html:<!-- Mirrored from saturn.picoctf.net:59405/ by HTTrack Website Copier/3.x [XR&CO'2014], Sun, 24 Mar 2024 21:17:06 GMT -->

index.html:<!-- Mirrored from saturn.picoctf.net:59405/ by HTTrack Website Copier/3.x [XR&CO'2014], Sun, 24 Mar 2024 21:17:27 GMT -->

index-2.html:<!-- Mirrored from saturn.picoctf.net:59405/index.html by HTTrack Website Copier/3.x [XR&CO'2014], Sun, 24 Mar 2024 21:17:29 GMT -->

index-2.html:<!-- Mirrored from saturn.picoctf.net:59405/index.html by HTTrack Website Copier/3.x [XR&CO'2014], Sun, 24 Mar 2024 21:17:29 GMT -->

┌──(kalicura㉿rufian)-[~/saturn.picoctf.net_59405]

└─$ 

  
  
  

picoCTF{1nsp3ti0n_0f_w3bpag3s_8de925a7}
```

# Notas
- picoCTF{1nsp3ti0n_0f_w3bpag3s_8de925a7}
- Usamos httrack para clonar la página en nuestra computadora, al usarlo se crea una nueva carpeta, usamos grep en esta nueva carpeta y encontramos la bandera

# Referencias
- https://medium.com/@newan0805/search-source-picoctf-2a50a9dc2820