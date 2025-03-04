import random
word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']
word = random.choice(word_bank)
guessedletter='_'*len(word)
turns=8
while turns > 0:
    print('\nCurrent letter: ' + ' '.join(guessedletter))



