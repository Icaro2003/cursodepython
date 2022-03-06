# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

# Ex: Ana Maria de Souza
# primeiro=Ana
# último=Souza

from colorama import Fore, Style

name = str(input('Informe seu nome completo: '))
name_split = name.split()
first_name = name_split[0]
last_name = name_split[len(name_split) - 1]

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}{}{}{}'.format(
    Style.BRIGHT, Fore.BLUE, first_name, Style.RESET_ALL))
print('Seu último nome é {}{}{}{}'.format(
    Style.BRIGHT, Fore.BLUE, last_name, Style.RESET_ALL))
