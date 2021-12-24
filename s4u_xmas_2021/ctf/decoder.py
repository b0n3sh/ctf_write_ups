#!/usr/bin/python3
import re

with open('final_hex', 'r') as c:
	raw_hex = c.read()

	# Remove packet headers, checksum and end of packets. (7+3+2) = 12 bytes.
	raw_hex = re.sub(r'[0-9a-f]{2} [0-9a-f]{2} [0-9a-f]{2} 0d 00 01 [0-9a-f]{2} [0-9a-f]{2} [0-9a-f]{2} [0-9a-f]{2} [0-9a-f]{2} [0-9a-f]{2}', '', ' '.join(raw_hex.split()))
	raw_hex = re.sub(r'0d 00', '', raw_hex)
	raw_hex = re.sub(r'01 [0-9a-f]{2} [0-9a-f]{2} [0-9a-f]{2} [0-9a-f]{2} [0-9a-f]{2} [0-9a-f]{2}', '', raw_hex)

	#get almost b64
	output = []
	for char in raw_hex.split():
		output.append(chr(int(char, 16)))

	#Decode multiple chars and breaks
	i = 0
	text = []
	while i < len(output):
		if output[i] == '~':
			num = output[i+1]
			numy = ord(num)-32
			text.append(output[i+2]*numy)
			i+=3
		else:
			text.append(output[i])
			i+=1
	text = re.sub(r'#J', r'\n', ''.join(text))

print(''.join(text))
