# Crie um programa que leia o nome completo de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas.
# > O nome com todas as letras minúsculas.
# > Quantas letras ao todo(sem considerar espaços).
# > Quantas letras tem o primero nome.

from colorama import Fore
from time import sleep

name = str(input('Informe seu nome completo: ')).strip()
print('{}Analisando seu nome...{}'.format(Fore.MAGENTA, Fore.RESET))
sleep(0.5)
name_without_space = ''.join(name.split())
# name_length = len(name) - name.count(' ')
# first_name = name.split()[0]
# first_name_length = len(first_name)

print('\nSeu nome em maiúsculas é {}{}{}.'.format(
    Fore.BLUE, name.upper(), Fore.RESET))
print('Seu nome em minúsculas é {}{}{}.'.format(
    Fore.BLUE, name.lower(), Fore.RESET))
print('Seu nome completo é {}{}{} e ele tem ao todo {}{}{} letras.'.format(
    Fore.BLUE, name, Fore.RESET, Fore.RED, len(name_without_space), Fore.RESET))
print('Seu primeiro nome é {}{}{} e ele tem {}{}{} letras.'.format(
    Fore.BLUE, name.split()[0], Fore.RESET, Fore.RED, len(name.split()[0]), Fore.RESET))
