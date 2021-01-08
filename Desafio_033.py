# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

v1 = float(input("Primeiro Valor: "))
v2 = float(input("Segundo Valor: "))
v3 = float(input("Terceiro Valor: "))
if v1 > v2 and v1 > v3:
    print("O maior valor digitado foi {}".format(v1))
else:
    if v2 > v1 and v2 > v3:
        print("O maior valor digitado foi {}".format(v2))
    else:
        print("O maior valor digitado foi {}".format(v3))
if v1 < v2 and v1 < v3:
    print("O menor valor digitado foi {}".format(v1))
else:
    if v2 < v1 and v2 < v3:
        print("O menor valor digitado foi {}".format(v2))
    else:
        print("O menor valor digitado foi {}".format(v3))

print("========= Outra forma de verificar =========")
menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
# Verificando o maior
maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))
