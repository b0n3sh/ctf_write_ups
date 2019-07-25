What does asm0(0x2a,0x4f) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://2018shell.picoctf.com/static/9dd737e97ccbb554569020e205ffa5c8/intro_asm_rev.S) located in the directory at /problems/assembly-0_3_b7d6c21be1cefd3e53335a66e7815307.
![problem](http://i.imgur.com/LRdnjYe.png)

# :uk: Solution :uk: 


---
###### It's an assembly file, where we use 2 parameters, `0x2a & 0x4f`, we have to know 2 things for this exercise:

* `eax` register is always returned.
* The parameters (the 2 values we passed into the assembly) is the first one stored in `ebp+0x8` the second in `ebp+0xc` and so on... (`ebp+0x4` is reserved for the returning value)
---

![code](http://i.imgur.com/HJGs06c.png)

---
###### Carrying on with the code, we can see that the first parameter `ebp+0x8`, is moved to register `eax`.
---

![firstparameter](http://i.imgur.com/OCrFY21.png)

---
###### Now we are moving the second parameter `ebp+0xc` into the register `ebx`.
---

![secondparameter](http://i.imgur.com/5IwtP5E.png)

---
###### At this line, we are moving the `ebx` value into `eax`, thus `eax = ebx`.
---

![equal](http://i.imgur.com/RoSjqAs.png)
 
---
###### Therefore, we now know that the value we are going to get as a value is always `eax`, and also that `eax` will be equal to `ebx`, so we are going to get as value the second parameter we passed into the assembly code.
---

![flag](http://i.imgur.com/TSWEHMN.png)

# :es: Solución :es:


---
###### Es un archivo de ensamblado, donde usamos 2 parámetros, `0x2a & 0x4f`, tenemos que saber 2 cosas para este ejercicio.

* El registro `eax` siempre es devuelto por la función.
* Los parámetros (los 2 valores que han sido pasados al código), el primero es almacenado en `ebp+0x8` y el segundo en `ebp+0xc` y así sucesivamente (`ebp+0x4` está reservado para el returning value).
---

![code](http://i.imgur.com/HJGs06c.png)

---
###### Siguiendo con el código, podemos ver que el primer parámetro `ebp+0x8`, es movido al registro `eax`.
---

![firstparameter](http://i.imgur.com/OCrFY21.png)

---
###### Ahora estamos moviendo el segundo parámetro `ebp+0xc` dentro del registro `ebx`.
---

![secondparameter](http://i.imgur.com/5IwtP5E.png)

---
###### En esta linea, estamos moviendo el valor `ebx` dentro de `eax`, por lo que `eax = ebx`.
---

![equal](http://i.imgur.com/RoSjqAs.png)
 
---
###### Por lo tanto, sabemos que el valor que vamos a recibir como value va a ser siempre `eax`, y como también sabemos que `eax` va a contener el mismo valor que `ebx`, sabemos que el valor que vamos a recibir va a ser el segundo parámetro que pasemos al código.
---

![flag](http://i.imgur.com/TSWEHMN.png)


