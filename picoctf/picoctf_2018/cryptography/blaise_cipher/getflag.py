#!/usr/bin/python3
import re
key = 'FLAG'
with open('encryptedtext.txt') as file:
    text = file.read()

ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

keyindex = 0

decrypted = []

for letter in text:
    if letter.upper() in ABC:
            letterind = ABC.find(letter.upper())
            keyind = ABC.find(key[keyindex])
            keyindex += 1
            if letter.isupper():
                decrypted.append(ABC[(letterind-keyind)%26])
            else:
                decrypted.append(ABC[(letterind-keyind)%26].lower())
            if keyindex == 4:
                keyindex = 0
    else:
        decrypted.append(letter)

print(''.join(decrypted)[:100], '...')
print(f"The flag is {re.findall('pico.*}', ''.join(decrypted), re.IGNORECASE)[0]}")

