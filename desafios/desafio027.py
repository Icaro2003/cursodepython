# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

# Ex: Ana Maria de Souza
# primeiro=Ana
# último=Souza
nome_completo = input('Informe seu nome completo: ')
nome_completo_dividido = nome_completo.split()
qtd_nome_completo = len(nome_completo_dividido)

nome = nome_completo_dividido[0]
print('Seu nome é: {}'.format(nome))
sobrenome = nome_completo_dividido[qtd_nome_completo - 1]
print('Seu sobrenome: {}'.format(sobrenome))
