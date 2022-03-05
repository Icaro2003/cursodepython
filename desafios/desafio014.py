from colorama import Fore

graus_c = float(str(input('Informe a temperatura em ºC: ')))
graus_f = ((9 * graus_c) / 5) + 32

print('A temperatura de {}{}°C{} corresponde a {}{}ºF{}!'.format(
    Fore.BLUE, graus_c, Fore.RESET, Fore.RED, graus_f, Fore.RESET))
