This flag has been encrypted with some kind of cipher, can you decrypt it? Connect with nc 2018shell.picoctf.com 23479.
![](http://i.imgur.com/vYQnDwP.png)

# :uk: Solution :uk:
---
###### As we have a random polyalphabetic cipher, where each letter has a random value, we have to rely on frequency analysis, that's it, knowing that in english language some letters are repeated more than others e.g. E,T,A,O are the most repetated ones, while X,Q,J,Z are the least repeated ones, we are using an online decoder for this.
![](http://i.imgur.com/zm2FJL3.png)
