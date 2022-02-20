# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
name = str(input('Informe seu nome completo: ')).strip()
name_silva = 'SILVA' in name.upper()
print('{} tem Silva? {}'.format(name, name_silva))
