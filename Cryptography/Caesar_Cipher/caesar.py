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
	global translated, output
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
	output = translated + '	(encrypted ----> with key ' + str(key) + ')'
	return output, translated
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

def textlen():
	if len(translated) > 5:
		print(f'The encrypted text, {translated[0:5]}... with the selected key {wantedkey} has been copied to your clipboard!')
	else:
		print(f'The encrypted text, {translated} with the selected key {wantedkey} has been copied to your clipboard!')

#Get variables.
text = input('Text: ').lower()

# We check that we get a correct mode.
mode = input('Mode ("e" for encrypt or "d" for decrypt): ').lower()
while mode != 'e' and mode != 'd':
	mode = input('Write "e" for encrypt or "d" for decrypt": ')

knownkey = input('Key: ')

# We check if the known key is a number between 0 to 25.
if knownkey.isdigit():
	while int(knownkey) < 0 or int(knownkey) > 25:
		knownkey = input('Please, write a number from 0 to 25, leave it empty or write ''random'': ')
# If he writes whatever different from a number, we check that it's a possible command.
else:
	while knownkey != '' and knownkey.lower() != 'random':
		knownkey = input('Please, write a number from 0 to 25, leave it empty or write ''random'': ')

# Check for the mode.

# If mode is encrypt.
if mode == 'e':
	# Check if we know the key or not.
	if knownkey == '':
		# If we don't give a key, we cipher the text in everyway possible.
		for key in range(len(SYMBOLS)):
			cipher(key=key)
			print(output)
		# Now we iniciate the method for selecting the desired key to be copied into the clipboard.
		wantedkey = input('Which key you want to copy to your keyboard? (Write the number): ')
		while int(wantedkey) < 0 and int(wantedkey) > 25:
			input('Please write a number from 0 to 25: ')
		cipher(key=wantedkey)
		pyperclip.copy(translated)
		# We shorten the encrypted text to print it.
		textlen()
	# If we give the random command, we choose a random key from 0 to 25.		
	elif knownkey == 'random':
		wantedkey = random.randrange(1, 26)
		cipher(key=wantedkey)
		pyperclip.copy(translated)
		textlen()
	# If we give a specific key, we just operate as normal.
	else:
		cipher(key=knownkey)
		pyperclip.copy(translated)
		wantedkey = knownkey
		textlen()
# If mode is decrypt.
else:
	# Check if we know the key or not.
	if knownkey == '':
		# If we don't give a key, we try to bruteforce the text.
		for key in range(len(SYMBOLS)):
			decipher(key=key)
