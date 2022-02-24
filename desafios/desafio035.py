print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

side_a = float(input('Informe o 1º lado do triângulo: '))
side_b = float(input('Informe o 2º lado do triângulo: '))
side_c = float(input('Informe o 3º lado do triângulo: '))
condition_side_a = [(side_a > (side_b - side_c)), (side_a < (side_b + side_c))]
condition_side_b = [(side_b > (side_a - side_c)), (side_b < (side_a + side_c))]
condition_side_c = [(side_c > (side_b - side_a)), (side_c < (side_b + side_a))]

if ((condition_side_a[0] and condition_side_a[1]) and (condition_side_b[0] and condition_side_b[1]) and (condition_side_c[0] and condition_side_c[1])):
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
