def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

while True:
    try:
        user_num = int(input('Enter a number:- '))
    except:
        print('Wrong data type')
        continue
    collatz(user_num)
    if user_num == 1:
        break
    else:
        continue
