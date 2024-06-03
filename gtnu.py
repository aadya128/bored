import random

def guess(x):
    r=0
    random_num=random.randint(1,x)
    print(random_num)
    while r != 'c' and 1!=x:
        r=input('enter h , l or c: ')
        if r=='h':
            input( f'is {random.randint(random_num,x)} ur guess?' )
        
        elif r=='l':
            input(f' is {random.randint(1,random_num)} ur guess? ')
         
        break
   
    if r=='c':
        print('YAYY ITS CORRECT!')

guess(10)
