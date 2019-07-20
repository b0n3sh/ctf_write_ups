#!venv/bin/python3
from PIL import Image
import re, os

regctflag = re.compile(r'[\w{}]')

def main():
	flag = bin_to_text(get_lsbRGB_from_RGBA(image_to_pixels_RGB(ask_image_file())))
	print('-'*30 + f'\nThe text is "{flag}"')

def image_to_pixels_RGB(image):
	with Image.open(image) as c:
		return list(c.getdata())

def get_lsbRGB_from_RGBA(data):
	lista = []
	byte = ''
	for pixel in data:
		for i in range(3):
			if len(byte) == 8:
				lista.append(byte)
				byte = ''
				byte += str(bin(pixel[i]))[-1]
			else:
				byte += str(bin(pixel[i]))[-1]
	return lista

def bin_to_text(data):
	text = []
	for byte in data:
		if regctflag.search(chr(int(byte,2))):
			text.append(chr(int(byte,2)))
	return ''.join(text)

def ask_image_file():
	file = input('Write the name of the file you want to extract data from (absolute or relative path)\n')
	while not file.endswith('.png'):
		file = input('It has to be a .png file\n')
		while not os.path.isfile(file):
			file = input('The file does not exist\n')
	return file

if __name__ == "__main__":
	main()
