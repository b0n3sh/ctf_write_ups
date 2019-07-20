# Least Significant Bit Extractor
---
In steganography, the lsb method is widely used, so I created this minitool to help me out in CTF's, and instead of using a premade tool, I created mine from scratch.

## Method
---
An image is made out by pixels, and every pixel is made by 3 colours (RGB) each of it has its own value from 0 to 255, which in binary would be a 8bit number, (a pixel is a sum of 3 bytes, each for each colour)

255 `1111 1111 in binary` would be black
0 `0000 0000 in binary` would be white

The least significant bit would be the one which is the rightmost, which has a value of 1 bit, while the leftmost would have a value of 128 bits.

The method then consits in switching the rightmost binary value of every colour, starting from R-G-B(1st pixel), then R-G-B(2nd pixel) and so on.

So for decrypting a hidden stego using lsb, we just have to grab every last bit of every colour in every pixel in the image, then concatenate it and turn into data, and check if it's the text we looking for.

## Installation
---
You just need python3 and install the requirements.txt `pip3 install -r requirements.txt`.
* The program whill ask for the user image to process.
* Then the text it found will be prompted. (you can change the regex for the flag or whatever text you're looking for inside the code)
