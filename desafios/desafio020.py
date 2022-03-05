# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
from colorama import Fore

aluno1 = str(input('Informe o nome do primeiro aluno: ')).strip()
aluno2 = str(input('Informe o nome do segundo aluno: ')).strip()
aluno3 = str(input('Informe o nome do terceiro aluno: ')).strip()
aluno4 = str(input('Informe o nome do quarto aluno: ')).strip()
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
ordem_alunos = shuffle(lista_alunos)

print('A ordem de apresentação do trabalho será:\n{}{}{}'.format(Fore.BLUE, lista_alunos, Fore.RESET))
