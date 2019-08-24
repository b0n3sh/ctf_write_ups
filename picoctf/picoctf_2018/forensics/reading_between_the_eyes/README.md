Stego-Saurus hid a message for you in this [image](https://2018shell.picoctf.com/static/9129761dbc4bf494c47429f85ddf7434/husky.png), can you retreive it?

# Solution
---
The flag is hidden using the steganography method called lsb (least significant bit) so I wrote a [tool](https://github.com/B0nesh/CTF_Tools/tree/master/Forensics/Steganography/lsb_extractor) to extract the flag.

### LSB
Least significant bit consists in flipping over the last bit (1 or 0) inside the RGB pixel, which has 3 bytes data (each for every colour), withouth altering the image for the eye to realize.

# Solución
---
La flag está escondida usando esteganografía, concretamente el método lsb (Bit de menos valor), lo que significa que en cada pixel, el cual está compuesto por 3 bytes (rojo, verde y azul), cogemos el último bit de cada uno y vamos poniendo el texto que queremos, sin modificar la imagen a la vista humana.
Por lo que he escrito un [programa](https://github.com/B0nesh/CTF_Tools/tree/master/Forensics/Steganography/lsb_extractor) para extraerla.
### LSB
El método LSB consiste en que se saca el último bit de cada byte que compone un pixel (los 3 colores), y se cambia ese bit por el del texto que pretendemos esconder en la imagen, haciéndolo indetectable al ojo humano, ya que la imagen sigue siendo la misma, sin alteración notable.
