from random import randint
from time import sleep
random_num = randint(0, 5)

print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)

user_num = int(input('\nEm qual número eu pensei? '))

if user_num >= 0 and user_num <= 5:
    print('PROCESSANDO...')
    sleep(0.6)

    if user_num == random_num:
        print('PARABÉNS, você acertou, o número era {}!'.format(random_num))
    else:
        print('ERROU! Eu pensei no número {} e não no {}!'.format(
            random_num, user_num))
else:
    print('Informe um valor entre 0 e 5!')
