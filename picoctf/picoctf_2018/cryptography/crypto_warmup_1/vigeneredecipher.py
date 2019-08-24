#!/usr/bin/python3

message = 'llkjmlmpadkkc'
key = 'thisisalilkey'
LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def decrypt():
	deciphered = ''
	for i in range(len(message)):
		num = LETTERS.find(message[i]) - LETTERS.find(key[i])
		if num < 0:
			num += 26
		deciphered += LETTERS[num]
	return deciphered

print(f'picoCTF{{{decrypt().upper()}}}')
