import random
import string

adjectives = ['sleepy', 'slow', 'hot', 'cold', 'big', 'red', 'orange', 'yellow', 'green', 'blue', 'good', 'old', 'white', 'free', 'brave']

nouns = ['apple', 'dinosaur', 'ball', 'cat', 'goat', 'dragon', 'car', 'duck', 'panda']

print('Добро пожаловать!')

while True:
    b = random.choice(adjectives)
    a = random.choice(nouns)
    c = random.randrange(0, 100)
    d = random.choice(string.punctuation)
    
    p = b + a + str(c) + d
    print('Новый пароль: %s' % p)
    
    response = input('Сгенерировать другой пароль? Введите д или н: ')
    if response == 'н':
        break
