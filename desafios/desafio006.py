num = int(str(input('Digite um número: ')))
double = num * 2
triple = num * 3
squareroot = num ** (1/2)

print('\nO dobro de {} vale {}.'.format(num, double))
print('O triplo de {} vale {}.'.format(num, triple))
print('A raiz quadrada de {} vale {:.2f}.'.format(num, squareroot))
