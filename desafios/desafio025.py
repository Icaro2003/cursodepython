# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Informe seu nome: ')
silva = "SILVA" in nome

print('O nome {} possui "SILVA"? {}'.format(nome, silva))
