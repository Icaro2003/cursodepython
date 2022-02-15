# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# Ex:
# Digite um número: 1834

# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

valor_inicial = int(input('Informe um valor: '))

unidade = valor_inicial % 10
dezena = valor_inicial // 10 % 10
centena = valor_inicial // 100 % 10
milhar = valor_inicial // 1000 % 10

print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
