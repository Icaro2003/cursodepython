num1 = int(str(input('Digite um número: ')))
num2 = int(str(input('Digite outro número: ')))
addt = num1 + num2

print('{}{}{} + {}{}{} = {}{}{}'.format('\033[36m', num1, '\033[m', '\033[36m', num2, '\033[m', '\033[31m', addt, '\033[m'))
