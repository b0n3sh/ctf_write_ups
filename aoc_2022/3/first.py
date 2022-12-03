#!venv/bin/python3

score = 0
with open('input', 'r') as r:
    for rucksack in r:
        rucksack = rucksack.strip()
        ruck_len = len(rucksack)//2
        left, right = rucksack[:ruck_len], rucksack[ruck_len:]
        for letter in left:
            if letter in right:
                if letter.isupper():
                    score += ord(letter)%65+27
                elif not letter.isupper():
                    score += ord(letter)%97+1
                break
print(score)
