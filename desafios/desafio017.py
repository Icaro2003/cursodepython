# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import sqrt
# from math import hypot

co = float(input('Informe o comprimento do cateto oposto do triângulo retângulo: '))
ca = float(
    input('Informe o comprimento do cateto adjacente do triângulo retângulo: '))
h = sqrt((co ** 2) + (ca ** 2))
# h = hypot(co, ca)

print('Com o cateto oposto medindo {} e o cateto adjacente {}, a hipotenusa vai medir {:.2f}.'.format(co, ca, h))
