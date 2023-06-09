from random import randint
from time import sleep

sorteio = randint(0, 5)
print('-=-' * 18)
print('Vou pensar em um número de 0 a 5, tente adivinhar...')
print('-=-' * 18)

num = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(3)

if (num == sorteio) :
    print('Parabéns! Você conseguiu me vencer!')
else: 
    print('Ganhei, pensei no número {} e não no {}!'.format(sorteio, num))
