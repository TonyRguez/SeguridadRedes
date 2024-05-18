# Objetivo
Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.Download the assembly dump [here](https://artifacts.picoctf.net/c/511/disassembler-dump0_d.txt).
# Solución
```
Abrimos el archivo


<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    cmp    DWORD PTR [rbp-0x4],0x2710
<+29>:    jle    0x55555555514e <main+37>
<+31>:    sub    DWORD PTR [rbp-0x4],0x65
<+35>:    jmp    0x555555555152 <main+41>
<+37>:    add    DWORD PTR [rbp-0x4],0x65
<+41>:    mov    eax,DWORD PTR [rbp-0x4]
<+44>:    pop    rbp
<+45>:    ret


<+15>:  Almacenar 0x9fe1a en el puntero de memoria en [rbp-0x4]
<+22>:  Comparar [rbp-0x4] con 0x2710
<+29>:  Saltar a la instrucción en <+37> si [rbp-0x4] es menor o igual a 0x2710 (NO lo es)
<+31>:  Restar 0x65 de [rbp-0x4] y almacenarlo en [rbp-0x4]
<+35>:  Saltar a <+41>
<+37>:  [NO EJECUTADO]
<+41>:  Almacenar el valor señalado por [rbp-0x4] en el registro eax

Después de todos los cálculos y la conversión de hexadecimal, obtenemos el número decimal y nuestra bandera:
picoCTF{654773}
```
# Notas
- picoCTF{654773}
# Referencia