# Objetivo
I have these 2 images, can you make a flag out of them? [scrambled1.png](https://mercury.picoctf.net/static/e8054e22552c6aba591cdf7440eb25e4/scrambled1.png) [scrambled2.png](https://mercury.picoctf.net/static/e8054e22552c6aba591cdf7440eb25e4/scrambled2.png)
# Solución
```
Hacemos el siguiente código en python para transformar las imágenes en matrices y hacer un and lógico, al resultado lo guardamos en otra imagen la cuál contiene la bandera

from PIL import Image
import numpy as np

image1 = np.asarray( Image.open('scrambled1.png') )
image2 = np.asarray( Image.open('scrambled2.png') )

datos = image1.copy() + image2.copy()

nueva = Image.fromarray(datos)
nueva.save('nueva.png', 'PNG')



```
# Notas
- picoCTF{d72ea4af}
# Referencia
