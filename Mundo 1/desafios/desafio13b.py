from colorama import Fore, Style

produto = float(input('Digite o preço do produto: R$ '))
produto_vista = produto - ((produto * 10) / 100)
produto_prazo = produto + ((produto * 8) / 100)

print('O produto que custava {}R$ {}{}, quando comprado à vista tem um desconto de {}10%{}, e passa a custar: {}{}R$ {}{}.'.format(
    Fore.GREEN, produto, Fore.RESET, Style.BRIGHT, Style.RESET_ALL, Style.BRIGHT, Fore.GREEN, produto_vista, Style.RESET_ALL))
print('O produto que custava {}R$ {}{}, quando comprado à prazo tem um aumento de {}8%{}, e passa a custar {}{}R$ {:.2f}{}.'.format(
    Fore.GREEN, produto, Fore.RESET, Style.BRIGHT, Style.RESET_ALL, Style.BRIGHT, Fore.GREEN, produto_prazo, Style.RESET_ALL))
