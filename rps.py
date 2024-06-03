#rock paper scissor
import random

def play():
    you=input("enter 'r','p','s' for rock paper scissors: ")
    computer=random.choice(['r','p','s'])
    
    if you==computer:
        return 'draw'

    if you_win(you,computer):
        return 'u winnn'

    return 'u lose...'
   
def you_win(u,c):
    if (u=='r' and c=='s') or (u=='p' and c=='r') or (u=='s' and c=='p'):
        return True

play()
            



'''
 if s=='r' and computer=='s':
        return 'u wonn'
    elif s=='s' and computer=='r':
        return 'u losttt'
    elif s=='p' and computer=='r':
        return 'u wonnn'
    elif s=='r' and computer=='p':
        return 'u losttt'
    elif s=='s' and computer=='p':
        return 'u wonnnn'
    elif s=='p' and computer=='s':
        return 'u losttt'

'''
