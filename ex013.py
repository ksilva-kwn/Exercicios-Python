larg= float (input('Digite a largura da parede : '))
alt= float (input('Digite a altura da parede : '))
area = larg * alt
tinta = area / 2

print('A área da parede corresponde a {:.1f}m2'.format(area))
print('Para pintar essa parede, você precisará de {:.1f}L de tinta'.format(tinta))
