# Crie um programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra "A".
# > Em que posição ela aparece a primeira vez.
# > Em que posição ela aparece a última vez.

from colorama import Fore

frase = str(input('Informe uma frase: ')).strip()
frase_upper = frase.upper()
letra_a = frase_upper.count('A')
pos_inicial = frase_upper.find('A') + 1
pos_final = frase_upper.rfind('A') + 1

print('"A" aparece {}{}{} vezes na frase: {}{}{}.'.format(
    Fore.RED, letra_a, Fore.RESET, Fore.BLUE, frase, Fore.RESET))
print('"A" aparece na posição {}{}{} da frase: {}{}{}.'.format(
    Fore.RED, pos_inicial, Fore.RESET, Fore.BLUE, frase, Fore.RESET))
print('"A" aparece na posição {}{}{} da frase {}{}{}.'.format(
    Fore.RED, pos_final, Fore.RESET, Fore.BLUE, frase, Fore.RESET))
