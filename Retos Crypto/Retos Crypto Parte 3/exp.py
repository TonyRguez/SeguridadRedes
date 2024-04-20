from PIL import Image
import numpy as np

image1 = np.asarray( Image.open('scrambled1.png') )
image2 = np.asarray( Image.open('scrambled2.png') )

datos = image1.copy() + image2.copy()

nueva = Image.fromarray(datos)
nueva.save('nueva.png', 'PNG')
