As nice as it is to use our webshell, sometimes its helpful to connect directly to our machine. To do so, please add your own public key to ~/.ssh/authorized_keys, using the webshell. The flag is in the ssh banner which will be displayed when you login remotely with ssh to with your username.
![problem](http://i.imgur.com/qjuOUrI.png)


# :uk: Solution :uk:
---

---
###### We don't even have to add our own public key to the authorized_keys, it's a bug they have, I don't think it's working as intended, but if you ssh straight into their server, it lets you in, without typing anything else than your pass.
###### And even gives you the flag before logging into the server successfully.
---
![flag](http://i.imgur.com/ENLR936.png)

# :es: Solución :es:
---

---
###### No tenemos ni que añadir nuestra public key al authorized_keys, supongo que será un bug, pero no tienes ni que añadir tu public key para entrar a su servidor, ni hace falta logearnos con nuestra password, ya que nos dan la flag simplemente con el request de SSH.
---
![flag](http://i.imgur.com/ENLR936.png)
