from colorama import Fore, Style

traveled_km = float(input('Qual a distância da sua viagem? '))

if traveled_km > 0:
    print('Você está prestes a fazer uma viagem de {}{} Km{}'.format(
        Fore.RED, traveled_km, Fore.RESET))

    if traveled_km <= 200:
        ticket = traveled_km * 0.5
        print('E o preço da sua passagem será de {}R$ {:.2f}{}'.format(
            Fore.GREEN, ticket, Fore.RESET))
    else:
        ticket = traveled_km * 0.45
        print('E o preço da sua passagem será de {}R$ {:.2f}{}'.format(
            Fore.GREEN, ticket, Fore.RESET))
else:
    print('{}{}Digite uma distância válida!{}'.format(
        Style.BRIGHT, Fore.RED, Style.RESET_ALL))
