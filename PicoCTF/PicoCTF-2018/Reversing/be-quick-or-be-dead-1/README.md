You find [this](https://www.youtube.com/watch?v=CTt1vk9nM9c) when searching for some music, which leads you to [be-quick-or-be-dead-1.](https://2018shell.picoctf.com/static/f825b5db114de1d3f811961b54f9cfb1/be-quick-or-be-dead-1) Can you run it fast enough? You can also find the executable in /problems/be-quick-or-be-dead-1_3_aeb48854203a88fb1da963f41ae06a1c.
![](http://i.imgur.com/Ev9StEG.png)


# :uk: Solution :uk:
---

---
###### If we execute the program, we get a prompt saying that our compute is slow, and we need a faster one, so it doesn't print the flag.
---
![](http://i.imgur.com/hTqXJ6a.png)

---
###### We can do this challenge in 3 different ways:
* Using gdb wiht [PEDA](https://github.com/longld/peda)
* Dissasemblying and changing the time it waits for print the error (its limit)
* Dissasemblying and changing the value it operates to finish the program and print the flag.

As the first one is really easy, it just needs to open gdb with PEDA, and the flag will be automaticaly displayed, but that's not interesting, let's see the third way.
---
![gdb-peda](http://i.imgur.com/IvguK8b.png)

---
###### Now let's start with the interesting, we open the file in writing mode with radar2, and then we analyze it, with `aaaa` command, then we can see that there are some interesting functions as get_key(), calculate_key(), print_flag(), set_timer()...
---
![](http://i.imgur.com/DcjcMpa.png)

---
###### We have nothing to do in the main funcion, so we move to `calculate_key()`, where we can see that there's a little lop, which starts at `0x0040070a`, giving the `dword` the value `0x6fd47e3c`, and then it adds 1 to `dword` (0x00400711), and then comparing it with the value `0xdfa8fc78`, jumping back to `0x00400711`, adding again 1, until this requirement is met.
---
![](http://i.imgur.com/ePvlimf.png)

---
###### Now we edit the dword value and we add the compared number, just 1 bit behind, of it, and when we execute the program it gives us the flag because the operation is almost instant.
---
![](http://i.imgur.com/4HLcHR7.png)
![](http://i.imgur.com/II0Bkbd.png)
