# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
from colorama import Fore

aluno1 = str(input('Informe o nome do primeiro aluno: ')).strip()
aluno2 = str(input('Informe o nome do segundo aluno: ')).strip()
aluno3 = str(input('Informe o nome do terceiro aluno: ')).strip()
aluno4 = str(input('Informe o nome do quarto aluno: ')).strip()
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
escolha_alunos = choice(lista_alunos)

print('O aluno escolhido foi {}{}{}.'.format(
    Fore.BLUE, escolha_alunos, Fore.RESET))
