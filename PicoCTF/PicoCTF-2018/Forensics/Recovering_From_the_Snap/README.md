There used to be a bunch of [animals](https://2018shell.picoctf.com/static/59cd22a161127c4924bbfdc9f25aa4b8/animals.dd) here, what did Dr. Xernon do to them?

![problem](http://i.imgur.com/a19rDy1.png)

# Solution
Doing a `file` on `animals.dd` we can see that is a DOS/MBR boot sector.
![file](http://i.imgur.com/oUrX0ac.png)
We just do a binwalk and extract every file there's inside, as some of them will be deleted in the drive, so we won't see them if we just mount the .dd.
![binwalk](http://i.imgur.com/WI1tbMs.png)
We get 8 pictures, being one the flag we were looking for.
![pics](http://i.imgur.com/UuxtgnI.png)
![flag](http://i.imgur.com/0xbRpKo.png)

# Solución
Haciendo `file` al archivo que nos hemos bajado `animals.dd` podemos ver que es una partición de disco DOS/MBR.
![file](http://i.imgur.com/oUrX0ac.png)
Simplemente hacemos un binwalk extrayendo todos los posibles archivos borrados en el disco.
![binwalk](http://i.imgur.com/WI1tbMs.png)
Obtenemos 8 imágenes, siendo una la flag que buscábamos.
![pics](http://i.imgur.com/UuxtgnI.png)
![flag](http://i.imgur.com/0xbRpKo.png)

