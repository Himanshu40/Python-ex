string = input('Enter any sentence:- ')
count = {}

for character in string:
    count.setdefault(character,0)
    count[character] += 1

print(count)
