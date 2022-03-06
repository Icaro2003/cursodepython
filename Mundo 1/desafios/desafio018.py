# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
from colorama import Fore

angulo_graus = float(input('Informe um ângulo em graus: '))
angulo_radianos = radians(angulo_graus)

print('\nO ângulo de {}{}º{} tem o SENO de {}{:.2f}º{}'.format(Fore.CYAN,
      angulo_graus, Fore.RESET, Fore.RED, sin(angulo_radianos), Fore.RESET))
print('O ângulo de {}{}º{} tem o COSSENO de {}{:.2f}º{}'.format(Fore.CYAN,
      angulo_graus, Fore.RESET, Fore.RED, cos(angulo_radianos), Fore.RESET))
print('O ângulo de {}{}º{} tem a TANGENTE de {}{:.2f}º{}'.format(
    Fore.CYAN, angulo_graus, Fore.RESET, Fore.RED, tan(angulo_radianos), Fore.RESET))
