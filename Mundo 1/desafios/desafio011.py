from colorama import Fore

width = float(input('Informe a largura da parede: '))
height = float(input('Informe a altura da parede: '))
area = width * height
ink_liter = area / 2

print('\nSua parede tem a dimensão de {}{}{} X {}{}{}.'.format(
    Fore.GREEN, width, Fore.RESET, Fore.GREEN, height, Fore.RESET, Fore.RED, area, Fore.RESET))
print('Para pintar uma parede com área de {}{}m²{}, você precisará de {}{}l{} de tinta.'.format(Fore.RED, area, Fore.RESET, Fore.RED, ink_liter, Fore.RESET))
