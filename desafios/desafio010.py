brl = float(input('Quanto você tem em na carteira? R$  '))
usd = brl / 5.37
eur = brl / 5.98
jpy = brl * 21.48

print('Com R$ {} você pode comprar:\n'.format(brl))
print('$ {:.2f}'.format(usd))
print('Є {:.2f}'.format(eur))
print('¥ {:.2f}'.format(jpy))
