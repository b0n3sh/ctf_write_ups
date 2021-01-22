We heard that there is something hidden in this [picture](https://2018shell.picoctf.com/static/a120d4af95c06068d5f5a08ec14a572d/nowYouDont.png). Can you find it?

# :uk: Solution :uk:

We just create another image with just red colour, the same as ours, and then with the 'compare' command, we will get the output of the different pixels, which turns out to be our flag.

`convert -size 857x783 canvas:'#ff2020' pure.png`

`compare nowYouDont.png pure.png flag.pn`
