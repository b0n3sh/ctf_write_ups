What does asm1(0x15e) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://2018shell.picoctf.com/static/7a387091ddf97208739cd0a1e8a2a393/eq_asm_rev.S) located in the directory at /problems/assembly-1_3_cfc4373d0e723e491f368e7bcc26920a.

![problem](http://i.imgur.com/lFL4JN7.png)


# :uk: Solution :uk:

---
###### Just another assembly challenge, we are using vim and python to solve it,as we need to calculate some hex operations. As always, we know that the input value (`0x15`) equals to `[ebp+0x8]` and that at the end of the function, we are always going to get `eax` variable.
---
![](http://i.imgur.com/Fk10l3M.png)

---
###### We start at `asm1`, after the typical `push ebp`and `mov ebp,esp`, we have a comparison operand, where we will jump if `[ebp+0x8]` > `0xdc`. As it is `True`, we jump to `part_a`.
---
![](http://i.imgur.com/TjbIRrM.png)

---
###### Now, at `part_a`, we compare `[ebp+0x8] != 0x68`, as this is `True` (0x15e is not equal to 0x68) we jump to part_c.
---
![](http://i.imgur.com/Coo4EF0.png)

---
###### Now we assign to the variable `eax`, the value `[ebp+0x8]` which is `0x15e` and add `0x3` to `eax`, which is `0x15e + 0x3 = 0x161`.
---
![](http://i.imgur.com/LvTdKz7.png)

---
###### Finally, we just continue to `part_d`, where the function is finished, and we return the value `eax` which is `0x161`, our flag.
---

# :es: Solución :es:

---
###### Simplemente otro desafío de ensamblador, usaremos Vim y Python para resolvero, ya que necesitamos calcular algunas operaciones en hexadecimal. Como siempre, sabemos que el valor que hemos metido en la función (`0x15`) equivale a `[ebp+0x8]` y que al final de la función, el valor que vamos a recibir es el de la variable `eax`.
---
![](http://i.imgur.com/Fk10l3M.png)

---
###### Empezamos en `asm1`, después del típico `push ebp`y `mov ebp,esp`, tenemos un comparador, donde saltaremos a `part_a`si `[ebp+0x8` > `0xdc`. Como es `True`, saltamos a `part_a`.
---
![](http://i.imgur.com/TjbIRrM.png)

---
###### Ahora, en `part_a`, comparamos `[ebp+0x8 != 0x68`, como es `True` (0x15e no es igual a 0x68) saltamos a `part_c`.
---
![](http://i.imgur.com/Coo4EF0.png)

---
###### Ahora asignamos a la variable `eax`, el valor `[ebp+0x8]` el cual es `0x15e`y añadimos `0x3`a `eax`, el cual es `0x15e + 0x3 = 0x161`.
---
![](http://i.imgur.com/LvTdKz7.png)

---
###### Finalmente, simplemente continuamos a `part_d`, donde la función se termina, y nos devuelve el valor de `eax`, el cual es `0x161`, nuestra flag.
---
