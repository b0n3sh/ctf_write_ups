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
Inspecting the source code, there's the main****.js file, where is has a validator function, we debug it and step into the code, which is validator.js, we take that function and print it as an alert, getting the flag.

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

### Rise of the monkeys
Just execute the encrypter and input their hashed passwod, weird.

### Cyber crime does pay
When we transfer from euros to cyber money, the system rounds up only to 2 decimals, so when we move 0.17 euros to cyber money, instead of receiving 0.17*0.03125 = 0.0053125 we get 0.01 cyber money, having a 0.01-0.0053125 = +0.0046875 benefit.

![](http://i.imgur.com/PCHaF95.png)

We create a script to spam requests for converting back money and voila 

![](https://i.imgur.com/6WrxhUx.png)

Now we can buy those secrets


