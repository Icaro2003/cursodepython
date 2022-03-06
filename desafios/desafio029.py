from colorama import Fore, Style

velocity = float(input('Informe a velocidade do carro(Km/h): '))
above_80km = 0

if velocity > 80:
    above_80km = (velocity - 80) * 7
    print('{}MULTADO!{} Seu carro excedeu o limite permitido que é de {}80 Km/h!{}'.format(
        Style.BRIGHT, Style.RESET_ALL, Fore.RED, Fore.RESET))
    print('Você deve pagar uma multa de {}R$ {:.2f}!{}'.format(
        Fore.GREEN, above_80km, Fore.RESET))

print('Tenha um bom dia! Dirija com segurança!')
