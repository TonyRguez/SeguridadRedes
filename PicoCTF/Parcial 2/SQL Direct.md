# Objetivo
Connect to this PostgreSQL server and find the flag!`psql -h saturn.picoctf.net -p 62568 -U postgres pico`Password is `postgres`
# Solución
```
**

┌──(kalicura㉿rufian)-[~]

└─$ psql -h saturn.picoctf.net -p 62568 -U postgres pico

Password for user postgres: 

psql (16.1 (Debian 16.1-1), server 15.2 (Debian 15.2-1.pgdg110+1))

Type "help" for help.

  

pico=# /dt

pico-# \dt

         List of relations

 Schema | Name  | Type  |  Owner   

--------+-------+-------+----------

 public | flags | table | postgres

(1 row)

  

pico=# select * from public.flags;

 id | firstname | lastname  |                address                 

----+-----------+-----------+----------------------------------------

  1 | Luke      | Skywalker | picoCTF{L3arN_S0m3_5qL_t0d4Y_31fd14c0}

  2 | Leia      | Organa    | Alderaan

  3 | Han       | Solo      | Corellia

(3 rows)

  
**
```

# Notas
- Al ingresar al servidor usamos \dt para ver a cuales tablas tenemos acceso, después usamos la sentencia select * from public.flags; para ver el contenido de la tabla y obtenemos la bandera.

# Referencias