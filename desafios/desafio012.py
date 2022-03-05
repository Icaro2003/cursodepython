from colorama import Fore, Style

price_product = float(input('Informe o preço do produto: R$ '))
super_sale = price_product - (price_product * 5 / 100)

print('O produto que custava {}R$ {}{}, na promoção com desconto de 5% vai custar {}{}R$ {:.2f}{}.'.format(
    Fore.GREEN, price_product, Fore.RESET, Fore.GREEN, Style.BRIGHT, super_sale, Style.RESET_ALL))
