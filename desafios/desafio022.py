# Crie um programa que leia o nome completo de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas.
# > O nome com todas as letras minúsculas.
# > Quantas letras ao todo(sem considerar espaços).
# > Quantas letras tem o primero nome.

name = input('Informe seu nome completo: ')

name_uppercase = name.upper()
name_lowercase = name.lower()
name_split = name.split()
join_name = ''.join(name_split)
name_length = len(join_name)
first_name_length = len(name_split[0])

print('\nO nome escrito em maiúsculo: {}.'.format(name_uppercase))
print('O nome escrito em minúsculo: {}.'.format(name_lowercase))
print('{} tem {} letras.'.format(name, name_length))
print('{} tem {} letras.'.format(name_split[0], first_name_length))