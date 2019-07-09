It's never a bad idea to brush up on those linux skills or even learn some new ones before you set off on this adventure! Connect with `nc 2018shell.picoctf.com 58422`.

# Solution
---
We just have to connect to the nc, and follow the instructions they ask us for, which are.
1. Doing ls to list all the folders.
2. Cd'ing to secrets/ folder.
3. Rm'ing everything.
4. Echo'ing 'Drop it in!' for having the exploit installed.
5. Executing it in executables/ folder.
6. Cp'ing /tmp/secrets folder into passwords/ folder.
7. Cat it in 10 seconds, or we will be kicked from the server.

# Solución
---
Simplemente tenemos que conectarnos al nc y de forma interactiva ir cumpliendo una serie de objetivos, en este orden.
1. Hacemos ls para listar todos las carpetas.
2. Hacemos cd a la carpeta secrets/.
3. Borramos todo haciendo rm.
4. Hacemos echo 'Drop it in!' para que se instale en el server el exploit.
5. Ejecutamos el código en la carpeta executables/
6. Copiamos el archivo instalado en /tmp/secrets en la carpeta passwords/.
7. Hacemos cat para ver su contenido antes de que nos tiren del servidor.
