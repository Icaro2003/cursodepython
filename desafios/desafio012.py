price_product = float(str(input('Informe o preço do produto: R$ '))
super_sale=price_product - (price_product * 5 / 100)

print('O produto que custava R$ {}, na promoção com desconto de 5% vai custar R$ {:.2f}.'.format(
    price_product, super_sale))
