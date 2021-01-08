# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

cels = float(input("Informe a temperatura em Celsius: "))
fahr = (cels * 9 / 5) + 32
print("A temperatura {} Celsius, convertido para Fahrenheit é {}".format(cels, fahr))
print("=" * 20)