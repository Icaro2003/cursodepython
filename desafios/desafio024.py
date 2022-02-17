# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
city = input('Informe o nome de uma cidade: ').strip() 
city_santo = 'SANTO' in city.split()[0].upper()
print('{} começa com "SANTO"? {}'.format(city, city_santo))
