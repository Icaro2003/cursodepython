from datetime import date
year_user = int(input('Que ano você quer analisar? '))

if year_user == 0:
    year_user = date.today().year

if (year_user % 4 == 0) and (year_user % 100 != 0) or (year_user % 400 == 0):
    print('{} é ANO BISSEXTO!'.format(year_user))
else:
    print('O ano de {} NÃO É ANO BISSEXTO!'.format(year_user))
