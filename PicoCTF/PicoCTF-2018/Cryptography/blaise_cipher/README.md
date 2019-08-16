My buddy Blaise told me he learned about this cool cipher invented by a guy also named Blaise! Can you figure out what it says? Connect with nc 2018shell.picoctf.com 26039.
![](http://i.imgur.com/mvXpF6W.png)

# :uk: Solution :uk:
---

---
###### If we connect to the direction it gives us, the server replies with the text encrypted.
---
![](http://i.imgur.com/9JixrWn.png)

---
###### Blaise was the real creator of Vigenere cipher, but we don't know the key, so we use some kasiski examination and frequency analisis using our tools, and we picture that the key is "flag", so I wrote a program to decrypt the text.
---
