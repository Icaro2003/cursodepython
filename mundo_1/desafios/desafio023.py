# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# Ex:
# Digite um número: 1834

# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

from colorama import Fore

valor_inicial = int(input('Informe um valor: '))

unidade = valor_inicial % 10
dezena = valor_inicial // 10 % 10
centena = valor_inicial // 100 % 10
milhar = valor_inicial // 1000 % 10

print('Unidade: {}{}{}'.format(Fore.RED, unidade, Fore.RESET))
print('Dezena: {}{}{}'.format(Fore.RED, dezena, Fore.RESET))
print('Centena: {}{}{}'.format(Fore.RED, centena, Fore.RESET))
print('Milhar: {}{}{}'.format(Fore.RED, milhar, Fore.RESET))
