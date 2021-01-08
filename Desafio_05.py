print("\033[1;31mInforme um inteiro e mostre o antecessor e o sucessor.\033[m")
num = int(input("Informe um número inteiro: "))
print("Analisando o valor de {}, o antecessor é {} e o sucessor {}.".format(num, (num - 1), (num + 1)))
print("=" * 100)