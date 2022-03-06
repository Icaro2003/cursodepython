from colorama import Fore

num = int(input('Digite um número: '))
double = num * 2
triple = num * 3
squareroot = num ** (1/2)

print('\nO dobro de {}{}{} vale {}{}{}.'.format(
    Fore.BLUE, num, Fore.RESET, Fore.RED, double, Fore.RESET))
print('O triplo de {}{}{} vale {}{}{}.'.format(
    Fore.BLUE, num, Fore.RESET, Fore.RED, triple, Fore.RESET))
print('A raiz quadrada de {}{}{} vale {}{:.2f}{}.'.format(
    Fore.BLUE, num, Fore.RESET, Fore.RED, squareroot, Fore.RESET))
