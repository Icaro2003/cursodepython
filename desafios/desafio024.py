# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

from colorama import Fore, Style

city = input('Informe o nome de uma cidade: ').strip()
city_santo = 'SANTO' in city.split()[0].upper()
# city_santo = 'SANTO' in city[:5].upper()
print('{}{}{} começa com {}"SANTO"{}? {}{}{}{}'.format(Fore.BLUE, city, Fore. RESET,
    Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Style.BRIGHT, city_santo, Style.RESET_ALL))
