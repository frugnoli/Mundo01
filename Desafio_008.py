print("\033[1;31mEscreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.\033[m")
num = float(input("A distância em metros: "))
print("A medida em metros {} m, convertido para {:.0f} cm e para {:.0f} mm".format(num, (num * 100), (num * 1000)))
print("=" * 100)