any = str(input('Digite algo: '))

print('O tipo primitivo desse valor é: {}'.format(type(any)))
print('Só tem espaços? {}'.format(any.isspace()))
print('É um número? {}'.format(any.isnumeric()))
print('É alfabético? {}'.format(any.isalpha()))
print('É alfanumérico? {}'.format(any.isalnum()))
print('Está em maiúsculas? {}'.format(any.isupper()))
print('Está em minúsculas? {}'.format(any.islower()))
print('Está capitalizada? {}'.format(any.istitle()))
