# Objetivo

# Solución
```
Al abrir el código observamos que nos dan datos clave
username_trial = "FRASER"
bUsername_trial = b"FRASER"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"


Encontramos un código que hace una función sha256 a los caracteres del username para así obtener la bandera

import hashlib
import base64


key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

username_trial = b"FRASER"

potential_dynamic_key = ""

# where our input begins:
offset = 23

# positions in username_trial
positions = [4,5,3,6,2,7,1,8]

for p in positions:
    potential_dynamic_key += hashlib.sha256(username_trial).hexdigest()[p]

key = key_part_static1_trial + potential_dynamic_key + key_part_static2_trial
print(key)
print(len(key))



```
# Notas
- picoCTF{1n_7h3_|<3y_of_ac73dc29}
# Referencia
- https://ctftime.org/writeup/26987