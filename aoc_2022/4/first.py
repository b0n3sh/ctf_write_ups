#!venv/bin/python3

score = 0
with open('input', 'r') as c:
	lines = c.read().splitlines()
	for line in lines:
		first_elf, second_elf = line.split(',')
		first_elf_first_zone, first_elf_second_zone = map(lambda x: int(x), first_elf.split('-'))
		second_elf_first_zone, second_elf_second_zone = map(lambda x: int(x), second_elf.split('-'))

		if first_elf_first_zone<= second_elf_first_zone and first_elf_second_zone >= second_elf_second_zone:
			score+=1

		elif second_elf_first_zone <= first_elf_first_zone and second_elf_second_zone >= first_elf_second_zone:
			score+=1
print(score)

		



