from colorama import Fore, Back, Style

print('-=' * 18)
print('{}{}Analisador de Triângulos{}'.format(
    Back.WHITE, Fore.BLUE, Style.RESET_ALL))
print('-=' * 18)

side_a = float(input('Primeiro segmento: '))
side_b = float(input('Segundo segmento: '))
side_c = float(input('Terceiro segmento: '))

if (side_a < (side_b + side_c)) and (side_b < (side_a + side_c)) and (side_c < (side_b + side_a)):
    print('Os segmentos acima {}{}PODEM FORMAR{} triângulo!'.format(
        Style.BRIGHT, Fore.BLUE, Style.RESET_ALL))
else:
    print('Os segmentos acima {}{}NÃO PODEM FORMAR{} triângulo!'.format(
        Style.BRIGHT, Fore.RED, Style.RESET_ALL))
