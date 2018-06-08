import random, sys

def addition():
        points = 0
        print('Lets start addition game(10 rounds)')
        for x in range(10):
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            com_answer = num1 + num2
            print(str(num1) + ' + ' + str(num2) + ' = ')
            user_answer = int(input())
            if user_answer == com_answer:
                print('Correct')
                points = points + 5
            else:
                print('Incorrect')
                points = points - 5
        print('Total points = ' + str(points))
        print('Thanks for playing')
        sys.exit()

def subtraction():
        points = 0
        print('Lets start Subtraction game(10 rounds)')
        for x in range(10):
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            com_answer = num1 - num2
            print(str(num1) + ' - ' + str(num2) + ' = ')
            user_answer = int(input())
            if user_answer == com_answer:
                print('Correct')
                points = points + 5
            else:
                print('Incorrect')
                points = points - 5
        print('Total points = ' + str(points))
        print('Thanks for playing')
        sys.exit()

print('Welcome to calculation game')
while True:
    operator = input('Choose any operator? +,-')
    if operator == '+':
        addition()
    elif operator == '-':
        subtraction()
    else:
        print('You entred something wrong')
        sys.exit()
