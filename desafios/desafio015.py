from colorama import Fore

km_rodado = float(input('Informe a quantidade km rodados: '))
dias_alugados = int(
    input('Informe a quantidade de dias que o carro foi alugado: '))
preco_total = (dias_alugados * 60) + (km_rodado * 0.15)

print('O cliente fez {}{}km{} rodados, em um período de {}{}{} dia(s). O total a pagar é de {}R$ {:.2f}{}.'.format(
    Fore.BLUE, km_rodado, Fore.RESET, Fore.BLUE, dias_alugados, Fore.RESET, Fore.GREEN, preco_total, Fore.RESET))
