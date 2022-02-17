# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo_graus = float(str(input('Informe um ângulo em graus: ')))
angulo_radianos = radians(angulo_graus)

print('\nO ângulo de {}º tem o SENO de {:.2f}º'.format(
    angulo_graus, sin(angulo_radianos)))
print('O ângulo de {}º tem o COSSENO de {:.2f}º'.format(
    angulo_graus, cos(angulo_radianos)))
print('O ângulo de {}º tem a TANGENTE de {:.2f}º'.format(
    angulo_graus, tan(angulo_radianos)))
