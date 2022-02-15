# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Informe uma cidade(CAIXA ALTA): ')
santo = "SANTO" in cidade

print('A cidade {} apresenta "SANTO" em seu nome? {}'.format(cidade, santo))
