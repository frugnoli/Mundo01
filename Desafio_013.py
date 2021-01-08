# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Salário Atual: "))
porcent = float(input("Porcentagem de aumento: "))
novo_sal = salario + (salario * porcent / 100)
print("O salário de R$ {:.2f}, foi reajustado com {}% de aumento, passando para R$ {:.2f}".format(salario, porcent, novo_sal))
print("=" * 20)
