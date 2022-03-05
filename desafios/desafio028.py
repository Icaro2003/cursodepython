from random import randint
from time import sleep
from colorama import Fore, Back, Style

random_num = randint(0, 5)

print('-=-' * 18)
print('{}{}{}Vou pensar em um número de 0 a 5. Tente adivinhar...{}'.format(
    Style.BRIGHT, Back.YELLOW, Fore.BLUE, Style.RESET_ALL))
print('-=-' * 18)

user_num = int(input('\nEm qual número eu pensei? '))

if user_num >= 0 and user_num <= 5:
    print('{}PROCESSANDO...{}'.format(Fore.RED, Fore.RESET))
    sleep(0.6)

    if user_num == random_num:
        print('{}PARABÉNS{}, você acertou, o número era {}{}{}!'.format(random_num))
    else:
        print('{}ERROU!{} Eu pensei no número {}{}{} e não no {}{}{}!'.format(Style.BRIGHT,
            Style.RESET_ALL, Fore.RED, random_num, Fore.RESET, Fore.RED, user_num, Fore.RESET))
else:
    print('Informe um valor entre {}0{} e {}5{}!'.format(
        Fore.RED * 2, Fore.RESET * 2))
