import sys

birthdays = {'Alice':'Apr 1', 'Bob':'Dec 12'}

while True:
    name = input('Enter a name:(blank to quit) ')
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('No information regarding that person')
        bday = input('What is their birthday? ')
        birthdays[name] = bday
        print('Birthday info updated')
    print(birthdays.keys())
    print(birthdays.values())
    print(list(birthdays.items()))
    sys.exit()
