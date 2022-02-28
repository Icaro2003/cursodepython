from colorama import Style, Fore


brl = float(input('Quanto você tem em na carteira? R$  '))
usd = brl / 5.37
eur = brl / 5.98
jpy = brl * 21.48

print('Com {}{}R$ {:.2f}{} você pode comprar:\n'.format(
    Fore.BLUE, Style.BRIGHT, brl, Style.RESET_ALL))
print('{}{}$ {:.2f}'.format(Fore.RED, Style.BRIGHT, usd))
print('Є {:.2f}'.format(eur))
print('¥ {:.2f}{}'.format(jpy, Style.RESET_ALL))
