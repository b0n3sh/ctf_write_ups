During your adventure, you will likely encounter a situation where you need to process data that you receive over the network rather than through a file. Can you find a way to save the output from this program and search for the flag? Connect with 2018shell.picoctf.com 37542.

# Solution
---
We just have to use the pipe character on the nc connection to pass it to grep and get our flag.

# Solución
---
Simplemente tenemos que usar pipe para pasar el texto que nos envia el puerto y pasarlo por grep para conseguir la flag.
