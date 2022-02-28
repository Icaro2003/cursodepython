from colorama import Fore

m = float(str(input('Digite uma distância em metros: ')))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('A distância de {}{} m{} equivale a:'.format(Fore.RED, m, Fore.RESET))
print('{}{} km{}'.format(Fore.BLUE, km, Fore.RESET))
print('{}{} hm{}'.format(Fore.BLUE, hm, Fore.RESET))
print('{}{} dam{}'.format(Fore.BLUE, dam, Fore.RESET))
print('{}{} dm{}'.format(Fore.BLUE, dm, Fore.RESET))
print('{}{} cm{}'.format(Fore.BLUE, cm, Fore.RESET))
print('{}{} mm{}'.format(Fore.BLUE, mm, Fore.RESET))
