print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)

side_a = float(input('Primeiro segmento: '))
side_b = float(input('Segundo segmento: '))
side_c = float(input('Terceiro segmento: '))

if (side_a < (side_b + side_c)) and (side_b < (side_a + side_c)) and (side_c < (side_b + side_a)):
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
