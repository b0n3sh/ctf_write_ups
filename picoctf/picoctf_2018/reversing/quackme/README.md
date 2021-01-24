Can you deal with the Duck Web? Get us the flag from this [program](https://2018shell.picoctf.com/static/1d21f78fd2b82ebff2ad54a8b09081c8/main). You can also find the program in /problems/quackme_3_9a15a74731538ce2076cd6590cf9e6ca.

# :uk: Solution :uk:
Looking at the disassembly of the code we can see a call to `do_magic`.

If we open it with r2, we can see that there's a loop where it takes our input and XOR it with a sekretBuffer which lays in `0x8048858`.

It only takes the first 25 bytes of the array so we open r2 and do
``` bash
$ pcp 0x19 @ obj.sekrutBuffer
```
And we get the buffer we need, I wrote a script for getting the flag just XORing every char with the greeting message, as it yields the flag.
