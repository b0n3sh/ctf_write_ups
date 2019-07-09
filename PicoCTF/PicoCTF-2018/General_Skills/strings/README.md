Can you find the flag in this file without actually running it? You can also find the file in /problems/strings_2_b7404a3aee308619cb2ba79677989960 on the shell server.

# Solution
---
It's a binary file, so we have to use strings on it, to get the flag text.

# Solución
---
El archivo está en binario, así que con el comando strings podemos sacarlos bytes printables que necesitamos, en este caso usamos la config por default, que son 4 chars, y luego lo pasamos por grep, sacando la flag.
