from datetime import date
from colorama import Fore, Style

year_user = int(input('Que ano você quer analisar? '))

if year_user == 0:
    year_user = date.today().year

if (year_user % 4 == 0) and (year_user % 100 != 0) or (year_user % 400 == 0):
    print('{}{}{} é {}{}ANO BISSEXTO{}!'.format(Fore.GREEN, year_user,
        Fore.RESET, Style.BRIGHT, Fore.BLUE, Style.RESET_ALL))
else:
    print('O ano de {}{}{} {}{}NÃO É ANO BISSEXTO{}!'.format(Fore.GREEN,
        year_user, Fore.RESET, Style.BRIGHT, Fore.RED, Style.RESET_ALL))
