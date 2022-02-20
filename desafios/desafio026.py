# Crie um programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra "A".
# > Em que posição ela aparece a primeira vez.
# > Em que posição ela aparece a última vez.

frase = str(input('Informe uma frase: ')).strip()
frase_upper = frase.upper()
letra_a = frase_upper.count('A')
pos_inicial = frase_upper.find('A') + 1
pos_final = frase_upper.rfind('A') + 1

print('"A" aparece {} vezes na frase: {}.'.format(letra_a, frase))
print('"A" aparece na posição {} da frase: {}.'.format(pos_inicial, frase))
print('"A" aparece na posição {} da frase {}.'.format(pos_final, frase))
