from colorama import Fore, Style

num = int(input('Informe um número: '))

if num % 2 == 0:
    print('O número {}{}{} é {}{}PAR{}!'.format(Fore.RED, num,
        Fore.RESET, Style.BRIGHT, Fore.BLUE, Style.RESET_ALL))
else:
    print('O número {}{}{} é {}{}ÍMPAR{}!'.format(Fore.RED, num,
        Fore.RESET, Style.BRIGHT, Fore.YELLOW, Style.RESET_ALL))
