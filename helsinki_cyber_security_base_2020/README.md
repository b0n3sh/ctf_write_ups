### Steganography I
We just have to check the exif data of the .jpg, the flag is in the Artist tag.

### Steganography II
Using strings, we get a base64 string at the end of the file, we decode it with `$echo "flag" | base64 -d.

### Dr. Kyberzig
Looking inside the javascript in the browser, we check which function changes, with compares with "VERY SECRET KEY".

### Cyber Monkeys
Rot 13, we just have to decipher.

### Who is Alice?
todo

### Password checker
Using strings, the flag is inside.

### CyberBank I 
We just check the robots.txt in the website.

### Two time pad
XOR deciphering

### Cyberbank II
There's a json called Nothingtoseehere inside the website.

### Dr. Kyberzig MK II
todo

### Password II
Using strings we get a base 64, `$echo 'flag' | base64 -d`

### Monkeys are back
Base 64, then we brute force with caesar.

### Steganography III
Exif and there's a thumbnail inserted within the flag.

### Dawn of the monkeys
Lot of text, so we use frequency analisis, knowing it's an email, we can start deciphering some easy words, as FROM, TO, DEAR....

### Don't rush my passwords
Is SHA1, we create a little script to iterate until we find it.

### Password III
Overflow with 257 chars and we get the flag.

