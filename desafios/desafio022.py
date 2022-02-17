# Crie um programa que leia o nome completo de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas.
# > O nome com todas as letras minúsculas.
# > Quantas letras ao todo(sem considerar espaços).
# > Quantas letras tem o primero nome.

name = input('Informe seu nome completo: ').strip()
print('Analisando seu nome...')

name_uppercase = name.upper()
name_lowercase = name.lower()
name_split = name.split()
name_length = len(''.join(name_split))
first_name_length = len(name_split[0])
# name_length = len(name) - name.count(' ')
# first_name = name.split()[0]
# first_name_length = len(first_name)

print('Seu nome em maiúsculas é {}.'.format(name_uppercase))
print('Seu nome em minúsculas é {}.'.format(name_lowercase))
print('Seu nome completo é {} e ele tem ao todo {} letras.'.format(name, name_length))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(
    name_split[0], first_name_length))
