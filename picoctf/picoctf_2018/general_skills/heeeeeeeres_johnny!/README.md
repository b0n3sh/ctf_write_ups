Okay, so we found some important looking files on a linux computer. Maybe they can be used to get a password to the process. Connect with nc 2018shell.picoctf.com 35225. Files can be found here: [passwd](passwd) [shadow](shadow).

# Solution
---
The own name of the challenge give us a hint, we have to use john the ripper to crack the hash, first unshadowing the passwd/shadow files, and then we can use the rockyou.txt database.

# Solución
---
El propio nombre de la prueba nos da una pista, tenemos que usar simplemente john the ripper para crackear el hash, pudiendo usar rockyou.txt como wordlist.

