# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
a = float(input("Digita o ângulo que deseja: "))
print("O ângulo de {} tem o SENO de {:.2F}".format(a, sin(radians(a))))
print("O ângulo de {} tem o COSSENO de {:.2F}".format(a, cos(radians(a))))
print("O ângulo de {} tem o TANGENTE de {:.2F}".format(a, tan(radians(a))))
