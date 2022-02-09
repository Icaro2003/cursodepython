# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

aluno1 = input('Informe o nome do primeiro aluno: ')
aluno2 = input('Informe o nome do segundo aluno: ')
aluno3 = input('Informe o nome do terceiro aluno: ')
aluno4 = input('Informe o nome do quarto aluno: ')
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
ordem_alunos = shuffle(lista_alunos)

print('A ordem de apresentação do trabalho será:\n{}'.format(lista_alunos))
