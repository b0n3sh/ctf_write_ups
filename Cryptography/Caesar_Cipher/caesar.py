#!/usr/bin/python3

SYMBOLS = 'abcdefghijklmnopqrstuvwxyz'

text = input('Text: ')

mode = input('Mode: ')


for key in range(len(SYMBOLS)):
	translated = ''
	for symbol in text:
		index = SYMBOLS.find(symbol) + key
		if index >= len(SYMBOLS):
			index = index - len(SYMBOLS)
		elif index < 0:
			index = index + len(SYMBOLS)
		translated = translated + SYMBOLS[index]
	print(translated + '-----------> with key ' + str(key))