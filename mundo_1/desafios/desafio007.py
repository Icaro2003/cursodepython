from colorama import Fore

nome = str(input('Digite o nome do aluno: '))
n1 = float(str(input('Digite a primeira nota: ')))
n2 = float(str(input('Digite a segunda nota: ')))
addition = n1 + n2
m = addition / 2

print('O aluno {}{}{} teve as notas {}{}{} e {}{}{}, a média calculada foi {}{:.2f}{}.'.format(
    Fore.MAGENTA, nome, Fore.RESET, Fore.BLUE, n1, Fore.RESET, Fore.BLUE, n2, Fore.RESET, Fore.RED, m, Fore.RESET))
