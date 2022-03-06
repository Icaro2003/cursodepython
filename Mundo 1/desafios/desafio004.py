from colorama import Fore, Back, Style

any = str(input('Digite algo: '))

print('O tipo primitivo desse valor é: {}{}{}'.format(Fore.BLUE, type(any), Fore.RESET))
print('Só tem espaços? {}{}{}'.format(Fore.RED, any.isspace(), Fore.RESET))
print('É um número? {}{}{}{}'.format(Fore.YELLOW, Back.CYAN ,any.isnumeric(), Style.RESET_ALL))
print('É alfabético? {}{}{}{}'.format(Fore.BLUE, Back.YELLOW, any.isalpha(), Style.RESET_ALL))
print('É alfanumérico? {}{}{}{}'.format(Fore.BLACK, Back.WHITE, any.isalnum(), Style.RESET_ALL))
print('Está em maiúsculas? {}{}{}'.format(Fore.MAGENTA, any.isupper(), Fore.RESET))
print('Está em minúsculas? {}{}{}'.format(Fore.GREEN, any.islower(), Fore.RESET))
print('Está capitalizada? {}{}{}'.format(Fore.CYAN, any.istitle(), Fore.RESET))
