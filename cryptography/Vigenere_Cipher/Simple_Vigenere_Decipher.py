text = 'ZORRO'
keyword = 'PIZZA'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ciphered = ''

for i in range(len(text)):
	num = (LETTERS.find(text[i]) + LETTERS.find(keyword[i])) % 26
	ciphered += LETTERS[num]
print(ciphered)