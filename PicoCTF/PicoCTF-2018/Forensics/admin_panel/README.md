We captured some [traffic](https://2018shell.picoctf.com/static/ee6ed2afe1da153ae06e61d5ee26d52d/data.pcap) logging into the admin panel, can you find the password?
![problem](http://i.imgur.com/bRpozua.png)


# :uk: Solution :uk:


---
###### We can see that it is a TCP/IP packed data capture, so we are using Wireshark to open it.
---

![file](http://i.imgur.com/mJGz29a.png)

---
###### Now we see that it is some HTTP unencrypted communication with some POST /loging requests on it.
---

![wire](http://i.imgur.com/yrH2rvv.png)

---
###### We just filter to get the POST data and we can see that the password is in plaintext data, and it's the flag for the challenge.
---

![hex](http://i.imgur.com/OrTMf1E.png)

---
###### There's a little shortcut, as we know that HTTP is unencrypted, this means that we can just string the .pcap file and grep it to get the flag we're looking for.
---

![grep](http://i.imgur.com/affRQsy.png)


# :es: Solución :es:
---
###### Podemos ver que es un archivo de TCP/IP, así que lo vamos a analizar con Wireshark.
---

![file](http://i.imgur.com/mJGz29a.png)

---
###### Se trata de una conversación HTTP entre unas IPs, con algún request y POST loging en él.
---

![wire](http://i.imgur.com/yrH2rvv.png)

---
###### Simplemente filtramos para obtener el POST data, en el cual se encuentran el usuario admin y la password en texto plano, sin encriptar (ya que es HTTP, no HTTPS) la cual es la propia flag.
---

![hex](http://i.imgur.com/OrTMf1E.png)

---
###### Hay un truquillo, ya que es HTTP y sabemos que no está encriptado el pcap, simplemente podemos hacerle un STRINGS, para sacar todo el texto, y de ahí pasarle pipe a grep, para obetner la flag.
---

![grep](http://i.imgur.com/affRQsy.png)


