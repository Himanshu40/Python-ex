import random

print('Welcome to Guess game')
secret_number = random.randint(1,10)

#Ask the player to guess 10 times
for number in range(1,11):
    user_number = int(input('Guess a Number between 1 and 10:- '))
    if user_number > secret_number:
        print('You guess above the secret number')
    elif user_number < secret_number:
        print('You guessed below the secret number')
    else:
        break

if user_number == secret_number:
    print('You guessed the exact number in ' + str(number) + ' times')
else:
    print('Better luck next time. The secret number is ' + str(secret_number))
