from colorama import Fore, Style

salary = float(input('Informe o salário do funcionário: R$ '))
readjust = salary + (salary * 15 / 100)

print('O funcionário que ganhava {}R$ {}{}, com um aumento de {}15%{}, passa a receber um salário de {}{}R$ {:.2f}{}.'.format(
    Fore.GREEN, salary, Fore.RESET, Style.BRIGHT, Style.RESET_ALL, Style.BRIGHT, Fore.GREEN, readjust, Style.RESET_ALL))
