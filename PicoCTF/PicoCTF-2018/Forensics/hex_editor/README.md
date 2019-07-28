This [cat](https://2018shell.picoctf.com/static/8bf13e0b1ce613af3b79223abb8f8d6d/hex_editor.jpg) has a secret to teach you. You can also find the file in /problems/hex-editor_2_c1a99aee8d919f6e42697662d798f0ff on the shell server.
![problem](http://i.imgur.com/3x0Dj04.png)


# :uk: Solution :uk:
---

---
###### We make a hexdump using `xxd` and we can see that the flag is in the end of the .jpg
---
![hex](http://i.imgur.com/0q9araF.png)


---
###### Now we use strings to get just the printable characters, and clean the output to get the flag in the valid format.
---
![flag](http://i.imgur.com/UPiSYRb.png)

# :es: Solución :es:
---

---
###### Hacemos un hexdump usando `xxd`y vemos que la flag está en el final del .jpg.
---
![hex](http://i.imgur.com/0q9araF.png)


---
###### Ahora usamos `strings` para obtener solamente el texto, y limpiamos el formato para recibir la flag.
---
![flag](http://i.imgur.com/UPiSYRb.png)
