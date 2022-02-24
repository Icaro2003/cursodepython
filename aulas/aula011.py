name = 'Ícaro'
colors_text = {
    'clear': '\033[m',
    'blue': '\033[34m',
    'yellow': '\033[33m',
    'negative': '\033[7;30m'
}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(
    colors_text['negative'], name, colors_text['clear']))
