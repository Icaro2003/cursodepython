salary = float(input('Informe seu salário: R$ '))

if salary > 0:
    if salary > 1250:
        percent_readjust = 10
        readjust_salary = salary + (salary * percent_readjust / 100)
    else:
        percent_readjust = 15
        readjust_salary = salary + (salary * percent_readjust / 100)

    print('O funcionário que ganhava R$ {:.2f}, teve um aumento de {}%, agora passa a ganhar R$ {:.2f}.'.format(
        salary, percent_readjust, readjust_salary))
else:
    print('Informe um valor de salário válido!')
