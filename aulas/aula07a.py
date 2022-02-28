n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

addition = n1 + n2
subtraction = n1 - n2
multiplication = n1 * n2
division = n1 / n2
int_division = n1 // n2
exponentiation = n1 ** n2

print('{} + {} = {}'.format(n1, n2, addition))
print('{} - {} = {}'.format(n1, n2, subtraction))
print('{} x {} = {}'.format(n1, n2, multiplication))
print('{} / {} = {:.3f}'.format(n1, n2, division))
print('{} // {} = {}'.format(n1, n2, int_division))
print('{}^{} = {}'.format(n1, n2, exponentiation))
