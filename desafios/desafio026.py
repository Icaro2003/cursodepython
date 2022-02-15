# Crie um programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra "A".
# > Em que posição ela aparece a primeira vez.
# > Em que posição ela aparece a última vez.

frase = input('Informe uma frase: ')
letra_a = frase.count('A')
pos_inicial = frase.find('A')
pos_final = frase.rfind('A')

print('"A" aparece {} vezes na frase: {}.'.format(letra_a, frase))
print('"A" aparece na posição {} da frase: {}.'.format(pos_inicial, frase))
print('"A" aparece na posição {} da frase {}.'.format(pos_final, frase))
