import random

def guess(x):
    
    random_num=random.randint(1,x)
    guess=0
    
    while guess != random_num:
        guess=int(input('enter ur guess: '))
        if guess < random_num:
            print("go higherrr")
        elif guess> random_num:
            print('go lowerrrr')
    print('YAY U GUESSED MY NUMBER WOOHOO')

guess(int(input('enter ur limit: ')))

