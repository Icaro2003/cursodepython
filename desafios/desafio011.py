width = float(input('Informe a largura da parede: '))
height = float(input('Informe a altura da parede: '))
area = width * height
ink_liter = area / 2

print('\nSua parede tem a dimensão de {} X {}, logo sua área é de {}m²'.format(
    width, height, area))
print('Para pintar uma parede com área de {}m², você precisará de {}l de tinta'.format(
    area, ink_liter))
