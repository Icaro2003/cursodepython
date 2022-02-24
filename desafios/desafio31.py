traveled_km = float(input('Qual a distância da sua viagem? '))

if traveled_km > 0:
    print('Você está prestes a fazer uma viagem de {} Km'.format(traveled_km))
    
    if traveled_km <= 200:
        ticket = traveled_km * 0.5
        print('E o preço da sua passagem será de R$ {:.2f}'.format(ticket))
    else:
        ticket = traveled_km * 0.45
        print('E o preço da sua passagem será de R$ {:.2f}'.format(ticket))
else:
    print('Digite uma distância válida!')
