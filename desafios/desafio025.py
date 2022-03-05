# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

from colorama import Fore, Style

name = str(input('Informe seu nome completo: ')).strip()
name_silva = 'SILVA' in name.upper()
print('{}{}{} tem {}Silva{}? {}{}{}{}'.format(Fore.BLUE, name, Fore.RESET,
    Style.BRIGHT, Style.RESET_ALL, Style.BRIGHT, Fore.BLUE, name_silva, Style.RESET_ALL))
