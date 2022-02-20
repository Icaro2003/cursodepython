km_rodado = float(str(input('Informe a quantidade km rodados: ')))
dias_alugados = int(
    input('Informe a quantidade de dias que o carro foi alugado: '))
preco_total = (dias_alugados * 60) + (km_rodado * 0.15)

print('O cliente fez {}km rodados, em um período de {} dias. O total a pagar é de R$ {:.2f}.'.format(
    km_rodado, dias_alugados, preco_total))
