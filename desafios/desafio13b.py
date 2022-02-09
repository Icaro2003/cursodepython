produto = float(input('Digite o preço do produto: R$ '))
produto_vista = produto - ((produto * 10) / 100)
produto_prazo = produto + ((produto * 8) / 100)

print('\nO produto que custava R$ {}, quando comprado à vista tem um desconto de 10%, e passa a custar: R$ {}'.format(
    produto, produto_vista))
print('O produto que custava R$ {}, quando comprado à prazo tem um aumento de 8%, e passa a custar R$ {}'.format(
    produto, produto_prazo))
