from colorama import Fore

with open('ciphertext.txt') as c:
	ciphertext = c.read()


sub = {
	'k': 'e',
	'a': 't'
}

text = ''
for char in ciphertext:
	if char in sub:
		char = char.replace(char, f'{Fore.GREEN}{sub[char]}{Fore.RESET}')
	text += char

print(text)