#!venv/bin/python3
# Substitution cipher

import random, pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = ''
message = ''

def main():
	global key, message
	message = input('Enter the text you want to process:\n')
	mode = input('Do you want to (E)ncrypt or (D)ecrypt?:\n').lower()
	while not mode.startswith('d') and not mode.startswith('e'):
		mode = input('Do you want to (E)ncrypt or (D)ecrypt?:\n').lower()
	if mode.startswith('d'):
		key = input('Insert the decrypting key:\n')
		return decryptsubstitution()
	else:
		key = getrandomkey()
		return(encryptsubstitution())

def translator(a,b):
	translated = ''
	for symbol in message:
		if symbol.upper() in a:
			currentindex = a.find(symbol.upper())
			if symbol.isupper():
				translated += b[currentindex]
			else:
				translated += b[currentindex].lower()
		else:
			translated += symbol 
	return translated

def encryptsubstitution():
	print(f'"{message}" encrypted to "{translator(LETTERS, key)}" with key "{key}"')
	pyperclip.copy(translator(LETTERS, key))

def decryptsubstitution():
	print(f'"{message}" decrypted to "{translator(key, LETTERS)}" with key "{key}"')
	pyperclip.copy(translator(key, LETTERS))

def getrandomkey():
	key = list(LETTERS)
	random.shuffle(key)
	return ''.join(key)

if __name__ == '__main__':
	main()

