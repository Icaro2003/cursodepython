# Crie um programa que leia um número Real qualquer do teclado e mostre sua porção inteira

from math import trunc
from colorama import Fore

num = float(input('Digite um número: '))

print('O valor digitado foi {}{}{} e a sua porção inteira é {}{}{}.'.format(
    Fore.BLUE, num, Fore.RESET, Fore.RED, trunc(num), Fore.RESET))

# n = float(input('Digite um número: '))

# print('O valor digitado foi {} e a sua porção inteira é {}.'.format(n, int(n))
