# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
# tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

lar = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
area = lar * alt
litros = area / 2
print("Sua parede tem dimensão de {}x{} e sua área é de {:.3f}m2.".format(lar, alt, area))
print("Para pintar essa parede, você precisará de {}l de tinta.".format(litros))
print("=" * 20)