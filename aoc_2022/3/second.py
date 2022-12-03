#!venv/bin/python3

score = 0
with open('input', 'r') as r:
    rucksacks = r.read().splitlines()
    i = 0
    while i < len(rucksacks):
        first = rucksacks[i]
        for letter in first:
            if letter in rucksacks[i+1] and letter in rucksacks[i+2]:
                if letter.isupper():
                    score += ord(letter)%65+27
                elif not letter.isupper():
                    score += ord(letter)%97+1
                break
        i+=3

print(score)
