nome = str(input('Digite o nome do aluno: '))
n1 = float(str(input('Digite a primeira nota: ')))
n2 = float(str(input('Digite a segunda nota: ')))
addition = n1 + n2
m = addition / 2

print('O aluno {} teve as notas {} e {}, a média calculada foi {:.2f}.'.format(
    nome, n1, n2, m))
