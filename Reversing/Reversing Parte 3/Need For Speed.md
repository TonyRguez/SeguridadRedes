# Objetivo
The name of the game is [speed](https://www.youtube.com/watch?v=8piqd2BWeGI). Are you quick enough to solve this problem and keep it above 50 mph? [need-for-speed](https://jupiter.challenges.picoctf.org/static/27dd5548b14661f65ce3ac6a8a8f575b/need-for-speed).
# Solución
```
Abrimos el programa con GDB y vemos que hay un timer que se acaba muy rápido, por lo que ponemos un break en esa linea y saltamos a la siguiente obteniendo así la bandera
```
# Notas
- PICOCTF{Good job keeping bus #1f2ac4ec speeding along!}
# Referencia