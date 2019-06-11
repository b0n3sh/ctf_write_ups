#!venv/bin/python3

import random
import pyperclip

# TO-DO
# 2.Add decrypt
# 5.Clean code (change modules)
# 6.Integrate with bash

# Instructions
print('''Instructions for caesar cipher:
	1. Insert the text you want to encrypt-decrypt (from a to z).
	2. Select the mode (encrypt-decrypt), writing it.
	3. Insert the key to apply (if you leave it empty, it will use all possible keys, if you write random, it will choose a random key)
	4. The translated text will be copied to your clipboard automatically.''')

SYMBOLS = 'abcdefghijklmnopqrstuvwxyz'

def cipher(key=''):
	global translated
	translated = ''
	for symbol in text:
		if symbol in SYMBOLS:
			index = SYMBOLS.find(symbol) + int(key)
			# Wrap-around in case we exceed the length of the symbol table and we need to start from the start again.
			if index >= len(SYMBOLS):
				index = index - len(SYMBOLS)
			# Now we start building up the translated variable.
			translated = translated + SYMBOLS[index]
			# We finally print the text.
		else:
			translated = translated + symbol
	print(translated + '	(encrypted ----> with key ' + str(key) + ')')

def decipher(key=''):
	global translated
	translated = ''
	for symbol in text:
		if symbol in SYMBOLS:
			index = SYMBOLS.find(symbol) - int(key)
			# Wrap-around in case we exceed the length of the symbol table and we need to start from the start again.
			if index < 0:
				index = index + len(SYMBOLS)
			# Now we start building up the translated variable.
			translated = translated + SYMBOLS[index]
			# We finally print the text.
		else:
			translated = translated + symbol
	print(translated + 'decrypted ----> with key ' + str(key))

#Get variables.
text = input('Text: ').lower()

# We check that we get a correct mode.
mode = input('Mode ("encrypt" or "decrypt"): ').lower()
while mode != 'encrypt' and mode != 'decrypt':
	mode = input('Write "encrypt" or "decrypt": ')

knownkey = input('Key: ')

# We check if the known key is a number between 0 to 25.
if knownkey.isdigit():
	while int(knownkey) < 0 or int(knownkey) >= 25:
		knownkey = input('Please, write a number from 0 to 25, leave it empty or write ''random'': ')
# If he writes whatever different from a number, we check that it's a possible command.
else:
	while knownkey != '' and knownkey.lower() != 'random':
		knownkey = input('Please, write a number from 0 to 25, leave it empty or write ''random'': ')

# Check for the mode.

# If mode is encrypt.
if mode == 'encrypt':
	# Check if we know the key or not.
	if knownkey == '':
		# If we don't give a key, we cipher the text in everyway possible.
		for key in range(len(SYMBOLS)):
			cipher(key=key)

		#pyperclip.copy(cipher(keytocopy))
	# If we give the random command, we choose a random key from 0 to 25.		
	elif knownkey == 'random':
		cipher(key=random.randrange(1, 26))
		pyperclip.copy(translated)
	else:
		cipher(key=knownkey)
		pyperclip.copy(translated)
else:
	# Check if we know the key or not.
	if knownkey == '':
		# If we don't give a key, we try to bruteforce the text.
		for key in range(len(SYMBOLS)):
			decipher(key=key)
