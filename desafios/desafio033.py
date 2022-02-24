n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

if n1 < n2 and n1 < n3:
    smaller_num = n1
if n2 < n1 and n2 < n3:
    smaller_num = n2
if n3 < n1 and n3 < n2:
    smaller_num = n3

if n1 > n2 and n2 < n3:
    bigger_num = n1
if n2 > n1 and n2 > n3:
    bigger_num = n2
if n3 > n1 and n3 > n2:
    bigger_num = n3

print('Menor valor: {}'.format(smaller_num))
print('Maior valor: {}'.format(bigger_num))

# smaller_num = n1
# if n2 < n1 and n2 < n3:
#     smaller_num = n2
# if n3 < n1 and n3 < n2:
#     smaller_num = n3

# bigger_num = n1
# if n2 > n1 and n2 > n3:
#     bigger_num = n2
# if n3 > n1 and n3 > n2:
#     bigger_num = n3

# print('Menor valor: {}'.format(smaller_num))
# print('Maior valor: {}'.format(bigger_num))
