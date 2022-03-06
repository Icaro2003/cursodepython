dia_nasc = str(input('Dia = '))
mes_nasc = str(input('Mês = '))
ano_nasc = str(input('Ano = '))

print('Você nasceu no dia {}{}{} do {}{}{} de {}{}{}. Correto?'.format(
    '\033[35m', dia_nasc, '\033[m', '\033[35m', mes_nasc, '\033[m', '\033[35m', ano_nasc, '\033[m'))
