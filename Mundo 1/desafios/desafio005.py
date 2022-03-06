from colorama import Fore

number = int(str(input('Digite um número? ')))
predecessor = number - 1
successor = number + 1

print('Analisando o valor {}{}{}, seu antecessor é {}{}{} e o sucessor é {}{}{}.'.format(
    Fore.BLUE, number, Fore.RESET, Fore.RED, predecessor, Fore.RESET, Fore.RED, successor, Fore.RESET))
