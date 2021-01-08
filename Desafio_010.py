# Crie um programa que leia quanto uma pessoa tem na carteira e mostre em quantos dolares ela pode comprar
# Considere US$1.00=R$ 3,27
real = float(input("Quanto você tem na carteira? R$ "))
dolar = real / 3.27
print("Com R$ {:.2f}, você pode comprar US$ {:.2f}".format(real, dolar))
print("=" * 20)
