#!/usr/bin/python3

text = 'cvpbPGS{guvf_vf_pelcgb!}'
key = 13
LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def main():
	deciphered = ''
	for letter in text:
		if letter.lower() in LETTERS:
			num = LETTERS.find(letter.lower()) - key
			if letter.isupper():
				deciphered += LETTERS[num].upper()
			else:
				deciphered += LETTERS[num]
		else:
			deciphered += letter
	return deciphered

if __name__ == '__main__':
	print(main())