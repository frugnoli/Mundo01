# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

prod = float(input("Valor do produto: "))
print("Valor original {:.2f}, com 5% de desconto {:.2f} sai por {:.2f}".format(prod, (prod * 0.05), prod - (prod * 0.05)))
print("=" * 20)