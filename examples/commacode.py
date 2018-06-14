def add(spam):
    spam.insert(len(spam)-1, 'and')
    new_spam = ', '.join(spam)
    new_spam = new_spam.replace('and,', 'and')
    return new_spam

string = []
print('Enter a word or enter nothing to stop:- ')
while True:
    name = input()
    if name == '':
        break
    string += [name]
print(add(string))
