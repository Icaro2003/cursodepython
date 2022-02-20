salary = float(input('Informe o salário do funcionário: R$ '))
readjust=salary + (salary * 15 / 100)

print('O funcionário que ganhava R$ {}, com um aumento de 15%, passa a receber um salário de R$ {:.2f}.'.format(
    salary, readjust))
